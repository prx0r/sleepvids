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

## The visual: the lofi model

Static cabin photo + animated flight map on seat-back screen = the whole video. Same as lofi girl studying, but you're on a plane.

### The layers
```
Layer 1 (bottom): Cabin background photo
Layer 2 (middle): Seat-back screen with flight map animation
Layer 3 (top): Subtle grain/overlay for texture
Layer 4 (audio): Cabin ambiance (engine hum)
Layer 5 (audio): Captain announcements at intervals
```

### Step 1: Get a cabin photo
- Pexels CC0: "airplane cabin interior" (30,000+ photos)
- Pixabay: "cabin interior" (10,000+ photos)
- Wikimedia Commons: Ryanair cabin, BA cabin, etc.
- Crop to show: seat back in front of you, with screen area visible
- The screen area is where the flight map goes

### Step 2: Create the flight map overlay
- The flight map sits on top of the seat-back screen area
- It's a small rectangle showing: route line, plane icon, altitude, time remaining
- The plane icon moves slowly along the route
- Data from OpenFlights (free CSV): airport lat/lon for every airport
- Animation: CSS/JS moving plane icon along great circle route

### Step 3: Add subtle animation
- The flight map moves (plane icon along route)
- Optional: slight camera shake (simulates turbulence)
- Optional: window light changes (day/night cycle)
- Keep it minimal — the movement should be hypnotic, not distracting

### Step 4: Layer the audio
- Cabin ambiance: engine hum, white noise, occasional creaks
- Captain announcements: at natural intervals (takeoff, cruise, turbulence, descent, landing)
- The announcements are the "event" — everything else is ambient

### Why this works
- Everyone has stared at a flight map at 3am, exhausted, drifting off
- The map is simple, repetitive, soothing
- It moves at a predictable pace — no surprises
- Combined with captain's voice + cabin hum = hypnotic
- Can run for 12+ hours (long-haul routes)

### Per-airline differentiation
| Airline | Cabin photo | Seat style | Screen type | Announcement style |
|---------|-------------|------------|-------------|-------------------|
| Ryanair | Blue/yellow seats, tight pitch | Fixed recline, no pockets | Small screen | Direct, efficient |
| British Airways | Navy seats, wider pitch | Reclining, IFE screens | Large screen | Warm, professional |
| Japan Airlines | Grey seats, compact | Reclining, personal screens | HD screen | Polite, melodic |
| Lufthansa | Grey/blue seats | Reclining, IFE | Standard screen | Precise, German |

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
