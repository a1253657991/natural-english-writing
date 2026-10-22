---
name: natural-english-writing
description: Write, revise, translate or audit professional and academic English so it reads as the work of a specific expert writing for a specific reader, not as generic LLM prose, without trading accuracy or quality for "human-sounding" tricks. Always starts by confirming the requirements with the user, asking as many questions as needed. Use whenever the user wants English prose drafted from notes, an English draft polished, a Chinese (or other) draft turned into English, or a text checked for "AI tone" (AI味, sounds like ChatGPT): papers, abstracts, essays, assignments, personal statements, cover letters, reports, memos, emails. Especially relevant when expert readers such as linguists, editors, examiners or reviewers will read closely. Not for chasing AI-detector scores.
license: MIT
metadata:
  version: "2.0.0"
---

# Natural English writing

The goal is text that a careful expert reader, including a linguist, reads as the work of a particular writer addressing them: faithful to the material, right for the genre, specific, and with a stance the evidence supports. Removing "AI tells" is a check at the end, not the method.

## Principles

1. **The material governs content.** Every claim, number, name, example, quotation and citation comes from the user's material or answers. Never invent one; ask, or mark it `[NEED: …]`. Keep each claim at the strength the material gives it. An interpretive link (because, so, which means, implies for policy) is also a claim: if the text needs one the material does not give, ask for it; if the user has said not to ask, keep it out of the text and offer it in the notes as a suggestion. An invented specific does more damage than a generic sentence: expert readers check, and one fabricated citation ends the text's credibility.
2. **The brief governs style.** Reader, genre, purpose and any sample decide each stylistic choice. The pattern catalogue is a diagnostic list, not a rulebook; it never overrides the brief or the genre (APA headings use title case, methods sections use the passive, a research article needs its limitations section).
3. **Fix causes, not words.** Generated prose sounds generated mainly because it lacks specific content, a specific reader and a stance. Supplying those removes most tells. Swapping a flagged word for a synonym keeps the sentence's shape and usually produces an odd collocation. Lists of words to avoid also pull attention toward those words, so they stay out of the drafting phase.
4. **Do not fake a human.** Do not add errors, slang, contractions, rhetorical questions, fragments, anecdotes or opinions the user did not supply in order to "sound human". Expert readers notice a register break faster than they notice polish; error-free prose is not the problem.
5. **Edit lightly what the user wrote.** In the user's own draft, keep their wording wherever it is correct and clear.

## Workflow

Work through the phases in order. Questions are welcome at every phase.

### Phase 1: Confirm the requirements (always first)

Before drafting or editing anything, settle the brief with the user. Do this first on every use, including requests that look simple, because most bad output comes from a wrong guess about reader, genre or purpose.

1. Read everything the user has provided (notes, drafts, samples, guidelines, rubric) so that questions are informed and nothing already answered is asked again.
2. Read `references/intake.md` for the question bank and the brief template.
3. Ask in rounds, in the user's language. There is no limit on the number of questions or rounds: continue until nothing that would change the text is ambiguous. Keep each round to a few related questions so it is easy to answer. With each question, give the reason in a few words and a recommended default where one exists, so the user can simply accept it.
4. Where the AskUserQuestion tool is available, use it for choice questions (up to four per call; call again for more). Ask open questions, such as "paste your notes", in plain text.
5. Question the material as well: conflicting numbers, unclear referents, undefined abbreviations, claims of unclear strength, sources without enough detail to cite.
6. When nothing ambiguous remains, write the brief from the template in the user's language and ask the user to confirm or correct it. Start Phase 2 only after they confirm.

If the user wants no questions, still show the brief, mark your guesses `[ASSUMED]`, and get a yes. If the user's message already contains a complete brief that they say is confirmed, restate it in a few lines and continue; ask only about real gaps or conflicts.

If a new ambiguity appears later (a gap, a conflict, a claim you cannot state at the right strength), stop and ask rather than guess.

### Phase 2: Inventory the content

1. List the claims the text must make, numbered, each with its source (note, file, answer) and its strength: established, likely, speculative, or the user's opinion.
2. List gaps as `[NEED: …]` and ask about them.
3. For texts over about 300 words, or when no template fixes the structure, write an outline: one line per paragraph or section, giving its job and the claims it carries. Agree the outline with the user before writing prose. Structure is decided here, from the argument, which prevents the symmetric default structure that generated text falls into.

### Phase 3: Set the register

1. If the user gave a sample (their own writing or a model text from the venue), profile it in at most eight lines: sentence-length range; person (I, we, impersonal); voice and tense habits; how claims are hedged and boosted; how sources are integrated; paragraph length; headings and lists; punctuation habits (dashes, semicolons, serial comma); spelling variety.
2. Without a sample, take the profile for the genre from `references/genres.md`.
3. The profile is the target. Where the profile and the pattern catalogue disagree, the profile wins.

### Phase 4: Draft

Write from the inventory and the outline, to the profile. These habits make prose specific and readable for an expert, and they are what generated prose usually lacks:

- One job per paragraph, and paragraphs that build on each other. Give space by importance. Open with the point; end on the last substantive point rather than a summary of it.
- Every sentence adds a fact, reason, consequence or qualification from the inventory. If a sentence would fit unchanged into another document on the same topic, make it specific or cut it.
- Characters as subjects and actions as verbs ("the bank cut limits", not "a reduction in limits was implemented"), except where the genre or the information flow calls for the passive or a nominal style (methods, legal text, unknown or irrelevant agent). Generated prose tends to have too many nominalisations and too few agentless passives, so do not convert passives by reflex.
- Known information early in the sentence, new information late; keep consecutive sentences on the same topic. Carry cohesion by repeating key terms and referring back; use connectives such as "however" or "therefore" where they mark a real logical relation.
- One term for one concept throughout.
- Show the author's stance as far as the genre allows: what you conclude, how confident you are, and why. Hedge where the evidence is uncertain and state plainly where it is not. Expert readers notice a missing authorial position as much as an overclaim.
- Plain verbs (is, has, shows) and the field's own terms. Use a less common word only when it is more precise.
- Let sentence length follow content: a short sentence for a key finding, a longer one for a qualified claim. Do not vary length for its own sake.
- Format by genre: prose unless the genre uses lists; headings as the style guide sets them.

Mode-specific rules:

- **Revise** (the user's English draft): make minimal edits. Fix errors, ambiguity and cohesion; keep the user's words and sentence structures when they are correct; do not upgrade plain words. Ask before structural changes. Report language fixes separately from substantive suggestions.
- **Translate** (a Chinese or other draft into English): translate the meaning and the argument, not the sentence structure. Re-segment sentences, restore English information order, and replace calques and set phrases with what an English writer in the field would write. Use the field's established English terms and ask when unsure. Stacked modifiers, four-character set phrases and parallel listing habits in the source tend to produce nominal, list-heavy English.
- **Audit only**: skip drafting. Run Phases 5 and 6 on the given text and report findings without rewriting unless asked.

### Phase 5: Audit

Read `references/patterns.md` now, not earlier. Go through the draft and record each finding: the quoted span, the pattern ID, strong or weak, and the proposed fix. Act on a weak pattern only when it clusters with other tells in the same passage. Fix by restating, specifying, merging or cutting, never by swapping in a synonym. Leave a pattern alone when the brief, the profile or the entry's "Leave it when" note covers it.

### Phase 6: Verify and deliver

Check before delivering:

1. **Fidelity.** Compare against the Phase 2 inventory: nothing added beyond the material (including inferences and causal or policy links), nothing the brief needs has been dropped, no claim made stronger or weaker, and numbers, names and citations are unchanged.
2. **Overcorrection.** No casual markers, fragments, rhetorical questions or rare-word substitutions were introduced, and no move the genre requires was removed (limitations, method detail, required signposting).
3. **Register.** The whole text matches the profile; no section reads differently from the rest.
4. **Surviving tells.** Re-scan for the patterns that most often survive revision: not-X-but-Y contrasts, triads, trailing -ing commentary, paragraph-final summaries and connector-led openings.
5. **Brief.** Length, spelling variety, citation style and format are as agreed.

Deliver, in this order:

1. The final text.
2. In the user's language: a short change note (substantive changes listed separately from language fixes), any remaining `[NEED: …]` items, and the places where the user's own judgement is needed, such as a stance, a trade-off or a fact to check.
3. The audit table, only if the user asked for it or chose audit mode.

Treat any correction the user makes afterwards as new brief information.

## Reference files

- `references/intake.md`: question bank and brief template (Phase 1).
- `references/genres.md`: register profiles for common genres when there is no sample (Phase 3).
- `references/patterns.md`: catalogue of generated-prose patterns, with fixes and exceptions (Phase 5 only).
