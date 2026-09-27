#!/usr/bin/env python3
"""
Long Haul Flight Engine
One command → full sleep video from flight data.

Usage:
    python3 engine.py --route videos/001_ba_lhr_jfk_business/route.json
    python3 engine.py --route videos/001_ba_lhr_jfk_business/route.json --preview
"""

import argparse
import json
import subprocess
import os
import sys
import math
from pathlib import Path

ROOT = Path(__file__).parent.parent
ENGINE = Path(__file__).parent

# ============================================================
# STEP 1: Load route data
# ============================================================

def load_route(route_path):
    with open(route_path) as f:
        return json.load(f)

# ============================================================
# STEP 2: Generate cabin ambiance
# ============================================================
def generate_ambient(duration_sec, output_path):
    """Generate cabin ambiance: pink noise base + lowpass."""
    cmd = [
        "ffmpeg", "-y", "-f", "lavfi", "-i",
        f"anoisesrc=d={duration_sec}:c=pink:r=44100:a=0.04",
        "-af", "lowpass=f=600",
        "-t", str(duration_sec), "-ar", "44100", "-ac", "2",
        str(output_path)
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    print(f"  ✓ Ambient: {duration_sec}s → {output_path.name}")

# ============================================================
# STEP 3: Generate TTS announcements
# ============================================================

def generate_announcements(announcements, output_dir):
    """Generate TTS for each announcement using edge-tts."""
    audio_files = []
    for i, ann in enumerate(announcements):
        out = output_dir / f"ann_{i:02d}.mp3"
        text = ann["text"]
        cmd = [
            "edge-tts",
            "--voice", "en-GB-RyanNeural",  # British male
            "--rate", "-10%",
            "--text", text,
            "--write-media", str(out)
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        audio_files.append({"time": ann["time"], "path": out})
        print(f"  ✓ TTS [{ann['time']}]: {text[:60]}...")
    return audio_files

# ============================================================
# STEP 4: Build announcement timeline
# ============================================================

def build_timeline(announcements, total_duration):
    """Create silence + announcement segments for the full timeline."""
    segments = []
    prev_time = 0
    
    for ann in sorted(announcements, key=lambda x: parse_time(x["time"])):
        target_time = parse_time(ann["time"])
        if target_time > prev_time:
            silence_dur = target_time - prev_time
            segments.append({"type": "silence", "duration": silence_dur})
        segments.append({"type": "announcement", "path": ann["path"], "time": target_time})
        prev_time = target_time
    
    # Add remaining silence after last announcement
    if prev_time < total_duration:
        segments.append({"type": "silence", "duration": total_duration - prev_time})
    
    return segments

def concatenate_segments(segments, output_path):
    """Concatenate silence + announcements into single audio track."""
    # Build silence segments and announcement segments
    files = []
    for seg in segments:
        if seg["type"] == "silence":
            silence_path = output_dir / f"silence_{seg['duration']:.0f}.wav"
            cmd = [
                "ffmpeg", "-y", "-f", "lavfi", "-i",
                f"anullsrc=r=44100:cl=stereo",
                "-t", str(seg["duration"]),
                str(silence_path)
            ]
            subprocess.run(cmd, capture_output=True, check=True)
            files.append(silence_path)
        else:
            files.append(seg["path"])
    
    # Create concat list
    list_path = output_dir / "concat.txt"
    with open(list_path, "w") as f:
        for fp in files:
            f.write(f"file '{fp}'\n")
    
    # Concatenate
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(list_path),
        "-c", "copy",
        str(output_path)
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    print(f"  ✓ Timeline: {len(segments)} segments → {output_path.name}")

# ============================================================
# STEP 5: Mix ambient + announcements with ducking
# ============================================================

def mix_audio(ambient_path, narration_path, output_path):
    """Mix ambient + narration with sidechain ducking."""
    cmd = [
        "ffmpeg", "-y",
        "-i", str(narration_path),
        "-i", str(ambient_path),
        "-filter_complex",
        "[1:a]volume=0.25[bg];"
        "[0:a]volume=1.0[narr];"
        "[narr][bg]amix=inputs=2:duration=longest:dropout_transition=2[mixed];"
        "[mixed]loudnorm=I=-16:TP=-1.5[out]",
        "-map", "[out]",
        "-ar", "44100", "-ac", "2",
        str(output_path)
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    print(f"  ✓ Mixed: {output_path.name}")

# ============================================================
# STEP 6: Build video (static image + audio)
# ============================================================

def build_video(image_path, audio_path, output_path):
    """Build MP4 from static image + audio."""
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", str(image_path),
        "-i", str(audio_path),
        "-c:v", "libx264", "-tune", "stillimage",
        "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        str(output_path)
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    print(f"  ✓ Video: {output_path.name}")

# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Long Haul Flight Engine")
    parser.add_argument("--route", required=True, help="Path to route.json")
    parser.add_argument("--preview", action="store_true", help="Preview mode (10 min)")
    args = parser.parse_args()
    
    route = load_route(args.route)
    flight = route.get("flight", route.get("airline", "Unknown"))
    route_data = route.get("route", route)
    cabin = route.get("cabin_class", "Economy")
    
    dep = route_data.get("departure", {}).get("airport", "???" if isinstance(route_data.get("departure"), str) else "???")
    arr = route_data.get("arrival", {}).get("airport", "???" if isinstance(route_data.get("arrival"), str) else "???")
    
    print(f"\n{'='*60}")
    print(f"  LONG HAUL — {flight}")
    print(f"  {dep} → {arr}")
    print(f"  {cabin}")
    print(f"{'='*60}\n")
    
    # Output directory
    route_dir = Path(args.route).parent
    out_dir = route_dir / "output"
    out_dir.mkdir(exist_ok=True)
    
    # Duration (full or preview)
    flight_time = route_data.get("typical_flight_time", "7h 0m")
    try:
        total_hours = float(flight_time.split("h")[0])
    except:
        total_hours = 7.0
    total_sec = int(total_hours * 3600) if not args.preview else 600  # 10 min preview
    
    print(f"Duration: {total_sec/3600:.1f} hours")
    print()
    
    # Step 1: Generate ambient
    print("[1/5] Generating ambient...")
    ambient_path = out_dir / "ambient.wav"
    generate_ambient(total_sec, ambient_path)
    
    # Step 2: Generate TTS announcements
    print("[2/5] Generating announcements...")
    ann_dir = out_dir / "announcements"
    ann_dir.mkdir(exist_ok=True)
    # Load script if exists
    script_path = Path(args.route).parent / "script.json"
    if script_path.exists():
        with open(script_path) as f:
            script = json.load(f)
        announcements = script["announcements"]
    else:
        announcements = [{"time": "0:30", "text": f"Good evening, this is your captain speaking on {flight}."}]
    
    # Filter for preview
    if args.preview:
        max_time = total_sec
        announcements = [a for a in announcements if parse_time(a["time"]) <= max_time]
    
    ann_files = generate_announcements(announcements, ann_dir)

def parse_time(time_str):
    """Parse time string like '0:30', '4:00', '240:00' to seconds."""
    parts = time_str.split(":")
    if len(parts) == 2:
        return int(parts[0]) * 60 + int(parts[1])
    return int(parts[0])
    
    # Step 3: Build timeline
    print("[3/5] Building timeline...")
    timeline = build_timeline(announcements, total_sec)
    narration_path = out_dir / "narration.wav"
    concatenate_segments(timeline, narration_path)
    
    # Step 4: Mix
    print("[4/5] Mixing audio...")
    mixed_path = out_dir / "mixed.wav"
    mix_audio(ambient_path, narration_path, mixed_path)
    
    # Step 5: Build video
    print("[5/5] Building video...")
    # Select cabin image based on class
    cabin_images = {
        "first": ENGINE.parent / "assets" / "ba_forward.jpg",
        "business": ENGINE.parent / "assets" / "ba_forward.jpg",
        "economy": ENGINE.parent / "assets" / "ba_forward.jpg",
    }
    cabin_image = cabin_images.get(cabin, ENGINE.parent / "assets" / "ba_forward.jpg")
    if not cabin_image.exists():
        cabin_image = ENGINE.parent / "assets" / "ba_business_cabin.jpg"
    video_path = out_dir / f"{flight}_{route_data['departure']['iata']}_{route_data['arrival']['iata']}.mp4"
    
    if cabin_image.exists():
        build_video(cabin_image, mixed_path, video_path)
    else:
        # Build video from audio only (no image)
        cmd = ["ffmpeg", "-y", "-i", str(mixed_path), "-c:a", "aac", str(video_path)]
        subprocess.run(cmd, capture_output=True, check=True)
        print(f"  ✓ Audio-only video: {video_path.name}")
    
    print(f"\n{'='*60}")
    print(f"  DONE: {video_path}")
    print(f"  Duration: {total_sec/3600:.1f} hours")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
