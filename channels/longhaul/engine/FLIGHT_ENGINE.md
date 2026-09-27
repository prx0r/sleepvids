# Flight Engine — Reusable Template

## What is the flight engine?
A reusable production pipeline that takes flight data and produces a sleep video. The engine has fixed parts (template announcements, visual structure, audio layers) and variable parts (specific route, airline, cabin class).

## The fixed parts (same for every video)
1. **Visual structure**: cabin photo + flight map overlay + subtle animation
2. **Audio structure**: cabin ambiance + captain announcements at intervals
3. **Announcement templates**: same phrases, different data filled in
4. **Flight map**: same animation engine, different routes

## The variable parts (different per video)
1. **Airline**: BA, Ryanair, JAL, Emirates (changes voice, visual, style)
2. **Route**: LHR-JFK, NRT-SIN, etc. (changes map, announcements, timing)
3. **Cabin class**: Economy, Business, First (changes visual, audio, vibe)
4. **Aircraft**: 777, 787, A350, A380 (changes seat configuration)

## The production pipeline (per video)

```
INPUT                          PROCESS                     OUTPUT
─────                          ───────                     ──────
Flight number                  → Route data extraction      → Route JSON
  (e.g. BA117)                   (OpenFlights CSV)

Airline + cabin class          → Cabin image selection       → cabin.jpg
  (e.g. BA Business)              or Cloudflare Flux generation

Route + airline                → Captain announcement writing → announcements.json
  (e.g. LHR-JFK BA)               (template + real data)

Route data + announcements     → TTS generation              → audio/*.mp3
  (cloned captain voice)

Route data                     → Flight map generation       → flightmap.html
  (lat/lon for airports)          (CSS/JS animation)

Cabin image + flight map       → Video composition           → out.mp4
  + audio layers                  (FFmpeg)
```

## The announcement templates

### Generic (all airlines)
```
BOARDING: "Flight [NUMBER] to [DESTINATION] is now boarding at Gate [GATE]"
SAFETY: "Your seatbelt should be worn whenever the seatbelt sign is illuminated"
TURBULENCE: "We may experience some light turbulence in the next few minutes"
LANDING: "Welcome to [DESTINATION]. Local time is [TIME]"
```

### British Airways specific
```
CAPTAIN: "Good evening, ladies and gentlemen, this is your captain speaking. 
         Welcome aboard British Airways flight [NUMBER] to [DESTINATION]. 
         We're currently cruising at an altitude of [ALTITUDE] feet. 
         The estimated flight time is [TIME]. 
         We expect to arrive at [DESTINATION] at approximately [TIME] local. 
         The weather [DESTINATION] is [WEATHER]. 
         Cabin crew, please prepare for landing."
```

### Ryanair specific
```
CAPTAIN: "Attention passengers, this is your first officer. 
         We're currently at thirty-seven thousand feet. 
         Flight time to [DESTINATION] is [TIME]. 
         We expect to land at [TIME]. 
         Crew, prepare for descent."
```

## The visual layers
```
Layer 1: cabin_[airline]_[class].jpg    (static background)
Layer 2: flightmap_[route].html         (animated map on screen)
Layer 3: grain_overlay.png              (subtle texture)
```

## The audio layers
```
Layer 1: cabin_ambiance_[airline].mp3   (engine hum, white noise)
Layer 2: seatbelt_chime.mp3             (occasional, synced with map)
Layer 3: captain_announcements.mp3      (at natural intervals)
```

## How to produce a new video
1. Choose airline + route + cabin class
2. Fill in templates with real data
3. Generate cabin image (Flux or select from library)
4. Generate flight map (route data → animation)
5. Generate announcements (templates + TTS)
6. Source ambiance (freesound.org or existing)
7. Compile with FFmpeg

## Time per video: ~60 minutes
- Template fill: 5 min
- Image generation: 5 min
- Flight map: 10 min
- Announcement writing: 10 min
- TTS generation: 10 min
- Ambiance sourcing: 5 min
- Compilation: 10 min
- QA: 5 min
