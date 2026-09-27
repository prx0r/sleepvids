# Flight Announcement Video Production

## The concept
Airline announcements + cabin ambiance + flight map = the whole video. The visual is a POV from an airplane seat — the back of the seat in front of you, with the flight map playing on the seat-back screen. The captain makes announcements. The engine hums. You're on a flight.

## Free/open sources available

### Captain voice
- **itch.io** — "Airplane Pilot Voice Pack" by Andrew Helbig: 1,000+ professionally recorded pilot clips. WAV + MP3. Free sample available. Use as reference for cloning.
- **Freesound.org** — "In-flight sounds" pack by bigfriendlyjiant: real captain announcements, cabin crew, takeoff, landing. CC licensed.

### Flight map
- **FlightAirMap** (GitHub, 609 stars, AGPL-3.0) — open source 2D/3D flight tracker
- **OpenLayers flight animation** — animated plane on map, ready to use
- **OpenFlights** — free airport, airline, route data (CSV)

### Flight data
- **Flightradar24 API** — real-time + historical flight data (paid, but has free tier)
- **Aviation Weather Center API** — turbulence, METAR, PIREPs (free, public)
- **OAG Historical Flights** — 20+ years of flight data (paid)

### Turbulence data
- **NASA ASRS Wake Turbulence Encounters** — public data
- **Aviation Weather Center** — turbulence forecasts (free)
- **PIREPs** — pilot reports of turbulence (free via Aviation Weather API)

### Cabin ambiance
- **Freesound.org** — cabin noise, seatbelt chimes, engine hum (CC0/CC-BY)

## The visual: POV seat-back screen

The video is a first-person view from an airplane seat. In front of you is the back of a seat. Embedded in that seat is a small screen. On that screen, the flight map is playing — a plane icon moving slowly across a map, showing the route, altitude, time remaining.

### How to create it
1. **Static background**: Image of airplane seat-back (from Pexels/Pixabay CC0, or generate)
2. **Flight map overlay**: Animated plane icon moving along route on the screen
3. **Route data**: From OpenFlights (free) — get lat/lon for departure and arrival airports
4. **Animation**: CSS/JS animation moving plane icon along great circle route
5. **Sync**: Flight map updates with captain announcements

### Why this works
- Everyone has stared at a flight map at 3am, exhausted, drifting off
- The map is simple, repetitive, soothing
- It moves at a predictable pace — no surprises
- Combined with captain's voice + cabin hum = hypnotic
- Can run for 12+ hours (long-haul routes)

## Captain voice clone approach
Clone ONE captain voice from the itch.io voice pack samples. Record additional phrases as needed. The clone produces all announcements for all routes.

### Template announcements
- Boarding: "Ladies and gentlemen, {airline} flight {number} to {destination} is now boarding at Gate {gate}"
- Safety: "Your seatbelt should be worn whenever the seatbelt sign is illuminated"
- Captain: "Good evening, this is your captain speaking. We are currently cruising at {altitude}"
- Turbulence: "We may experience some light turbulence in the next few minutes"
- Descent: "We are now beginning our descent into {destination}"
- Landing: "Welcome to {destination}. Local time is {time}"

## Production per video
1. Get route data from OpenFlights (free): departure, arrival, distance, typical flight time
2. Get turbulence forecast from Aviation Weather Center (free)
3. Write template announcements with real data
4. Generate TTS with cloned captain voice
5. Create flight map animation (CSS/JS or screen recording)
6. Source cabin ambiance from freesound.org
7. Compile: seat-back background + flight map + announcements + ambiance

## Time to produce
- Route data: 5 minutes
- Turbulence data: 5 minutes
- Announcement writing: 15 minutes
- TTS generation: 10 minutes
- Flight map creation: 20 minutes
- Compilation: 10 minutes
- Total: ~65 minutes per video

## Scaling
- One captain voice clone = all routes
- 100 major long-haul routes = 100 videos
- Each video 8-12 hours (long-haul)
- Update when flight schedules change (seasonal)
