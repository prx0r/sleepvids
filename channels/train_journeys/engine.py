#!/usr/bin/env python3
"""
Train Journeys Engine
One command → full sleep video from route data.

Usage:
    python3 engine.py --route videos/001_lon_edi/route.json
    python3 engine.py --route videos/001_lon_edi/route.json --preview
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


def load_route(route_path):
    with open(route_path) as f:
        return json.load(f)


def generate_ambient(duration_sec, output_path):
    """Generate carriage ambiance: brown noise base + rhythmic click."""
    cmd = [
        "ffmpeg", "-y", "-f", "lavfi", "-i",
        f"anoisesrc=d={duration_sec}:c=brown:r=44100:a=0.03",
        "-af", "lowpass=f=400",
        "-t", str(duration_sec), "-ar", "44100", "-ac", "2",
        str(output_path)
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    print(f"  ✓ Ambient: {duration_sec}s → {output_path.name}")


def generate_rhythm_track(duration_sec, output_path, output_dir, bpm=60):
    """Generate rhythmic wheel-on-track sound."""
    interval = 60.0 / bpm
    num_beats = int(duration_sec / interval)
    files = []

    for i in range(num_beats):
        beat_path = output_dir / f"beat_{i:05d}.wav"
        cmd = [
            "ffmpeg", "-y", "-f", "lavfi", "-i",
            f"anullsrc=r=44100:cl=mono",
            "-t", "0.05",
            "-af", "volume=0.15,highpass=f=200,lowpass=f=800",
            str(beat_path)
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        files.append((i * interval, beat_path))

    segments = []
    prev_time = 0
    for t, path in files:
        if t > prev_time:
            silence_dur = t - prev_time
            silence_path = output_dir / f"silence_{prev_time:.2f}.wav"
            cmd = [
                "ffmpeg", "-y", "-f", "lavfi", "-i",
                f"anullsrc=r=44100:cl=mono",
                "-t", str(silence_dur),
                str(silence_path)
            ]
            subprocess.run(cmd, capture_output=True, check=True)
            segments.append(silence_path)
        segments.append(path)
        prev_time = t + 0.05

    if prev_time < duration_sec:
        silence_dur = duration_sec - prev_time
        silence_path = output_dir / f"silence_end.wav"
        cmd = [
            "ffmpeg", "-y", "-f", "lavfi", "-i",
            f"anullsrc=r=44100:cl=mono",
            "-t", str(silence_dur),
            str(silence_path)
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        segments.append(silence_path)

    list_path = output_dir / "rhythm_concat.txt"
    with open(list_path, "w") as f:
        for fp in segments:
            f.write(f"file '{fp}'\n")

    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(list_path),
        "-c", "copy",
        str(output_path)
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    print(f"  ✓ Rhythm track: {num_beats} beats → {output_path.name}")


def generate_announcements(announcements, output_dir):
    """Generate TTS for each announcement using edge-tts."""
    audio_files = []
    for i, ann in enumerate(announcements):
        out = output_dir / f"ann_{i:02d}.mp3"
        text = ann["text"]
        cmd = [
            "edge-tts",
            "--voice", "en-GB-RyanNeural",
            "--rate", "-15%",
            "--text", text,
            "--write-media", str(out)
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        audio_files.append({"time": ann["time"], "path": out, "station": ann.get("station", "")})
        print(f"  ✓ TTS [{ann['time']}]: {text[:60]}...")
    return audio_files


def parse_time(time_str):
    """Parse time string like '0:30', '4:00', '240:00' to seconds."""
    parts = time_str.split(":")
    if len(parts) == 2:
        return int(parts[0]) * 60 + int(parts[1])
    return int(parts[0])


def build_timeline(announcements, total_duration):
    """Create silence + announcement segments for the full timeline."""
    segments = []
    prev_time = 0

    for ann in sorted(announcements, key=lambda x: parse_time(x["time"])):
        target_time = parse_time(ann["time"])
        if target_time > prev_time:
            silence_dur = target_time - prev_time
            segments.append({"type": "silence", "duration": silence_dur})
        segments.append({"type": "announcement", "path": ann["path"], "time": target_time, "station": ann.get("station", "")})
        prev_time = target_time

    if prev_time < total_duration:
        segments.append({"type": "silence", "duration": total_duration - prev_time})

    return segments


def concatenate_segments(segments, output_path, output_dir):
    """Concatenate silence + announcements into single audio track."""
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

    list_path = output_dir / "concat.txt"
    with open(list_path, "w") as f:
        for fp in files:
            f.write(f"file '{fp}'\n")

    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(list_path),
        "-c", "copy",
        str(output_path)
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    print(f"  ✓ Timeline: {len(segments)} segments → {output_path.name}")


def mix_audio(ambient_path, rhythm_path, narration_path, output_path):
    """Mix ambient + rhythm + narration with ducking."""
    cmd = [
        "ffmpeg", "-y",
        "-i", str(narration_path),
        "-i", str(ambient_path),
        "-i", str(rhythm_path),
        "-filter_complex",
        "[1:a]volume=0.2[bg];"
        "[2:a]volume=0.3[rhythm];"
        "[0:a]volume=1.0[narr];"
        "[narr][bg][rhythm]amix=inputs=3:duration=longest:dropout_transition=2[mixed];"
        "[mixed]loudnorm=I=-16:TP=-1.5[out]",
        "-map", "[out]",
        "-ar", "44100", "-ac", "2",
        str(output_path)
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    print(f"  ✓ Mixed: {output_path.name}")


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


def main():
    parser = argparse.ArgumentParser(description="Train Journeys Engine")
    parser.add_argument("--route", required=True, help="Path to route.json")
    parser.add_argument("--preview", action="store_true", help="Preview mode (10 min)")
    args = parser.parse_args()

    route = load_route(args.route)
    route_name = route.get("route", "Unknown")
    operator = route.get("operator", "Unknown")
    duration_hours = route.get("duration_hours", 4.0)
    stops = route.get("stops", [])

    print(f"\n{'='*60}")
    print(f"  TRAIN JOURNEYS — {operator}")
    print(f"  {route_name}")
    print(f"  {len(stops)} stops")
    print(f"{'='*60}\n")

    route_dir = Path(args.route).parent
    out_dir = route_dir / "output"
    out_dir.mkdir(exist_ok=True)

    total_sec = int(duration_hours * 3600) if not args.preview else 600

    print(f"Duration: {total_sec/3600:.1f} hours")
    print()

    print("[1/6] Generating ambient...")
    ambient_path = out_dir / "ambient.wav"
    generate_ambient(total_sec, ambient_path)

    print("[2/6] Generating rhythm track...")
    rhythm_path = out_dir / "rhythm.wav"
    generate_rhythm_track(total_sec, rhythm_path, out_dir, bpm=60)

    print("[3/6] Generating announcements...")
    ann_dir = out_dir / "announcements"
    ann_dir.mkdir(exist_ok=True)
    script_path = Path(args.route).parent / "script.json"
    if script_path.exists():
        with open(script_path) as f:
            script = json.load(f)
        announcements = script["announcements"]
    else:
        announcements = []
        for i, stop in enumerate(stops):
            t = int((i + 1) * total_sec / (len(stops) + 1))
            announcements.append({
                "time": f"{t//60}:{t%60:02d}",
                "text": f"This train is calling at {stop}.",
                "station": stop
            })

    if args.preview:
        announcements = [a for a in announcements if parse_time(a["time"]) <= total_sec]

    ann_files = generate_announcements(announcements, ann_dir)

    print("[4/6] Building timeline...")
    timeline = build_timeline(announcements, total_sec)
    narration_path = out_dir / "narration.wav"
    concatenate_segments(timeline, narration_path, out_dir)

    print("[5/6] Mixing audio...")
    mixed_path = out_dir / "mixed.wav"
    mix_audio(ambient_path, rhythm_path, narration_path, mixed_path)

    print("[6/6] Building video...")
    image_path = ENGINE.parent / "assets" / "train_carriage.png"
    if not image_path.exists():
        image_path = ENGINE.parent / "assets" / "train_window.png"
    if not image_path.exists():
        image_path = ENGINE.parent / "longhaul/assets/ba_window.jpg"

    video_path = out_dir / f"{route.get('id', 'train')}.mp4"

    if image_path.exists():
        build_video(image_path, mixed_path, video_path)
    else:
        cmd = ["ffmpeg", "-y", "-i", str(mixed_path), "-c:a", "aac", str(video_path)]
        subprocess.run(cmd, capture_output=True, check=True)
        print(f"  ✓ Audio-only video: {video_path.name}")

    print(f"\n{'='*60}")
    print(f"  DONE: {video_path}")
    print(f"  Duration: {total_sec/3600:.1f} hours")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
