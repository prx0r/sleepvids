# Timetable Video Production Process

## The concept
Real train announcements + train ambiance = the whole video. The voice IS the departure board. Per country, per operator, accurate local style.

NOT reading timetables. MAKING announcements. The difference:
- ❌ "The 14:35 departure calls at Stevenage, Peterborough, Doncaster..."
- ✅ "The next train to arrive at platform 2 is the 14:35 LNER Azuma service to Edinburgh Waverley"

## How to make a train announcement sleep video

### 1. Pick the route
- UK: nationalrail.co.uk timetables (PDF, CC-BY-2.0)
- Japan: JR timetable PDFs (check license)
- Germany: Deutsche Bahn (data.deutschebahn.com, free)
- France: SNCF (check license)

### 2. Get the ambiance
- freesound.org: "train interior rain window" (CC0)
- freesound.org: "train station announcement echo" (CC0)
- freesound.org: "wheel rhythm" (CC0)
- Layer at 20-30% under announcements

### 3. Write announcements (not timetable reading)
Each departure becomes a realistic announcement:

UK style:
"The next train to arrive at platform 2 is the 14:35 LNER Azuma service to Edinburgh Waverley, calling at Stevenage, Peterborough, Doncaster, York, and Newcastle. This service is expected to arrive at Edinburgh Waverley at 19:00. Platform 2 for the 14:35 LNER Azuma service to Edinburgh Waverley."

Japan style:
"Mamonaku, ichiban-sen ni, Tokyo yuki Tokkaido Shinkansen, Nozomi 21, ga mairimasu. Doa ga shimarimasu. Gochuui kudasai." (Translation: "Shortly, the Tokkaido Shinkansen Nozomi 21 bound for Tokyo will arrive at platform 1. The doors are closing. Please take care.")

### 4. Generate TTS
- UK: V10 Companion (warm, polite) or a custom train-announcement voice
- Japan: V05 Healer (gentle, melodic) — or a custom voice with Japanese phrases
- Germany: V03 Lecturer (precise, efficient)
- France: V02 Storyteller (elegant, measured)
- Pace: normal announcement pace (don't slow down — the announcements ARE the content)

### 5. Compile
- Concatenate all announcements for the route
- Layer train ambiance underneath
- Add intro: "Good afternoon. Welcome to LNER services from London Kings Cross."
- Add closing: "That concludes today's services. Sleep well."

## Scaling
- Each route = 1 video
- ~40 UK routes + international routes
- One route can generate 8+ hours (all departures through the day)
- Update quarterly when timetables change

## Time to produce
- Route research: 10 minutes
- Announcement writing: 20 minutes
- TTS generation: 15 minutes
- Ambiance sourcing: 5 minutes
- Compilation: 10 minutes
- Total: ~60 minutes per video

## Why this works for sleep
- Repetitive patterns (same announcement structure)
- Predictable rhythm (departure, calling points, arrival)
- Ambient train sounds (wheel rhythm, rain)
- No surprises, no tension
- The voice is authoritative but soothing
- It's a lullaby disguised as a departure board

## The voice clone approach
Clone ONE voice per country/style with Qwen TTS. Then the content is infinitely scalable — just plug in timetable data.

### Voice clones needed
| Style | Voice | Sample | Use for |
|-------|-------|--------|---------|
| UK train | V10 Companion (warm, polite) | Record 5-10 sample announcements | LNER, GWR, Avanti, ScotRail |
| Japan train | Custom (melodic, formal) | Record Japanese announcement samples | JR, Tokyo Metro, Keihan |
| Germany train | V03 Lecturer (precise, efficient) | Record German announcement samples | DB ICE, DB Regio |
| France train | V02 Storyteller (elegant) | Record French announcement samples | SNCF TGV, TER |
| UK bus | V10 Companion (casual) | Record bus announcement samples | Local bus networks |
| Captain | V01 Sage (authoritative, calm) | Record captain announcement samples | Airlines |

### Template announcements per country
Each country gets a set of template phrases that are filled with data:
- "The [TIME] [SERVICE] to [DESTINATION] departing from platform [X]"
- "Calling at [STATION1], [STATION2], [STATION3]..."
- "Expected arrival [TIME]. Journey time [DURATION]"
- "We are sorry to announce a delay of approximately [MINUTES] minutes"
- "Please mind the gap between the train and the platform"

### Visuals: stock footage synced to announcements
- Source: Pexels, Pixabay (CC0), or self-shot footage
- Sync: train leaving station matches departure announcement
- Format: wide shot of train exterior → interior shot → window view
- Each announcement gets a visual beat
- Slow, steady cuts — no rapid editing

### Content math
- 1 voice clone = all routes in that country
- 30 departures per route × 30 seconds = 15 minutes of unique announcements
- Repeat with different routes = 8+ hours
- One voice clone + timetable data = infinite content
