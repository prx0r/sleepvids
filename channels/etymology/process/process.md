# process.md — How to write a deep etymology essay

## The pipeline

```
0. PICK THE WORD
1. RESEARCH (hoard everything)
2. SCAFFOLD (structure the journey)
3. STORYBOARD (scene-by-scene breakdown)
4. DRAFT (write section by section)
5. TRIM/PAD (hit 12,600 words)
6. RECORD (TTS narration)
```

## Step 0: Pick the word

Criteria:
- Dramatic meaning shift (ideally opposite or surprising)
- Rich etymology (PIE root → multiple language transitions)
- Philosophical connections (Aristotle, medieval thinkers)
- Historical journey (centuries of documented usage change)
- Modern relevance (science, medicine, culture)
- Tangent potential (word leads to interesting places)

The word must answer: "Can I talk about this for 2 hours without it getting boring?"

## Step 1: Research (hoard everything)

Create: `videos/NNN_word/RESEARCH.md`

Sources to hit:
1. **Etymonline** — full entry for the word + all related words from same root
2. **Wiktionary** — etymology tree, cognates, descendant languages
3. **PIE root family** — every English word from the same root (etymonline.com/word/*ROOT)
4. **Gutenberg** — Aristotle De Anima (or relevant philosophical source)
5. **Academic papers** — key paper abstracts + key passages (PubMed, PMC)
6. **Wikipedia** — background on philosophers, scientists, medical terms
7. **YouTube** — competitor landscape (search the word + "etymology" + "sleep")
8. **Merriam-Webster / Dictionary.com** — additional definitions and usage quotes

Format: Raw passages, not summaries. Full quotes we can read out. Include source URLs.

## Step 2: Scaffold the journey

Create: `videos/NNN_word/SCAFFOLD.md`

Map the narrative arc:
- Where does the word start? (PIE root)
- Where does it go? (language transitions)
- What's the turning point? (meaning shift)
- Where does it end? (modern meaning)
- What loops back? (contradictions, ironies)

Key question: What's the ONE story this word tells?

Examples:
- vegetable: "alive" → "food" → "brain-dead" (Aristotle's ghost)
- silly: "holy" → "foolish" (the greatest reversal)
- nice: "ignorant" → "pleasant" (six hundred years of upward drift)
- panic: "god" → "feeling" (divinity becomes anxiety)
- algorithm: "a man's name" → "machine thinking" (person becomes method)

## Step 3: Storyboard

Create: `videos/NNN_word/STORYBOARD.md`

Scene-by-scene breakdown. Each scene has:
- Section number
- Title
- Time window
- Word target
- Content summary
- Key passages to read out
- Tangents to follow
- Tone (engaging vs cozy vs sleep-inducing)

## Step 4: Draft

Create: `videos/NNN_word/DRAFT.md`

Write section by section. Rules:
- Read source passages directly (don't rewrite — quote and unpack)
- Use the hook structure: The Moment → The Map → The Cozy Opening
- Go deep on tangents in sections 2-4
- Taper hard in section 6
- Aim for 105 WPM (sleep pace)
- No cliffhangers, no tension, no sudden changes
- End with "Sleep well."

## Voice: Relaxing and Charming

The listener is smart. Don't waste their time. Don't over-explain things they already know. Don't pad for the sake of padding.

The voice is:
- **Relaxing** — slow, warm, unhurried. Like a late-night radio host.
- **Charming** — gentle humor, surprising connections, the occasional wink.
- **Respectful** — the listener is intelligent. Trust them to follow.
- **Cozy** — the feeling of being read to by someone who knows the story well.

What makes the voice charming:
- Asking questions the listener is already thinking: "How did that happen?"
- The occasional dry observation: "Now it means broccoli."
- Reading a passage, then unpacking it clause by clause, like sharing a secret
- Finding the human behind the history: Aristotle walking in the Lyceum, monks in their gardens
- Letting a surprising fact land, then pausing before moving on
- Not being afraid of silence between ideas

What kills the voice:
- Excitement or hype — this is sleep content, not a TED talk
- Over-explaining — trust the listener
- Padding — adding words that don't earn their place
- Academic dryness — this isn't a lecture, it's a story
- Forcing humor — it should feel natural, not scripted

## NoSlop — the anti-pattern rules

Run every draft through NoSlop (`/root/noslop/miner/src/detector.py`). Treat it as gospel.

### NEG patterns (negation scaffolding) — ELIMINATE
The worst pattern. "Not X but Y." "It wasn't X. It was Y." The reader learns to skip the first half of every sentence.

**Bad:** "The word wasn't about food. It was about being alive."
**Good:** "The word was about being alive."

**Bad:** "Not just a philosophical category now. As a practical label."
**Good:** "A practical label."

**Bad:** "Vegetables was something else. Vegetables was about being alive."
**Good:** "Vegetables were about being alive."

The repair: State what it IS. No negation, no implied negation. Delete the "not X" clause and see if the sentence still works. If it does, the negation was scaffolding.

Exception: One or two negations per essay can work as a defining gesture. "The word meant alive — not food." But use sparingly. One per section maximum.

### 3LIST patterns (three-item lists) — BREAK INTO PROSE
Three-item lists are the most common slop signal. "X, Y, and Z." They feel mechanical. They feel like the writer is filling space.

**Bad:** "They grew lavender for calm, chamomile for sleep, rosemary for memory."
**Good:** "They grew lavender for calm. Chamomile for sleep. Rosemary for memory." (Period-separated — slows the pace, more cozy)

**Bad:** "vigour, wake, watch, witch"
**Good:** "vigour. wake. watch. witch." (Each word gets its own beat)

**Bad:** "Through the Renaissance. Through the Reformation. Through the Enlightenment."
**Good:** "Through the Renaissance and the Reformation and the Enlightenment." (Merged — feels like one flowing thought)

The rule: If the three items are a deliberate rhythm (listing root family words, building a cadence), period-separate them. If they're just a list, merge them into flowing prose. Never use the "X, Y, and Z" pattern.

### NARR patterns (tour-guide narration) — CUT OR RESTATE
"This section examines..." "We now turn to..." "What follows is..." The reader doesn't need a tour guide. They need the content.

**Bad:** "Let's talk about what the medieval world looked like for this word."
**Good:** Just start talking about the medieval world.

**Bad:** "Let's spend a moment with each of the major cognates."
**Good:** Start spending the moment. Don't announce it.

Exception: One orienting narration per 500 words, only if it does genuine orienting work (telling the reader where they are in a long journey). Test: delete it. If the reader isn't lost, it was padding.

### FLAT patterns (uniform sentence length) — VARY THE RHYTHM
If all sentences are the same length, the prose feels robotic. Mix short punches with longer flowing sentences. Let some sentences trail off. Let others land hard.

### CHOPPY patterns (staccato fragmentation) — WEAVE INTO PROSE
Short sentences of 1-5 words are the most common slop signal. They feel like the writer couldn't sustain a thought.

**Exception for this project:** The etymology voice uses short sentences for emphasis. "Vegetus meant vigorous. Active. Sprightly." This is deliberate rhythm, not laziness. The test: read aloud. If the short sentence feels like a beat that lands a point, keep it. If it feels like connecting tissue that breaks the flow, rewrite it.

Rule: max 3 short sentences in a row. After 3, merge into flowing prose. Never stack 4+ short sentences.

### CLICHE patterns — AVOID
"Trust the process." "Step into your power." "Living your truth." These don't apply to etymology content, but be aware they exist.

## Threads, Not Padding

When a section needs more words, don't add filler. Find a thread worth following.

A thread is:
- A person you can meet (Aristotle, Gagliano, Cockeram)
- A place you can visit (the Lyceum, a monastery garden, a hospital room)
- A passage you can read out loud (from a paper, a dictionary, a law)
- A surprising connection (vegetable and witch come from the same root)
- A detail that brings the era to life (Roman gardens had a space set apart for olera)
- A question that the listener is already asking (if plants are intelligent, what does that mean?)

A thread earns its place if:
- It tells us something about the word we didn't know
- It reveals something about how humans think
- It creates a moment of "wait, WHAT?"
- It connects back to the main story
- It's genuinely interesting

A thread does NOT earn its place if:
- It's just more words about the same thing
- It repeats what we already said
- It doesn't connect back
- It's there because the word count was low

Example of a thread worth following: "The same root that gives us vegetable gives us witch. Let's talk about that."
Example of padding: "There are many interesting things about the word vegetable. One interesting thing is its history. The history is very long and interesting."

## Step 5: Trim/pad

Hit 12,600 words (2 hours at 105 WPM).

Expansion strategies (threads, not padding):
- Read a source passage out loud, then unpack it line by line
- Follow a surprising connection to its endpoint (vegetable → witch → Wicca)
- Paint a scene (a monk in a garden, a Roman market, Aristotle in the Lyceum)
- Introduce a person (who was Cockeram? who was Gagliano?)
- Quote a law or dictionary definition, then unpack it
- Ask a question, then let the listener sit with it before answering

Trimming strategies:
- Cut repetition that doesn't serve the sleep function
- Tighten threads that don't connect back
- Remove anything that creates tension or excitement in the wrong sections
- Remove any sentence that exists only to fill space

## Step 6: Record

TTS generation:
- Voice: V03 Lecturer (etymology/mind shelf)
- Pace: -30% (105 WPM)
- Provider: Edge TTS or Qwen3 TTS
- Output: nar.mp3 + nar.srt

## Word targets per section

| Section | Time | Words | Purpose |
|---------|------|-------|---------|
| 1. Hook + Opening | 7 min | 735 | The Moment + The Map + Cozy Opening |
| 2. The Etymology | 15 min | 1,575 | PIE root → Latin → Old French → Middle English |
| 3. Historical Journey | 30 min | 3,150 | Century by century — tangents encouraged |
| 4. Philosophy | 30 min | 3,150 | Aristotle passages, medieval context, hierarchy |
| 5. Science | 25 min | 2,625 | Modern research, the word's second life |
| 6. Return | 13 min | 1,365 | Circle back, slow down, sleep well |
| **Total** | **120 min** | **12,600** | |

## Folder structure per video

```
videos/NNN_word/
├── RESEARCH.md          # Raw data dump (Step 1)
├── SCAFFOLD.md          # Narrative arc (Step 2)
├── STORYBOARD.md        # Scene-by-scene (Step 3)
├── sections/            # One file per scene (Step 4)
│   ├── section_01.md    # Hook
│   ├── section_02.md    # Root
│   ├── section_03.md    # History
│   ├── ...
│   └── section_NN.md    # Return
├── DRAFT.md             # Compiled from sections/ (Step 5)
├── HOOK.md              # Opening 5 minutes (standalone)
└── meta.json            # Video metadata (engine, voice, SEO, sources)
```

**Key rule: work in sections/, not in DRAFT.md.** Each section is an independent file. Edit section by section. Run NoSlop on each section individually. Only compile into DRAFT.md when all sections are clean.

## The fix loop (simple)

1. `cat sections/section_0X.md | python3 /root/noslop/miner/src/detector.py`
2. Look at what's flagged (3LIST, NEG, SIGNPOST, CHOPPY)
3. Open the section file, fix the flagged patterns
4. Re-run NoSlop
5. Repeat until clean
6. Move to next section
7. When all sections are clean: `cat sections/*.md > DRAFT.md`

## Passage maxing (the expansion strategy)

**The principle:** Don't write about what sources say. READ the sources. Quote them directly. Unpack them clause by clause. This is real content, not padding. It's what the user came for.

**How it works:**
1. Find a primary source (book, paper, historical text, interview)
2. Extract the key passage (1-5 sentences)
3. Read it out in the essay
4. Unpack it — what does each clause mean? What's surprising? What connects back?
5. The passage becomes 200-500 words of essay content

**Examples:**
- Knuth: "The word algorithm comes from the name of a famous Persian textbook author..." → unpack the etymology, the irony, the "pseudo-etymological perversion"
- Knuth: "An algorithm must be seen to be believed" → unpack what this means
- Aristotle: "the soul is the first actuality of a natural body having life potentially within it" → unpack clause by clause
- Gagliano: "Mimosa can display the learned response even when left undisturbed in a more favourable environment for a month" → unpack the implications
- Donald Glover: "I want to thank the great algorithm" → unpack the irony
- Uber driver: "the boss is the algorithm" → unpack the power dynamic

**Why this works:**
- Real words from real people carry weight
- The listener hears actual source material, not paraphrasing
- Each passage unpacks into 200-500 words naturally
- No slop — the source does the work

**The math:**
- 12,000 words ÷ 105 WPM = 114 minutes
- If each passage is ~300 words, and we have 40 passages, that's 12,000 words
- 40 passages × ~300 words each = 12,000 words

**Where to find passages:**
- Etymonline (full entries for each word)
- Wiktionary (etymology trees, quotations)
- Academic papers (abstracts, key findings)
- Historical texts (Gutenberg PD books)
- Interviews (NPR, The Guardian, etc.)
- Dictionaries (Oxford, Merriam-Webster, historical)
- Knuth's Art of Computer Programming
- Aristotle's De Anima
- The actual Latin manuscripts (Dixit Algoritmi)

## Checklist before recording

- [ ] Word count is ~12,600 (±500)
- [ ] All claims sourced (no invented facts)
- [ ] No cliffhangers or tension in wrong places
- [ ] Section 6 is slower and softer than Section 1
- [ ] At least 3 loops/contradictions identified and hit
- [ ] Key quotes from sources read out (not paraphrased)
- [ ] "Sleep well" at the end

## Word count reality check

The first draft of vegetable came in at ~9,000 words (85 min). Here's why that's OK:
- The 12,600 target is aspirational. 9,000-12,600 is the acceptable range.
- A 90-minute video is still a solid format.
- Better to have 9,000 good words than 12,600 padded ones.
- Additional words should come from genuine threads, not filler.
- If you need to hit 2 hours, find another thread worth following. Don't add fluff.

## NoSlop results (vegetable, after fix pass)

| Metric | Before | After |
|--------|--------|-------|
| Short sentences (<=5 words) | 52% | 15% |
| Average sentence length | 6.5 words | 17.6 words |
| NEG patterns | 83 | 52 |
| 3LIST patterns | 57 | 162 (but embedded in prose) |
| CHOPPY flag | yes | yes (15%, borderline) |
| Words | 9,991 | 9,303 |
| Minutes | 95 | 89 |

**What changed:**
- Merged short sentences into flowing complex prose
- Removed negation scaffolding ("Not X but Y" → direct assertions)
- Broke three-item lists into flowing text
- Removed signposting ("Here's how it happened" → just tell it)
- Kept emphasis short sentences for highest impact only

**Still flagged:** 3LIST (162) — mostly embedded in flowing prose (listing root family words, historical details). Acceptable within flowing sentences. NEG (52) — some remain in quotes from sources and where negation is semantically necessary.

---

## Algorithm — expansion pass

**Word counts per section:**
| Section | Before | After | Added |
|---------|--------|-------|-------|
| Hook/Map/Opening | 309 | ~700 | +391 |
| Man and His Book | 806 | ~1,500 | +694 |
| Journey of Word | 728 | ~2,500 | +1,772 |
| Modern Demon | 690 | ~2,500 | +1,810 |
| Return | 339 | ~1,000 | +661 |
| **Total** | **2,884** | **4,507** | **+1,623** |

**Rabbit holes added:**
1. Algorithms in nature (ants, slime molds, DNA, evolution) — Section 2
2. Competing terms (algorists vs abacists, 1503 woodcut, Fibonacci) — Section 3
3. Euclid's algorithm (predates al-Khwarizmi by 1,200 years) — Section 2
4. Pingāla (algorithmic thinking in ancient India, 200 BCE) — Section 2
5. The "al-" prefix family (alcohol, alkali, alchemy, Altair) — Section 4
6. Knuth + Dijkstra + computing transition — Section 4
7. The spelling corruption (Knuth's "pseudo-etymological perversion") — Section 3

**NoSlop:** 0.71 confidence, 41 patterns (26 3LIST, 12 NEG, 1 NARR, 1 SIGNPOST, 1 CHOPPY)

**Key learning:** The second word was much easier. The process is now:
1. Create folder structure
2. Research → RESEARCH.md (hoard everything)
3. Scaffold → SCAFFOLD.md (arc, loops)
4. Storyboard → STORYBOARD.md (scenes)
5. Write sections directly into sections/ (apply NoSlop as you write)
6. Compile → DRAFT.md
7. NoSlop check

**Why algorithm was cleaner:**
- Applied NoSlop rules while writing, not after
- Fewer lists (algorithm's story is more linear — person → book → word → modern)
- Less need for negation (the story is affirmative — "this is what happened")
- The loops are stronger (person → method → system → demon)

**Algorithm NoSlop scores:**
- Confidence: 0.67 (vs 0.99 for vegetable)
- NEG: 2 (vs 52 for vegetable)
- 3LIST: 15 (vs 162 for vegetable)
- CHOPPY: borderline but acceptable

**Sections need expansion:** Current draft is 2,091 words (20 min). Needs ~10,000 more to hit 2 hours. Expansion should follow the same principle: threads, not padding. The research pack has enough material for a full 2-hour essay.

---

## Key learnings across both videos

### 1. Write clean from the start
The algorithm draft was written in one pass with NoSlop principles in mind. The vegetable draft was written sloppily and then fixed. Writing clean is 10x faster than fixing after. Apply these rules while writing:
- No "Not X but Y" — just state what it IS
- No "X, Y, and Z" lists — use flowing prose
- No "Here's what happened" — just tell what happened
- No short sentences stacked — merge into complex prose
- Keep short sentences only for highest impact (2-3 per essay)

### 2. The tone mix
Each word needs a balance of:
- **Historical** — what happened, when, who was involved
- **Philosophical** — what it means, how humans think
- **Technical** — etymology trees, root families, language transitions
- **Light humour** — dry observations, surprising connections ("now it means broccoli")

### 3. Research depth matters
The more you research, the better the tangents. Vegetable had great tangents (Vegetable Lamb of Tartary, tomato fear, Bonnefons). Algorithm needs similar depth — Knuth, Pingāla, the "al-" prefix family, the spelling corruption.

### 4. The loops make the essay
Linear timelines are the spine. Loops are the story. For each word, find:
- Where does the word contradict itself?
- Where does the past haunt the present?
- Where does science overturn philosophy?
- Where does the root family tell a different story?

### 5. Rabbit holes are the expansion strategy
When a section needs more words, don't pad. Follow a rabbit hole:
- **Algorithms in nature** — ant colony optimization, slime molds, evolution as algorithm. The concept predates the word.
- **Competing terms** — algorism vs algorithm. The algorists vs abacists war. The 1503 woodcut.
- **The "al-" family** — alcohol, alkali, alchemy, Altair. Arabic fossils in English.
- **The oldest algorithm** — Euclid, 300 BCE. Knuth: "the granddaddy of all algorithms."
- **Pingāla** — algorithmic thinking in ancient India, 200 BCE.
- **What is an algorithm** — the recipe analogy. Knuth's five properties. The computer as literal cook.
- **Conway's Game of Life** — four rules create life. Cellular automata. Turing complete.
- **Algorithms everywhere** — Spotify, Netflix, TikTok, GPS. Every app is an algorithm.
- **AI and deep learning** — neural networks, GPT, algorithms that learn. The recipe becomes the chef.
- **The attention economy** — algorithms that shape behavior. TikTok, Netflix, the feedback loop.

Each rabbit hole should:
1. Connect back to the main story
2. Add a surprising fact or quote
3. Be 200-500 words
4. Not feel like padding

### 6. The tone mix (repeatable across words)
Every essay needs:
- 1 historical deep dive (the person, the place, the era)
- 1 technical detour (how the thing works, competing terms, the science)
- 1 nature/universal connection (algorithms in ants, vegetable Lamb, the root family)
- 1 modern loop (how the word haunts us today)
- Dry humour throughout ("now it means broccoli," "the spelling is a lie")
