# Timetable Video Production Process

## How to make a timetable sleep video

### 1. Get the data
- Go to nationalrail.co.uk/travel-information/timetables
- Search for the route (e.g., "London Kings Cross to Edinburgh")
- Download the PDF timetable
- OR use the National Rail API (free registration)
- OR scrape from data.gov.uk (CC-BY-2.0)

### 2. Extract departures
From the PDF or API, extract for each departure:
- Departure time
- Service name (e.g., "06:00 LNER Azuma")
- Calling points (intermediate stations with times)
- Arrival time at destination
- Journey time
- Platform number (if available)

### 3. Format for narration
Each departure becomes a spoken paragraph:
"The 06:00 LNER Azuma service to Edinburgh Waverley. Calling at: Stevenage at 06:20, platform 2. Peterborough at 06:52, platform 3. Doncaster at 07:41, platform 4. York at 08:05, platform 3. Newcastle at 08:42, platform 2. Durham at 08:56, platform 1. Edinburgh Waverley at 10:20. Journey time: four hours twenty minutes."

### 4. Generate TTS
- Voice: V10 Companion (warm, casual) or V03 Lecturer (clear, precise)
- Pace: -30% (105 WPM)
- Each departure gets 10-15 seconds of narration
- 30 departures × 12 seconds = 6 minutes of narration per route
- For 8-hour video: repeat route through the day + add connecting services

### 5. Add ambient (optional)
- Train sounds: wheel rhythm, rain on window, distant whistle
- Keep at 20-30% volume under narration
- Source from freesound.org (CC0/CC-BY)

### 6. Visual
- Option A: Black screen (simplest)
- Option B: Departure board text scrolling slowly (white text on black)
- Option C: Static image of the route map

### 7. Compile
- Concatenate all departure narrations
- Add intro and closing
- Layer ambient audio
- Export as MP4

## Scaling strategy
- Each major UK route = 1 video
- ~40 major routes = 40 videos
- Each route can be updated when timetable changes (quarterly)
- International routes (JR, DB, SNCF) expand the catalog
- Connecting services and variations add more content per route

## SEO
- Title: "{Route} Timetable — {Operator} Train Departures for Sleep | {Duration}"
- Tags: timetable, train, sleep, {route}, {operator}, departure board, ASMR
- Description: list all departure times, add timestamps

## Time to produce
- Data extraction: 15 minutes
- TTS generation: 10 minutes
- Ambient sourcing: 5 minutes
- Compilation: 5 minutes
- Total: ~35 minutes per video

## Content math
- 30 departures per route × 12 seconds = 6 minutes of unique narration
- For 8-hour video: repeat route through day + add morning/evening variations
- Or: combine 8-10 routes into one long video
- One route can generate 8+ hours of content easily
