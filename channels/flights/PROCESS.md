# Flight Announcement Video Production

## The concept
Airline announcements + cabin ambiance = the whole video. Captain speaking, boarding calls, safety briefings, altitude updates, landing announcements. The captain's voice is the logo.

## The captain voice
Clone ONE captain voice per airline style with Qwen TTS. Record sample announcements:
- "Good evening, ladies and gentlemen, this is your captain speaking"
- "We are currently cruising at an altitude of thirty-five thousand feet"
- "We expect to arrive at approximately local time"
- "Cabin crew, please prepare for landing"

The captain's voice is warm, authoritative, reassuring. The voice that says "everything is fine, you can sleep now."

## Announcement templates

### Boarding
"Ladies and gentlemen, British Airways flight BA115 to New York JFK is now boarding at Gate B32. We would like to invite our priority passengers to board at this time."

### Safety briefing
"Ladies and gentlemen, welcome aboard British Airways flight BA115 to New York JFK. Your seatbelt should be worn whenever the seatbelt sign is illuminated. To fasten your seatbelt, insert the metal end into the buckle until you hear a click. To release, lift the top of the buckle."

### Captain's announcement
"Good evening, ladies and gentlemen. This is your captain speaking. We are currently cruising at an altitude of thirty-five thousand feet. The flight time to New York JFK is approximately seven hours and forty-five minutes. We expect to arrive at JFK at approximately 11:45 PM local time. The weather in New York is clear with a temperature of twelve degrees Celsius. Cabin crew, please prepare for arrival."

### Turbulence
"Ladies and gentlemen, we may experience some light turbulence in the next few minutes. I've turned on the fasten seatbelt sign. Please return to your seats and ensure your seatbelt is securely fastened."

### Descent
"Ladies and gentlemen, we are now beginning our descent into Tokyo Narita. Please ensure your seatbelt is securely fastened and your seat is in the upright position. We expect to land at approximately 6:30 PM local time."

### Landing
"Ladies and gentlemen, welcome to Tokyo Narita. The local time is 6:28 PM. Please remain seated with your seatbelt fastened until the aircraft has come to a complete stop and the seatbelt sign has been turned off. On behalf of Japan Airlines and your captain, thank you for flying with us."

## Visuals: the flight map
The in-flight entertainment map. The one that shows your plane crossing the ocean. That's the visual. It's already calming. It's already hypnotic. Everyone has stared at it on a long flight.

- Source: screen recordings of flight tracker maps (FlightAware, Flightradar24)
- Or: recreate the map animation (simple CSS: moving plane icon across route)
- The map shows: current position, route line, altitude, speed, time remaining, destination
- It moves slowly across the screen — perfect for sleep
- Each announcement syncs with map updates: "We are now crossing the Atlantic" matches the plane icon over the ocean

### Why this works
- Everyone has stared at a flight map at 3am, exhausted, drifting off
- The map is simple, repetitive, soothing
- It moves at a predictable pace — no surprises
- Combined with captain's voice + cabin hum = hypnotic
- Can run for 12+ hours (long-haul routes)

## Audio layers
- Layer 1: Cabin ambiance (engine hum, white noise)
- Layer 2: Occasional seatbelt chime
- Layer 3: Announcement voice (captain or cabin crew)
- Keep announcements at natural pace — don't slow down

## Scaling
- One captain voice clone = all routes for that airline
- Different routes = different destinations, different flight times
- 20 major airlines × 10 routes each = 200 videos
- Each video 60-120 minutes
