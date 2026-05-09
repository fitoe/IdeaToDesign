# Stage Gates

Use these gates to keep `idea-to-design` simple and controlled.

## Gate 1: Scope -> Structure

Must have:
- one-sentence product definition
- target user identified
- current scope defined
- non-goal or exclusion stated
- at least one candidate core flow

Do not proceed if:
- project scope is still "entire platform"
- no clear user task exists
- user input is so broad that no core journey can be selected

If blocked:
- reduce to one primary use case
- state assumptions explicitly
- draft a narrow first-pass scope

---

## Gate 2: Structure -> Visual Direction

Must have:
- at least one approved core flow
- page index exists
- core vs supporting pages separated
- 3-5 core pages selected for deeper work

Do not proceed if:
- pages are still disconnected
- no page purpose is defined
- product structure is changing at a high level

If blocked:
- rewrite flow summary
- simplify page inventory
- drop non-core pages from active scope

---

## Gate 3: Visual Direction -> Image Iteration

Must have:
- one selected design direction
- visual principles defined
- text wireframes for core pages
- clear distinction between structure and style decisions

Do not proceed if:
- multiple visual directions remain unresolved
- no text wireframes exist
- visual exploration is being used to discover product logic

If blocked:
- pick one direction
- write text wireframes first
- move unresolved product logic back to structure

---

## Gate 4: Wireframe -> Mid-Fi

Must have:
- structure accepted
- main blocks stable
- CTA placement stable
- main interaction pattern stable

Do not proceed if:
- page layout is still shifting heavily
- content hierarchy is unclear
- user is still debating page purpose

If blocked:
- revise text wireframe
- reduce change scope to one page or one problem

---

## Gate 5: Mid-Fi -> Hi-Fi

Must have:
- stable information hierarchy
- stable component direction
- stable visual tone
- only local refinements remaining

Do not proceed if:
- core layout is still changing
- major product decisions are unresolved
- new features are being inferred from images

If blocked:
- return to mid-fi
- update spec first
- confirm whether new elements are official or just visual noise

---

## Gate 6: Finalize Design Doc

Must have:
- approved structure
- approved design direction
- approved visuals for core pages
- clear notes for key interactions and states

Do not proceed if:
- final doc would mostly contain drafts
- core pages still lack stable visuals
- process notes are being mistaken for final decisions

If blocked:
- mark unresolved items clearly
- reduce doc scope to confirmed material only
- keep process material in background files, not main doc

---

## Compression Rules

Always prefer lighter final output.

Default:
- one main doc
- one asset directory
- one state file

Only expand when:
- user asks for archival depth
- project complexity truly requires it
- team handoff demands more traceability

---

## Escalation Rules

Escalate only when needed.

### Expanded Mode
Use when:
- more than 8-10 pages
- more than 2 meaningful flows
- formal team handoff needed

### Archive Mode
Use when:
- many visual branches were explored
- long-running project needs history
- prompts and rejected options must be preserved


---

## Gate 7: Level 3 Implementation Handoff

Use when formal UI mockups are approved and implementation will follow. This absorbs the former `design-process-gates` responsibility into `idea-to-design`.

Must have:
- approved mockup refs in `state.json`
- `DESIGN.md` and `tokens.json`
- `visual-source-contract.json` with at least one approved mockup
- compact `page-style-briefs/<page-id>.md` for each core page that will be implemented
- `implementation-parity-checklist.md`
- `scripts/check-design-handoff.py` passes
- `state.json.implementation_gate.status = "open"`

Do not proceed to implementation if:
- mockups are approved but tokens are missing
- page briefs are missing for core pages
- implementation plan does not reference design tokens and visual source IDs
- `implementation_gate.status` is blocked and there is no explicit user waiver

If blocked:
- generate the smallest missing Level 3 artifact instead of expanding all docs
- keep page briefs short and link to global tokens
- record waivers explicitly if the user chooses to bypass a gate

---

## Implementation Parity Gate

After coding starts, each UI checkpoint must compare the implemented page against the approved mockup and page brief. Functional tests/builds alone are insufficient.

Minimum parity check:
- exact mockup/page brief identified
- mobile viewport screenshot captured
- header/navigation, first-screen density, card anatomy, and button hierarchy compared
- drift recorded as fixed, accepted deviation, user decision, or design debt

Development agents must not silently redesign approved mockups. If the design is impractical, create a design change request or design debt item.
