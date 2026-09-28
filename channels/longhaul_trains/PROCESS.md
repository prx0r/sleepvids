# Train Channel — Build Plan

## Channel Overview

**Long Haul Trains** — the immersive, cozy, rhythmic sibling to Long Haul Flights.

| Attribute | Value |
|-----------|-------|
| Brand | Long Haul Trains |
| Shelf | PLACE (like flights) |
| Core Engine | E4 (ambience — rhythmic track, scenery, no narration) |
| Workhorse Engine | E5a/E5b (train essays, deep dives) |
| Reading Engine | E2 (railway stories, ghost trains, historical accounts) |
| Vibe | Rhythmic, hypnotic, endless landscape, cabin warmth, journey as ritual |

## Engines for Trains

### E4 — Ambience (Effort 1)
Pure train sounds. The rhythmic clatter of wheels on track. The sway of the carriage. Rain on windows. The tunnel rush. No narration. Just the train.

- Audio: layered rhythmic track + ambient beds (rain, wind, tunnel)
- Visual: slow scenery loop, window view, cabin interior
- Duration: 2-8 hours per video
- Sources: freesound.org field recordings, synthesized rhythms

### E5a/E5b — Essays & Deep Dives (Effort 5/3)
Research essays about railways, train culture, historical moments, engineering. Same format as flight essays but train-themed.

### E2 — Reading (Effort 3)
PD railway stories. Ghost train tales. Historical accounts of famous journeys. Read slowly with ambient train bed.

## First Videos (MVP)

| # | Title | Engine | Duration | Effort |
|---|-------|--------|----------|--------|
| 1 | Night Train Through the Mountains — 8 Hours | E4 | 8h | 1 |
| 2 | Trans-Siberian Railway — The Longest Journey on Earth | E5b | 90 min | 3 |
| 3 | Orient Express — Murder, Mystery, and Golden Age | E5b | 90 min | 3 |
| 4 | The British Rail Enigma — Why Can't We Run Trains on Time? | E5a | 60 min | 5 |
| 5 | Ghost Trains — Stories of the Ones That Shouldn't Exist | E2 | 45 min | 3 |

## Folder Structure (per video)

```
channels/longhaul_trains/
├── channel.json               # channel definition, SEO, engines
├── videos/
│   └── NNN_title/
│       ├── meta.json          # video metadata (engine, duration, style, word targets)
│       ├── SCAFFOLD.md        # narrative arc, structure, key facts
│       ├── RESEARCH.md        # sources, quotes, data points
│       ├── STORYBOARD.md      # scene-by-scene breakdown
│       ├── sections/          # individual script sections
│       │   ├── section_01.md
│       │   └── ...
│       └── DRAFT.md           # compiled final script
└── PROCESS.md                 # how to make train videos (repeatable)
```

## Repeatable Process (PROCESS.md)

### Step 1 — Pick the journey/topic
- Choose a specific route, train, or phenomenon
- Verify it's interesting enough for 2-8 hours (E4) or 30-120 min (E5)
- Check for existing content (avoid duplication)

### Step 2 — Build the sound bed (E4 only)
- Layer 3-5 rhythmic elements: track joints, wheel rhythm, carriage sway
- Add ambient layers: rain, wind, tunnel roar
- Ensure seamless looping (crossfade 30 seconds)

### Step 3 — Research
- Gather 5-10 sources: books, articles, documentaries, first-hand accounts
- Extract key facts, quotes, sensory details
- For E4: collect field recordings, verify rhythm authenticity

### Step 4 — Scaffold
- Map the narrative arc (for E5/E2)
- Define section structure and word counts
- For E4: define the emotional arc of the journey

### Step 5 — Script
- Write each section to word target
- Use sensory language (sound, motion, light)
- For E5: use the same essay format as flights
- For E2: use slow-reading format with train bed

### Step 6 — Produce
- E4: produce audio bed, encode video with looped visual
- E5: TTS narration + ambient bed + visual
- E2: TTS reading + train bed + minimal visual

### Step 7 — Ship
- Upload to YouTube with proper SEO
- Add chapters/timestamps
- Cross-link in Long Haul Trains playlist

## Sound & Research

Full sound sourcing plan: [SOUND_PLAN.md](SOUND_PLAN.md)

Key points:
- Source field recordings from Freesound (CC0/CC-BY)
- Layer rhythmic elements (wheel joints, wind, hums)
- Stack ambient beds
- Pull excerpts from PD travelogues and histories
- All claims sourced; receipts before recording
- See sleepsearch repos for full source registry

## Key Differences from Flights

| Aspect | Flights | Trains |
|--------|---------|--------|
| Rhythm | Engine hum (continuous) | Wheel clatter (rhythmic, hypnotic) |
| Visual | Clouds, sky, wing | Landscape, tunnels, stations, tracks |
| Feeling | Floating, weightless | Rolling, swaying, connected to earth |
| History | 100+ years | 200+ years (since 1804) |
| Iconic routes | London-NY, Sydney-Singapore | Trans-Siberian, Orient Express, Ghan |
| Fears | Turbulence, heights | Derailment, claustrophobia |
| Comfort | Seats, cocktails | Bunks, dining cars, observation decks |

## SEO Keywords
- "train sounds for sleep"
- "night train ambient"
- "train journey for sleeping"
- "railway history explained slowly"
- "8 hours train ride"
- "train cabin ambience"

---

This process will be updated as we produce more train videos and learn what works.
