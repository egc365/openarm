# Role cart, 2026-10-08

The installed KSAO picker was not run. `/wiki/outputs/ksao-v4-20260929/OWNER-HANDOFF.md` says that picker is unsafe and that version 4 is not approved. The v0.3 procedure was followed by hand. Each role below may use only the listed skill. A role does not get CAD write access.

## Survey reader

Job: read the Black Belt handbook and return a page locator for DMAIC.
Input: corpus book search.
Output: retrieval refusal.
Skill: `/home/egc365/Documents/skills/daniel skills/ksao_mcp_v0.3/ksao_mcp/SKILL.md`
Tool: corpus `corpus_books` and `corpus_search` only.
Result: both handbook editions are historical-working and unaccepted. Search returned HTTP 400. No quotation was taken from the handbook.

## Web and forum reader

Job: bring current failure reports for small printed gears, and the GitHub file-size rule.
Skill: `/home/egc365/Documents/skills/matt-skills/skills/engineering/research/SKILL.md`
Skill: `/home/egc365/Documents/skills/pstack-main/skills/unslop/SKILL.md`
Tool: web search and page fetch. No CAD write.
Result: the sources in `references.md`.

## Recorder

Job: write this folder, the decision log, and the crosswalk.
Skill: `/home/egc365/Documents/skills/matt-skills/skills/productivity/writing-for-agents/SKILL.md`
Skill: `/home/egc365/Documents/skills/pstack-main/skills/unslop/SKILL.md`
Skill: `/home/egc365/Documents/skills/pstack-main/skills/show-me-your-work/SKILL.md`
Tool: local files only. Do not edit run2, the engineering arm, or the gantry directory.

## Adversarial reviewer

Job: read this folder and flag a claim that has no file path or no URL.
Skill: `/home/egc365/Documents/skills/pstack-main/skills/unslop/SKILL.md`
Skill: `/home/egc365/Documents/skills/pstack-main/skills/interrogate/SKILL.md`
Tool: read only. Two reviewers, two model families. Sol and Opus 5.5 are not in this session's model list, so they were not called.
Done when: the reviewer returns flags tied to a file, or the words "no flags".
