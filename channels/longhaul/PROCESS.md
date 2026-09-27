# Long Haul — Flight Announcement Video Production

## The concept
Real long-haul flights. Real flight numbers. Real routes. Captain announcements, cabin ambiance, flight map. Economy to first class. The sky at 3am.

Each video is a specific flight on a specific airline. The viewer is on the plane. The captain speaks. The map moves. The engine hums. You fall asleep somewhere over the Atlantic.

## The channel: Long Haul
- **Name**: Long Haul
- **Concept**: Real flights, real data, real airline style
- **Differentiation**: Not generic "flight sounds" — specific flights, specific airlines, specific cabin classes
- **SEO**: "long haul flight sleep", "British Airways flight for sleep", "business class sleep"

## Flight numbers are real
We use actual flight data from OpenFlights (free CSV) or Flightradar24 API. Each video corresponds to a real route:
- BA117: London Heathrow to New York JFK
- BA287: London Heathrow to Los Angeles
- FR1234: London Stansted to Dublin
- JL402: Tokyo Narita to New York JFK

The flight map shows the actual route. The announcements match the actual airline. The cabin class matches the actual aircraft.

## Per-airline production

### British Airways (flagship)
- **Routes**: LHR-JFK, LHR-LAX, LHR-HKG, LHR-SIN, LHR-SYD, LHR-NRT
- **Cabin classes**: First, Club World, World Traveller Plus, World Traveller
- **Voice**: Warm, British, professional. Clone from BA announcements.
- **Visual**: Navy seats, large IFE screens, warm lighting
- **Ambiance**: Quieter cabin, occasional service sounds
- **Duration**: 7-14 hours (long-haul)

### Ryanair (budget contrast)
- **Routes**: STN-DUB, STN-BCN, DUB-LHR, short-haul Europe
- **Cabin classes**: Economy only
- **Voice**: Direct, efficient, Irish. Clone from Ryanair announcements.
- **Visual**: Blue/yellow seats, tight pitch, small screens
- **Ambiance**: Engine louder (smaller plane), more announcements
- **Duration**: 2-4 hours (short-haul)

### Japan Airlines (premium)
- **Routes**: NRT-JFK, NRT-LHR, NRT-SIN, HNL-NRT
- **Cabin classes**: First, J Class, Premium Economy, Economy
- **Voice**: Formal Japanese with English announcements
- **Visual**: Grey seats, meticulous service, departure melodies
- **Announcements**: Poetic, precise timing
- **Duration**: 8-14 hours (long-haul)

### Emirates (luxury)
- **Routes**: DXB-JFK, DXB-LHR, DXB-SIN, DXB-SYD
- **Cabin classes**: First, Business, Premium Economy, Economy
- **Voice**: Warm, multilingual, Gulf accent
- **Visual**: Gold/cream interiors, entertainment system
- **Duration**: 8-16 hours (ultra-long-haul)

## Cabin class differentiation

### Economy
- Standard engine hum
- Occasional announcements
- Small seat-back screen
- The long night flight

### Business
- Quieter cabin
- Champagne service sounds
- Larger personal screen
- Full recline

### First
- Near silence
- Private suite
- Personal minibar sounds
- The captain whispers

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
