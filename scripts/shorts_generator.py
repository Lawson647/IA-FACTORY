#!/usr/bin/env python3
"""
IA Factory — Shorts Generator
Génère automatiquement des Shorts/Reels/TikTok à partir d'une vidéo longue YouTube.

Usage:
    python shorts_generator.py --input video.mp4 --output shorts/
    python shorts_generator.py --input video.mp4 --output shorts/ --count 3 --duration 45

Dépendances:
    pip install moviepy opencv-python-headless srt whisper openai pillow numpy

Étapes:
1. Extrait l'audio
2. Transcrit avec Whisper
3. Détecte les moments forts (silences, mots-clés, pics audio)
4. Génère des clips 9:16 avec sous-titres
5. Ajoute un hook visuel et un CTA final
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

import cv2
import numpy as np
from moviepy.editor import (
    AudioFileClip,
    ColorClip,
    CompositeVideoClip,
    ImageClip,
    TextClip,
    VideoFileClip,
)
from PIL import Image, ImageDraw, ImageFont


def ensure_dir(path: str) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def extract_audio(video_path: str, output_path: str) -> str:
    """Extrait l'audio d'une vidéo en WAV."""
    cmd = [
        "ffmpeg", "-y", "-i", video_path,
        "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1",
        output_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path


def transcribe_audio(audio_path: str) -> List[dict]:
    """Transcrit l'audio avec Whisper (local)."""
    try:
        import whisper
        model = whisper.load_model("base")
        result = model.transcribe(audio_path, word_timestamps=True)
        return result["segments"]
    except Exception as e:
        print(f"⚠️ Whisper a échoué: {e}")
        print("Assure-toi d'avoir installé whisper : pip install openai-whisper")
        return []


def detect_highlights(segments: List[dict], keyword_boost: List[str] = None) -> List[Tuple[float, float, str]]:
    """
    Détecte les moments forts à partir des segments Whisper.
    Retourne une liste de (start, end, text).
    """
    keyword_boost = keyword_boost or [
        "résultat", "gagné", "gagner", "temps", "argent", "test", "outil",
        "incroyable", "vraiment", "automatiser", "agent", "abonne"
    ]

    scored_segments = []
    for seg in segments:
        text = seg["text"].lower()
        score = seg["end"] - seg["start"]  # base : durée

        # Bonus mots-clés
        for kw in keyword_boost:
            if kw in text:
                score += 2.0

        # Bonus phrases courtes percutantes
        if 5 <= len(text) <= 80:
            score += 1.0

        scored_segments.append((score, seg["start"], seg["end"], seg["text"]))

    # Trier par score décroissant
    scored_segments.sort(reverse=True)
    return [(s, e, t) for _, s, e, t in scored_segments]


def find_best_moments(
    video_path: str,
    audio_path: str,
    num_clips: int = 3,
    target_duration: int = 45,
    min_duration: int = 20,
) -> List[Tuple[float, float, str]]:
    """Trouve les meilleurs moments pour créer des Shorts."""
    segments = transcribe_audio(audio_path)
    if not segments:
        # Fallback : découper en segments réguliers
        with VideoFileClip(video_path) as clip:
            duration = clip.duration
        step = duration / (num_clips + 1)
        return [(i * step, i * step + target_duration, "Moment clé") for i in range(1, num_clips + 1)]

    highlights = detect_highlights(segments)

    selected = []
    used_ranges = []

    for start, end, text in highlights:
        if len(selected) >= num_clips:
            break

        # Éviter les chevauchements
        overlap = any(
            (start < u_end and end > u_start) for u_start, u_end in used_ranges
        )
        if overlap:
            continue

        # Ajuster la durée
        clip_duration = end - start
        if clip_duration < min_duration:
            end = min(start + target_duration, segments[-1]["end"])
        elif clip_duration > target_duration:
            end = start + target_duration

        selected.append((start, end, text))
        used_ranges.append((start, end))

    return selected


def create_subtitle_image(text: str, width: int, height: int, font_size: int = 48) -> np.ndarray:
    """Crée une image PNG avec sous-titres stylisés (fond noir, texte blanc)."""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Utiliser une police système
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except Exception:
        font = ImageFont.load_default()

    # Ligne de fond semi-transparente
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    padding = 20
    x = (width - text_w) // 2
    y = (height - text_h) // 2

    draw.rounded_rectangle(
        [x - padding, y - padding, x + text_w + padding, y + text_h + padding],
        radius=20,
        fill=(0, 0, 0, 180)
    )

    # Contour jaune
    draw.text((x - 2, y - 2), text, font=font, fill=(255, 215, 0, 255))
    draw.text((x + 2, y + 2), text, font=font, fill=(255, 215, 0, 255))
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

    return np.array(img)


def generate_short(
    video_path: str,
    start: float,
    end: float,
    text: str,
    output_path: str,
    target_size: Tuple[int, int] = (1080, 1920),
    hook_text: str = "⚡ Résultat surprenant",
    cta_text: str = "Abonne-toi 🔴",
) -> str:
    """Génère un Short 9:16 à partir d'un segment vidéo."""
    with VideoFileClip(video_path) as clip:
        subclip = clip.subclip(start, end)

        # Redimensionner en 9:16 (crop center)
        w, h = subclip.size
        target_w, target_h = target_size

        # Hauteur cible = target_h, largeur proportionnelle
        new_h = target_h
        new_w = int(w * new_h / h)
        resized = subclip.resize(height=new_h)

        # Si plus large que target, crop au centre
        if new_w > target_w:
            x_center = new_w // 2
            x1 = x_center - target_w // 2
            x2 = x1 + target_w
            cropped = resized.crop(x1=x1, x2=x2)
        else:
            # Sinon, ajouter des bandes noires
            cropped = resized

        # Hook (2 premières secondes)
        hook = (
            TextClip(
                hook_text,
                fontsize=64,
                color="white",
                font="DejaVu-Sans-Bold",
                stroke_color="black",
                stroke_width=3,
                size=(target_w, 200),
                method="caption",
            )
            .set_position(("center", 150))
            .set_duration(2.0)
            .set_start(0)
        )

        # Sous-titre central
        subtitle = (
            TextClip(
                text[:80],
                fontsize=48,
                color="yellow",
                font="DejaVu-Sans-Bold",
                stroke_color="black",
                stroke_width=2,
                size=(target_w - 100, 300),
                method="caption",
                align="center",
            )
            .set_position(("center", target_h - 400))
            .set_duration(end - start)
        )

        # CTA final (3 dernières secondes)
        cta = (
            TextClip(
                cta_text,
                fontsize=56,
                color="white",
                font="DejaVu-Sans-Bold",
                stroke_color="red",
                stroke_width=3,
                size=(target_w, 150),
                method="caption",
                align="center",
            )
            .set_position(("center", target_h - 250))
            .set_duration(3.0)
            .set_start(max(0, (end - start) - 3.0))
        )

        final = CompositeVideoClip([cropped, hook, subtitle, cta], size=target_size)
        final = final.set_audio(cropped.audio)

        final.write_videofile(
            output_path,
            codec="libx264",
            audio_codec="aac",
            fps=30,
            threads=4,
            logger=None,
        )

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Générateur de Shorts IA Factory")
    parser.add_argument("--input", "-i", required=True, help="Vidéo source (MP4)")
    parser.add_argument("--output", "-o", default="shorts/", help="Dossier de sortie")
    parser.add_argument("--count", "-n", type=int, default=3, help="Nombre de Shorts à générer")
    parser.add_argument("--duration", "-d", type=int, default=45, help="Durée cible par Short (secondes)")
    parser.add_argument("--hook", default="⚡ Résultat surprenant", help="Texte du hook")
    parser.add_argument("--cta", default="Abonne-toi 🔴", help="Texte du CTA final")
    parser.add_argument("--keywords", default="", help="Mots-clés boostés, séparés par des virgules")
    args = parser.parse_args()

    video_path = Path(args.input)
    if not video_path.exists():
        print(f"❌ Vidéo non trouvée : {video_path}")
        sys.exit(1)

    output_dir = ensure_dir(args.output)

    print(f"🎬 Traitement de : {video_path}")

    # Étape 1 : extraire l'audio
    audio_path = output_dir / "temp_audio.wav"
    print("🔊 Extraction audio...")
    extract_audio(str(video_path), str(audio_path))

    # Étape 2 : trouver les meilleurs moments
    print("🧠 Analyse des moments forts...")
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    moments = find_best_moments(
        str(video_path),
        str(audio_path),
        num_clips=args.count,
        target_duration=args.duration,
    )

    print(f"✅ {len(moments)} moments trouvés")

    # Étape 3 : générer les Shorts
    generated = []
    for idx, (start, end, text) in enumerate(moments, 1):
        output_file = output_dir / f"short_{idx:02d}.mp4"
        print(f"\n🎞️  Génération Short #{idx} ({start:.1f}s - {end:.1f}s)")
        print(f"   Texte : {text[:60]}...")

        generate_short(
            str(video_path),
            start,
            end,
            text,
            str(output_file),
            hook_text=args.hook,
            cta_text=args.cta,
        )
        generated.append(str(output_file))
        print(f"   ✅ Sauvegardé : {output_file}")

    # Nettoyer
    audio_path.unlink(missing_ok=True)

    print(f"\n🚀 {len(generated)} Shorts générés dans {output_dir}:")
    for g in generated:
        print(f"   - {g}")


if __name__ == "__main__":
    main()
