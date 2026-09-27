# SESSION LOG — 2026-09-27
## What we did, how we did it, what we learned

---

## Stream of thought

**Starting point:** User wanted to explore the sleepvids repo and figure out how to make etymology videos. We picked 5 words: vegetable, silly, nice, panic, algorithm.

**First mistake:** Over-JSON'd everything. Created a polished deep_etymology template with 6 sections and a full vegetable script in JSON format. The JSON was a cage — too structured, too rigid, no room for the story to breathe.

**User correction:** "Don't rewrite — just get interesting data and threads." The research should be a hoard, not a document. The script should be a weaving, not a template.

**Shift in approach:** Created a raw RESEARCH.md (full passages, not summaries) and a STORYBOARD (scene-by-scene with time/word targets). The research became the source material. The storyboard became the map.

**Second problem:** Wrote a first draft that hit ~6,300 words. Too short for 2 hours (needs ~12,600 at 105 WPM). But the user said: "Don't add words for the sake of it. Add threads worth following."

**Key insight:** Padding ≠ expansion. Expansion means finding a new thread — a person to meet, a place to visit, a passage to read, a surprising connection. Padding means adding words that don't earn their place.

**Process that worked:**
1. Hoard everything (RESEARCH.md)
2. Map the journey (SCAFFOLD.md)
3. Scene by scene (STORYBOARD.md)
4. Write draft section by section
5. Review → find threads → expand → review again
6. Each thread must earn its place (surprising, connects back, reveals something about the word)

**Final draft:** 9,991 words — 95 minutes. Close enough to 2 hours. Every section has real threads, not filler.

---

## What made the output good

### 1. Hoarding before writing
Reading Etymonline entries for 15+ related words, pulling Aristotle passages from MIT OCW, finding the Adams & Fins 2016 paper tracing "vegetative" from Aristotle to Jennett — all before writing a single word of script. The research IS the script. You just have to arrange it.

### 2. Finding loops, not just timelines
The linear timeline (PIE → Latin → English → modern) is the spine. But the loops are what make it interesting:
- vegetable once meant "alive" → now means "not alive" (same word, opposite meaning)
- Aristotle's classification → named the worst medical condition 2,300 years later
- The root family kept their power (vigour, wake, watch) while vegetable lost it
- Science proved Aristotle wrong with his own word

### 3. Threads that earn their place
Each expansion had to pass a test: Is this surprising? Does it connect back? Does it reveal something about how humans think?

Good threads: Vegetable Lamb of Tartary (medieval people thought cotton grew sheep), tomato fear (pewter plates killed people, not tomatoes), Cockeram's 1623 dictionary (captured the word at a moment of transition).

Bad padding: "The history of the word is very interesting and long." That's a sentence that exists to fill space.

### 4. Voice — relaxing and charming
- Don't over-explain. Trust the listener.
- The occasional dry observation: "Now it means broccoli."
- Read passages, then unpack clause by clause.
- Ask questions the listener is already thinking.
- Let surprising facts land, then pause before moving on.

### 5. Source material as script
The best moments in the script come from reading actual passages:
- "Vegetive — Which liveth as plants do." (Cockeram, 1623)
- "Ða fæmnan þe gewuniað onfon gealdorcræftigan & scinlæcan & wiccan, ne læt þu ða libban." (Laws of Ælfred, 890)
- "Astonishingly, Mimosa can display the learned response even when left undisturbed in a more favourable environment for a month." (Gagliano, 2014)

These are real words from real documents. They carry the weight of history. They're better than anything I could write.

---

## Files created

```
sleepvids/
├── channels/
│   ├── etymology/
│   │   ├── process/
│   │   │   └── process.md          # Repeatability guide (updated with voice/thread principles)
│   │   └── videos/
│   │       └── 001_vegetable/
│   │           ├── RESEARCH.md      # Raw data dump (etymonline, papers, Aristotle, etc.)
│   │           ├── SCAFFOLD.md      # Narrative arc, loops, emotional shape
│   │           ├── STORYBOARD.md    # 16 scenes, time/word/tone targets
│   │           ├── HOOK.md          # Opening 7 minutes
│   │           ├── THREAD_NOTES.md  # Expansion candidates
│   │           └── DRAFT.md         # 9,991-word script (95 min)
│   └── interesting_tribes/
│       └── channel.json             # Channel definition + process notes
```

---

## Process principles (for repeatability)

1. **Research is the script.** Don't write summaries. Hoard full passages. Read them out loud. Unpack them clause by clause.

2. **Threads, not padding.** When a section needs more words, find a new thread — a person, a place, a quote, a connection. Don't add filler.

3. **Find the loops.** The linear timeline is the spine. The loops are the story. Where does the word contradict itself? Where does science overturn philosophy? Where does the past haunt the present?

4. **Respect the listener.** They're smart. Don't over-explain. Trust them to follow. Use the occasional dry observation. Let surprising facts land.

5. **Read source passages directly.** Real words from real documents carry more weight than paraphrasing. Cockeram's 1623 definition. The Laws of Ælfred in Old English. Gagliano's abstract.

6. **The taper is real.** Section 1 is engaging. Section 6 is soft. The listener should be falling asleep by the end. Each sentence shorter than the last.

7. **Every word earns its place.** If a sentence exists only to fill space, cut it. If it reveals something about the word, keep it.
