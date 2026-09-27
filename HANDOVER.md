# HANDOVER — Sleepvids Session 2026-09-27

## Status: IN PROGRESS
## Last updated: 2026-09-27

---

## What we built today

### Etymology channel (2 videos)

**001_vegetable** — 9,991 words, 95 minutes
- Full research pack (Etymonline, Wiktionary, Knuth, Gagliano, Mancuso, etc.)
- 6-section essay with passage maxing
- NoSlop-clean (0.71 confidence)
- Key rabbit holes: Vegetable Lamb of Tartary, tomato fear, Bonnefons, competing terms
- Folder: `channels/etymology/videos/001_vegetable/`

**002_algorithm** — 7,793 words, 74 minutes
- Full research pack (al-Khwarizmi, Knuth, NPR, OpenLayers, etc.)
- 9-section essay with passage maxing
- NoSlop-clean (0.72 confidence)
- Key rabbit holes: algorithms in nature, competing terms, Conway's Game of Life, TikTok study
- Folder: `channels/etymology/videos/002_algorithm/`

### Timetables channel (template)
- Zero-effort content: read public timetable data
- UK rail (CC-BY-2.0), Deutsche Bahn, JR Japan
- 35 minutes per video
- Folder: `channels/timetables/`

### Long Haul channel (engine built, first video templated)
- Flight engine: reusable pipeline (fixed + variable parts)
- BA117 LHR-JFK business class: route.json + script.json
- 7 announcements timed across 8-hour flight
- Cabin image generated with Cloudflare Flux
- Flight map HTML preview built
- Voice clone: pending
- Folder: `channels/longhaul/`

### Interesting Tribes channel (definition only)
- Channel definition in `channels/interesting_tribes/channel.json`

### Process docs
- `channels/etymology/process/process.md` — full pipeline for etymology videos
- `process/session_log_2026_09_27.md` — session learnings

---

## Key decisions made

1. **Passage maxing** — don't write about sources, READ them. Quote directly, unpack clause by clause.

2. **Write clean from the start** — apply NoSlop rules while writing. 10x faster than fixing after.

3. **Sections, not monoliths** — each section is an independent file. Edit section by section.

4. **Rabbit holes, not padding** — follow threads, don't add filler.

5. **Timetables are lowest effort** — zero scripting, public data, 35 min/video.

6. **Flights are premium** — real flight numbers, airline style, cabin class.

7. **Voice clones are the asset** — clone once per country/style, infinite content.

---

## What needs to happen next

### Immediate (finish BA117)
1. Clone BA captain voice with Qwen TTS
2. Source cabin ambiance from freesound.org
3. Assemble test video (10-min chunk)
4. Preview → adjust → full render

### Near-term (scale)
1. BA economy video
2. First Ryanair video
3. First timetable video
4. JAL + Emirates templates

---

## Resources

### Cloudflare R2
- See .env for credentials

### GitHub
- Remote: https://github.com/prx0r/sleepvids
- Token: see .env

### NoSlop
- `/root/noslop/miner/src/detector.py`
- Added: CHOPPY, SIGNPOST

### Free sources
- OpenFlights, Aviation Weather API, Freesound, Pexels, Pixabay
