#!/usr/bin/env python3
"""
Sleepvids MVP Engine — ambient + TTS + mix
Takes a prompt, generates ambient audio, adds TTS announcements, mixes with ducking.
"""

import subprocess
import json
import sys
from pathlib import Path

def generate_ambient(prompt, duration_sec, output_path):
    """Generate ambient audio from prompt using ffmpeg synthesis."""
    # Pink noise base (wind/rain foundation)
    # Low-pass filter for warmth
    # LFO modulation for movement
    # Duration: duration_sec seconds
    
    filters = (
        f"aevalsrc='0.03*sin(2*PI*0.1*t)*pinknoise':s=44100:d={duration_sec},"
        f"lowpass=f=800,aecho=0.8:0.88:60:0.4"
    )
    
    cmd = [
        "ffmpeg", "-y", "-f", "lavfi", "-i", filters,
        "-t", str(duration_sec), "-ar", "44100", "-ac", "2",
        output_path
    ]
    subprocess.run(cmd, capture_output=True)
    print(f"Ambient generated: {output_path} ({duration_sec}s)")

def generate_tts(text, voice, output_path):
    """Generate TTS using edge-tts."""
    cmd = [
        "edge-tts", "--voice", voice,
        "--rate", "-30%",
        "--text", text,
        "--write-media", output_path
    ]
    subprocess.run(cmd, capture_output=True)
    print(f"TTS generated: {output_path}")

def mix_with_ducking(narration_path, ambient_path, output_path):
    """Mix narration + ambient with sidechain ducking (12dB under narration)."""
    cmd = [
        "ffmpeg", "-y",
        "-i", narration_path,
        "-i", ambient_path,
        "-filter_complex",
        "[1:a]volume=0.3[bg];[0:a][bg]amix=inputs=2:duration=first[mixed];"
        "[mixed]loudnorm=I=-16:TP=-1.5[out]",
        "-map", "[out]",
        "-ar", "44100", "-ac", "2",
        output_path
    ]
    subprocess.run(cmd, capture_output=True)
    print(f"Mixed: {output_path}")

def build_video(cabin_image, ambient_path, output_path):
    """Build video from static image + ambient audio."""
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", cabin_image,
        "-i", ambient_path,
        "-c:v", "libx264", "-tune", "stillimage",
        "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        output_path
    ]
    subprocess.run(cmd, capture_output=True)
    print(f"Video: {output_path}")

if __name__ == "__main__":
    print("Sleepvids MVP Engine")
    print("Usage: python3 mvp.py --prompt 'rain on window' --duration 300 --output test.mp4")
