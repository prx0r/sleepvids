#!/usr/bin/env python3
"""
Train Compositor — depth-aware parallax + station name popups + lighting transition
Uses Pillow + FFmpeg (no OpenCV needed).
"""

import numpy as np
import subprocess
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent.parent


def generate_depth_map(width, height):
    Y, X = np.ogrid[:height, :width]
    cy, cx = height // 2, width // 2
    max_dist = math.sqrt(cx**2 + cy**2)
    return np.sqrt((X - cx)**2 + (Y - cy)**2) / max_dist


def apply_parallax(img_array, depth, dx, dy):
    h, w = img_array.shape[:2]
    Y, X = np.ogrid[:h, :w]
    src_x = np.clip(X + (depth * dx).astype(np.int32), 0, w - 1)
    src_y = np.clip(Y + (depth * dy).astype(np.int32), 0, h - 1)
    return img_array[src_y, src_x]


def composite_frame(img, depth, frame_num, total_frames, fps=12, station_name="", show_station=False):
    t = frame_num / total_frames
    dx = 4 * math.sin(t * 2 * math.pi * 0.25)
    dy = 2 * math.sin(t * 2 * math.pi * 0.15)

    img_array = np.array(img)
    result = apply_parallax(img_array, depth, dx, dy)
    frame = Image.fromarray(result)

    draw = ImageDraw.Draw(frame)
    w, h = frame.size

    if show_station and station_name:
        font_size = int(h * 0.06)
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
        except (IOError, OSError):
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), station_name, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]

        px = (w - tw) // 2
        py = int(h * 0.15)

        draw.rectangle(
            [px - 20, py - 10, px + tw + 20, py + th + 10],
            fill=(0, 0, 0, 180)
        )

        draw.text((px, py), station_name, fill=(255, 255, 255), font=font)

    if t > 0.3:
        dim = min(1.0, (t - 0.3) / 0.1)
        darkened = Image.fromarray(
            (np.array(frame).astype(np.float32) * (1 - dim * 0.4)).astype(np.uint8)
        )
        return darkened

    return frame


def generate_video(carriage_path, depth, out_dir, audio_path, duration_sec=10, fps=12,
                   stations=None, station_times=None):
    total_frames = duration_sec * fps
    print(f"Generating {total_frames} frames...")

    img = Image.open(carriage_path).resize((512, 512), Image.LANCZOS)

    for i in range(total_frames):
        t_sec = i / fps
        show_station = False
        station_name = ""

        if stations and station_times:
            for st_name, st_time in zip(stations, station_times):
                if st_time <= t_sec <= st_time + 3:
                    show_station = True
                    station_name = st_name
                    break

        frame = composite_frame(img, depth, i, total_frames, fps, station_name, show_station)
        frame_path = out_dir / f"frame_{i:05d}.png"
        frame.save(frame_path)
        if i % (fps * 2) == 0:
            print(f"  Frame {i}/{total_frames} ({i/total_frames*100:.0f}%)")

    print("Encoding video...")
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(fps),
        "-i", str(out_dir / "frame_%05d.png"),
        "-i", str(audio_path),
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        str(out_dir.parent / "preview_lofi.mp4")
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    print(f"  ✓ Video: {out_dir.parent / 'preview_lofi.mp4'}")


if __name__ == "__main__":
    carriage = ROOT / "train_journeys/assets/train_carriage.png"
    if not carriage.exists():
        carriage = ROOT / "longhaul/assets/ba_window.jpg"

    audio = ROOT / "train_journeys/videos/001_lon_edi/output/ambient.wav"
    out_dir = ROOT / "train_journeys/videos/001_lon_edi/output/frames"
    out_dir.mkdir(parents=True, exist_ok=True)

    stations = ["London Kings Cross", "York", "Darlington", "Edinburgh Waverley"]
    station_times = [0, 30, 60, 90]

    print("Generating depth map (512x512)...")
    depth = generate_depth_map(512, 512)
    print(f"  Depth: {depth.shape}")

    print("\nGenerating 10s preview...")
    generate_video(carriage, depth, out_dir, audio, duration_sec=10, fps=12,
                   stations=stations, station_times=station_times)

    print("\nDone!")
