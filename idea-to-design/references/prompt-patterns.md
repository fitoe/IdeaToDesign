# Prompt Patterns

Use these patterns to keep image generation controlled and progressive.

Core rule:
- structure first
- style second
- refinement last

Do not ask image generation to invent product logic.

---

## 1. Text Wireframe Prompt

Use before image wireframes.

### Purpose
Turn page spec into a compact structural draft.

### Template

Page ID: [P-001]  
Page Name: [Page Name]  
Goal: [What user must accomplish here]  
Target user: [Who uses it]  
Primary CTA: [Main action]  
Main blocks:
- [Block 1]
- [Block 2]
- [Block 3]

Key states:
- default
- loading
- empty
- error
- success

Key interactions:
- [Interaction 1]
- [Interaction 2]

Constraints:
- prioritize clarity
- do not invent new features
- do not over-style
- focus on layout, hierarchy, and CTA placement
- use formal Chinese product copy for any human-facing labels
- do not use explanatory placeholders such as "这里是详情" or "这里展示数据"

Output:
- concise wireframe-style layout description
- clear hierarchy
- no decorative detail

---

## 2. Image Wireframe Prompt

Use for first visual pass after text wireframe is stable.

### Purpose
Generate low-fidelity structural page image.

### Template

Create a low-fidelity product wireframe for [product type].

Page:
- ID: [P-001]
- Name: [Page Name]

User goal:
- [Goal]

Layout blocks:
- [Block 1]
- [Block 2]
- [Block 3]

Primary CTA:
- [CTA]

Required states or elements:
- [State or element 1]
- [State or element 2]

Style constraints:
- grayscale or very minimal tone
- no final branding
- no decorative visuals
- focus on layout clarity and content hierarchy
- clear spacing and information grouping
- use formal Chinese UI copy where visible text is needed

Do not:
- invent additional features
- add unnecessary illustrations
- add polished marketing styling
- change page purpose

---

## 3. Mid-Fi Prompt

Use when structure is accepted and hierarchy is stable.

### Purpose
Add component direction, density, and visual rhythm without final polish.

### Template

Create a mid-fidelity product UI concept for [product type].

Page:
- ID: [P-001]
- Name: [Page Name]

Purpose:
- [Purpose]

Main blocks:
- [Block 1]
- [Block 2]
- [Block 3]

Interaction emphasis:
- [What must feel obvious]

Visual direction:
- [Tone keywords]
- [Principle 1]
- [Principle 2]

Color direction:
- [Primary]
- [Secondary]
- [Background behavior]

Component direction:
- [Buttons]
- [Cards]
- [Navigation]
- [Forms or data display]

Constraints:
- keep layout consistent with approved structure
- moderate polish only
- no extra product features
- support readability and clear CTA hierarchy
- use specific Chinese UI copy instead of placeholder explanations

Do not:
- radically change layout
- over-style empty space
- turn into final glossy mockup if hierarchy still needs review

---

## 4. Hi-Fi Prompt

Use only after structure and mid-fi direction are stable.

### Purpose
Generate polished concept visuals for final design reference.

### Template

Create a high-fidelity product UI screen for [product type].

Page:
- ID: [P-001]
- Name: [Page Name]

Purpose:
- [Purpose]

Main blocks:
- [Block 1]
- [Block 2]
- [Block 3]

Primary CTA:
- [CTA]

Visual brief:
- tone: [keywords]
- first impression: [feeling]
- context fit: [classic trusted / modern practical / warm lifestyle / bold editorial / experimental]
- one memorable move: [single distinctive design idea]
- freshness budget: [1-2 visual moves only]
- visual principles:
  - [Principle 1]
  - [Principle 2]
  - [Principle 3]

Design direction:
- color strategy: [Summary]
- typography direction: [Summary]
- component direction: [Summary]
- density: [compact / balanced / spacious]

Must preserve:
- approved structure
- clear content hierarchy
- obvious primary action
- consistency with product-wide design direction
- formal Chinese product copy across visible UI text
- project visual DNA and audience fit

Do not:
- introduce new flows
- introduce hidden product assumptions
- overcomplicate the screen
- prioritize beauty over usability
- use explanatory placeholder labels in visible UI
- fall back to generic hero-plus-three-cards templates
- use decorative gradients, glass, blobs, or 3D objects without product purpose

---

## 5. Refinement Prompt

Use after a review round. Change one main goal only.

### Purpose
Refine without destabilizing the whole page.

### Template

Refine this page design.

Page:
- ID: [P-001]

Keep:
- [Thing 1]
- [Thing 2]

Change:
- [Single main goal]

Improve:
- [Specific issue]

Do not change:
- page structure
- page purpose
- CTA position unless explicitly requested
- established visual direction
- approved formal UI copy unless refinement target is copy itself

If tradeoff appears:
- prioritize [clarity / hierarchy / density / CTA / readability]

---

## 6. Direction Exploration Prompt

Use before committing to one visual direction.

### Purpose
Generate 2-3 distinct but plausible visual directions.

### Template

Explore [2 or 3] visual directions for a [product type] product.

Shared product context:
- target users: [Users]
- core feeling: [Feeling]
- product goal: [Goal]

Generate distinct directions:
- Direction A: [description]
- Direction B: [description]
- Direction C: [description]

For each direction, vary:
- density
- tone
- emphasis style
- color behavior
- component feel
- composition
- material language
- typography rhythm

Variation rule:
- each direction must differ in at least 2-3 of composition, material, density, color strategy, typography rhythm, component shape, or visual hook
- do not create three versions that only change colors or adjectives

Keep constant:
- overall page purpose
- main content blocks
- core CTA logic

Do not:
- invent different products
- change structure between directions more than necessary

---

## 7. Negative Constraint Patterns

Useful phrases:
- do not invent new features
- do not alter page purpose
- do not add extra navigation levels
- do not over-decorate
- do not use excessive gradients
- do not reduce readability for style
- do not create a marketing page if this is a workflow page
- do not make the design feel game-like unless explicitly desired

---

## 8. Prompt Writing Rules

Always include:
- page purpose
- user goal
- main blocks
- primary CTA
- current fidelity target
- visual constraints
- context fit and audience fit
- one memorable move for core pages
- explicit "do not" items
- visible copy should be real Chinese product wording, not structural annotations

Avoid:
- vague adjectives only
- giant all-in-one prompts
- mixing structure changes with polish changes
- asking for multiple major changes in one round

---

## 9. Fidelity Rules

### L1
Text wireframe only

### L2
Image wireframe
- low visual noise
- structure review only

### L3
Mid-fi
- hierarchy and component direction review

### L4
Hi-fi
- polish and cohesion review

Do not skip levels unless page is trivial or already well-defined.
