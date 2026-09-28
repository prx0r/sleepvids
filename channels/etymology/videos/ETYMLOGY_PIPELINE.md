# Etymology Video Pipeline — "Sleepy Etymology"

Deep-dive word origin stories for sleep. One word per episode. 2 hours. Narrative, winding, surprising.

## Concept

Pick a common English word. Trace its full etymology from PIE root → Latin/Greek → Old French → Middle English → modern meaning. The "hook" is that the word's original meaning is the OPPOSITE of what it means now.

## The 5 MVP words

| # | Word | Original meaning → Modern meaning | Clickbait hook |
|---|------|-----------------------------------|----------------|
| 1 | **vegetable** | "alive, growing" (Latin vegetabilis) → "food plant" | "Vegetable used to mean ALIVE. Now it means DINNER." |
| 2 | **algorithm** | "a guy's name" (al-Khwarizmi, Persian mathematician) → "machine thinking" | "Algorithm is just a PERSON'S NAME." |
| 3 | **nice** | "ignorant, foolish" (Latin nescius) → "pleasant, kind" | "Nice used to mean STUPID." |
| 4 | **silly** | "blessed, holy" (Old English sælig) → "foolish" | "Silly used to mean HOLY." |
| 5 | **panic** | "of Pan, the Greek god" → "sudden overwhelming fear" | "Panic is named after a GOD." |

## Narrative arc per episode

```
Section 1: The Hook (5 min, ~525 words)
  - "Today we say X to mean Y. But 500 years ago, it meant Z."
  - Establish the word in modern context
  - Create the contrast that makes the listener curious
  - Map out the journey ahead

Section 2: The Etymology (15 min, ~1,575 words)
  - PIE root (the proto-language, 5000+ years ago)
  - Latin / Ancient Greek branch
  - Old French entry into English
  - The Norman Conquest (1066) as the gateway
  - First recorded use in Middle English (cite OED / etymonline)

Section 3: The Historical Journey (30 min, ~3,150 words)
  - Century by century: who used it, how it shifted
  - Key texts: Chaucer, Shakespeare, the King James Bible
  - Social/political events that drove semantic change
  - Cognates in other European languages
  - Related words that share the root (mini-etymologies within the main one)

Section 4: The Philosophy (30 min, ~3,150 words)
  - What the original meaning reveals about how people thought
  - Aristotle's classification (if applicable)
  - Theological/philosophical implications
  - Modern scientific understanding that vindicates or overturns the ancient meaning

Section 5: The Return (10 min, ~1,050 words)
  - Circle back to the original meaning
  - What the word means now vs. then
  - The comfort of knowing a word's full story
  - "Sleep well."
```

## Research workflow per episode

1. **etymonline.com** — primary source, quote directly
2. **Wiktionary** — etymology tree, cognates, reconstructed proto-forms
3. **OED** (via library) — first recorded usage, dated quotes
4. **Google Books Ngram** — track frequency over centuries
5. **PIE etymology resources** — Mallory & Adams, Watkins' dictionary
6. **Academic sources** — Aristotle's De Anima (Loeb), medieval bestiaries, etc.
7. **Cross-check** — every claim needs 2+ sources

## Output files per video

```
channels/etymology/videos/NNN_word/
├── RESEARCH.md           — Full source dump, quotes, citations
├── meta.json              — Video metadata
├── sections/
│   ├── 01_hook.md
│   ├── 02_etymology.md
│   ├── 03_journey.md
│   ├── 04_philosophy.md
│   └── 05_return.md
└── DRAFT.md              — Compiled full script
```

## Quality standards

- Every etymological claim has a named source
- Read primary source passages out loud when possible
- Cross-reference cognates to build the "root family tree"
- No padding — if a section is thin, find more rabbit holes
- The narrative should feel like wandering through a library, not reading a textbook
- End each episode with the word's original meaning echoing back

## Voice

- Warm, curious, slightly awed
- "Isn't that strange?" not "As we can see from the data"
- Occasional dry humor
- Treats ancient people as real humans, not primitives
- The word is the protagonist
