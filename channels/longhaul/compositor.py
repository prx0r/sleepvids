#!/usr/bin/env python3
"""
Cabin Compositor — depth-aware parallax + overlays + lighting transition
Uses Pillow + FFmpeg (no OpenCV needed).
"""

import numpy as np
import subprocess
import math
from pathlib import Path
from PIL import Image, ImageDraw

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

def composite_frame(img, depth, frame_num, total_frames, fps=12):
    t = frame_num / total_frames
    dx = 3 * math.sin(t * 2 * math.pi * 0.5)
    dy = 2 * math.sin(t * 2 * math.pi * 0.3)
    
    img_array = np.array(img)
    result = apply_parallax(img_array, depth, dx, dy)
    frame = Image.fromarray(result)
    
    draw = ImageDraw.Draw(frame)
    w, h = frame.size
    sx, sy = int(w * 0.35), int(h * 0.25)
    sw, sh = int(w * 0.3), int(h * 0.25)
    
    for i in range(50):
        tp = i / 50 * t
        px = int(sx + sw * 0.1 + sw * 0.8 * tp)
        py = int(sy + sh * 0.3 + sh * 0.4 * math.sin(tp * math.pi))
        draw.ellipse([px-1, py-1, px+1, py+1], fill=(74, 158, 255))
    
    path_x = int(sx + sw * 0.1 + sw * 0.8 * t)
    path_y = int(sy + sh * 0.3 + sh * 0.4 * math.sin(t * math.pi))
    draw.ellipse([path_x-3, path_y-3, path_x+3, path_y+3], fill=(74, 158, 255))
    
    if t > 0.3:
        dim = min(1.0, (t - 0.3) / 0.1)
        darkened = Image.fromarray((np.array(frame).astype(np.float32) * (1 - dim * 0.5)).astype(np.uint8))
        return darkened
    
    return frame

def generate_video(cabin_path, depth, out_dir, audio_path, duration_sec=10, fps=12):
    total_frames = duration_sec * fps
    print(f"Generating {total_frames} frames...")
    
    img = Image.open(cabin_path).resize((512, 512), Image.LANCZOS)
    
    for i in range(total_frames):
        frame = composite_frame(img, depth, i, total_frames, fps)
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
    cabin = ROOT / "longhaul/assets/ba_forward.png"
    audio = ROOT / "longhaul/videos/001_ba_lhr_jfk_business/output/ambient.wav"
    out_dir = ROOT / "longhaul/videos/001_ba_lhr_jfk_business/output/frames"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    print("Generating depth map (512x512)...")
    depth = generate_depth_map(512, 512)
    print(f"  Depth: {depth.shape}")
    
    print("\nGenerating 10s preview...")
    generate_video(cabin, depth, out_dir, audio, duration_sec=10, fps=12)
    
    print("\nDone!")
