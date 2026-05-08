# Review Checklists

Use these checklists to keep reviews short, useful, and decision-oriented.

Main rule:
- review for decisions, not for commentary volume

---

## 1. Scope Review

Use after early discovery.

Check:
- Is product goal clear?
- Is target user clear?
- Is current scope narrow enough?
- Is at least one non-goal stated?
- Is there one primary task worth designing first?

If any answer is no:
- do not move on

---

## 2. Structure Review

Use before visual direction.

Check:
- Are core task flows explicit?
- Do pages belong to clear flows?
- Are core pages separated from supporting pages?
- Does each core page have a purpose?
- Is there a sane entry and exit path?
- Is scope still manageable?

Reject if:
- pages feel disconnected
- too many pages are treated as equally important
- structure still depends on unknown business logic

---

## 3. Design Brief Review

Use before image-heavy work.

Check:
- Is tone clear?
- Is `Creative Direction Summary` present?
- Is context fit explicit?
- Is audience fit explicit?
- Is there one memorable move for each core page or core visual direction?
- Are visual principles concrete?
- Is color strategy defined enough to guide consistency?
- Is component direction defined enough to prevent drift?
- Are "do not use" constraints present?
- Would two different screens still look like same product?

Reject if:
- brief is only adjectives
- no component guidance exists
- visual direction is still multiple unresolved directions
- the direction defaults to generic SaaS, dashboard, or landing-page templates without a product reason

---

## 4. Text Wireframe Review

Use before image wireframes.

Check:
- Is page purpose obvious?
- Are main blocks in right order?
- Is primary CTA clear?
- Is hierarchy logical?
- Are key states acknowledged?
- Are key interactions represented structurally?

Reject if:
- layout is still solving product logic
- CTA placement is arbitrary
- content blocks are too vague

---

## 5. Wireframe Review

Use before mid-fi.

Check:
- Does image match approved structure?
- Are blocks grouped clearly?
- Is primary action discoverable?
- Is content density reasonable?
- Are there any invented features?

Reject if:
- image changed page purpose
- major layout confusion remains
- decorative choices distract from structure

---

## 6. Mid-Fi Review

Use before hi-fi.

Check:
- Is information hierarchy strong?
- Are components consistent?
- Is visual rhythm coherent?
- Is CTA hierarchy clear?
- Does page feel aligned with design brief?
- Are unresolved issues local rather than structural?

Reject if:
- layout still needs large changes
- component language is unstable
- page feels like a different product from other pages

---

## 7. Hi-Fi Review

Use before finalizing.

Check:
- Is visual direction cohesive?
- Does the page pass `Aesthetic Review` if it is a core page?
- Is maturity at least `distinctive` for core pages?
- Is readability preserved?
- Is polish serving function?
- Does design still match approved structure?
- Are key states still understandable?
- Is this good enough for implementation reference?

Reject if:
- aesthetics hide usability issues
- key interactions are unclear
- polish introduced ambiguity
- the page feels generic, outdated, or AI-template-like

---

## 7.5 Aesthetic Review

Use before accepting core-page high-fidelity visuals.

Check:
- Does the design fit product context and audience taste?
- Is there one clear memorable move?
- Is visible content realistic and product-ready?
- Does it avoid generic hero-plus-three-cards, empty dashboards, decorative blobs, cheap glass, and meaningless gradients?
- Does it preserve visual DNA without copying the previous page composition mechanically?
- Can it be implemented without disproportionate complexity?

Reject if:
- result is `generic` on the maturity ladder
- novelty harms readability, trust, or task completion
- traditional projects look old or rough instead of refined and credible

---

## 8. Page Spec Review

Use on each important page.

Check:
- Is purpose clear in one sentence?
- Are main blocks listed?
- Is primary CTA identified?
- Are key states listed?
- Are key interactions captured?
- Are implementation notes minimal but sufficient?

Reject if:
- spec repeats image without adding useful meaning
- states are missing
- interactions depend on guesswork

---

## 8.5 Content Realism Review

Use on all human-facing copy.

Check:
- Does title text read like real product copy?
- Do buttons use real actions instead of placeholder descriptions?
- Do cards, forms, and empty states avoid structural explanation text?
- For core pages, does visible copy feel close to production-ready?
- For supporting pages, is the wording still user-facing rather than annotation-like?

Reject if:
- copy says things like "这里是详情", "这里展示数据", "按钮文案", "用户信息区域"
- labels describe structure instead of user meaning
- text reads like designer notes rather than product copy

---

## 9. Final Document Review

Use before shipping `Design-Spec.md`.

Check:
- Is the document readable end-to-end?
- Does overview explain scope quickly?
- Are core flows and pages easy to find?
- Are images paired with right pages?
- Are supporting pages compressed enough?
- Are implementation notes practical?
- Are unresolved items explicitly marked?
- Is process noise excluded?

Reject if:
- document feels like archive dump
- too many pages are over-documented
- reader must inspect working files to understand product

---

## 10. Designer-Friendly Compression Check

Use on final pass.

Check:
- Would a designer actually read this?
- Is there one obvious main doc?
- Are core pages emphasized more than minor pages?
- Are explanations short and decision-focused?
- Are repeated patterns collapsed instead of restated?
- Is the document lighter than the working process behind it?

If no:
- compress harder
- move process notes to background
- shorten non-core page sections

---

## 11. Developer Handoff Check

Use before completion.

Check:
- Can developer identify page IDs quickly?
- Can developer understand page purpose without guessing?
- Are main blocks and CTA clear?
- Are key states covered?
- Are responsive or implementation risks called out when needed?
- Can developer map images to page specs?

If no:
- add only missing operational clarity
- do not bloat prose

---

## 12. One-Question Review Pattern

When asking user for feedback, prefer one focused question:
- Is structure correct?
- Is density too high or about right?
- Should this page move to higher fidelity?
- Is CTA emphasis strong enough?
- Does this feel too formal or too playful?

Avoid:
- "What do you think?"
- multi-topic review prompts
- vague requests for broad feedback
