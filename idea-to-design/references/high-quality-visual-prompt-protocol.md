# High-Quality Visual Prompt Protocol

## Core Principle

High-quality visual prompts are compiled from design decisions, not written as long wishlists.

Before writing the final image prompt, decide:

- who must trust this page or screen;
- what must be understood first;
- what the single memorable visual move is;
- what real content is safe to show;
- what the image model must not invent;
- what canvas, board type, and maturity level are required.

Then compile those decisions into the final prompt. Do not start by piling adjectives or copying a long generic template.

## When to Use

Use this protocol before generating any user-facing design source that must be more than a rough draft, especially:

- homepage or landing page visuals;
- brand-defining pages or hero sections;
- key visual approval boards;
- generated design sources for downstream DesignToCode work;
- regulated, factual, or trust-sensitive domains;
- any image where the target maturity is `distinctive` or `excellent`.

Do not use the full protocol for trivial internal sketches. For ordinary secondary pages, use a compressed version: Brief Card + Content Evidence Ledger + Canvas Contract + Prompt Lint.

## Maturity Target

Always set a maturity target before writing the prompt.

| Target | Meaning | Use |
|---|---|---|
| `generic` | Template-like, ordinary, no memorable move | Reject for core pages |
| `competent` | Clear and usable but not distinctive | Support pages, utility pages |
| `distinctive` | Credible domain fit with a clear visual hook | Minimum for homepage/key pages |
| `excellent` | Strong craft, strong hierarchy, memorable, feasible | Brand-defining visuals |

Core pages must target at least `distinctive`. If the prompt does not explain how the result avoids generic templates, revise it before generation.

## Prompt Compiler Flow

Produce these decisions, then compile the final prompt.

### 1. Prompt Brief Card

```md
Prompt Brief Card

Page / screen:
Output type:
Canvas contract:
Target maturity:
Audience:
Primary user goal:
Business / project goal:
Trust context:
Primary CTA or next action:
Hard constraints:
```

### 2. Design DNA Card

Define design principles, not brand imitation.

```md
Design DNA Card

Brand feeling:
Audience expectation:
Whitespace behavior:
Typography rhythm:
Color behavior:
Component personality:
Imagery / illustration style:
Motion or depth implication if relevant:
Styles that would conflict with trust:
```

If using references, translate each reference into one borrowed principle and one non-borrowed boundary.

```md
Reference Translation

Apple
- Borrow: spatial discipline, large type, section-as-scene rhythm.
- Do not borrow: product-launch minimalism so extreme that service content disappears.

Stripe
- Borrow: controlled layered gradients and energetic information architecture.
- Do not borrow: SaaS dashboard language for non-SaaS institutions.
```

Rules:

- Use at most 3 reference sources.
- Each reference may contribute only 1-2 dimensions.
- Reference brands are design principles, not imitation targets.

### 3. Content Evidence Ledger

Use for any real organization, real product, regulated claim, people, pricing, credential, map, metric, or customer proof.

```md
Content Evidence Ledger

Confirmed facts:
- name:
- contact:
- location:
- services / products:
- people / roles:
- credentials / claims:
- safe titles / labels:

Allowed illustrative content:
- abstract icons:
- symbolic diagrams:
- generic non-human illustrations:
- generated backgrounds:

Forbidden invented content:
- names:
- titles:
- photos:
- certificates:
- numbers:
- maps:
- reviews:
- success claims:
- customer logos:
```

Do not let the image model invent factual material. If facts are missing, use abstract or symbolic visuals instead of fake specifics.

### 4. One Memorable Move

Every homepage, landing page, brand-defining page, and key approval image needs one main visual hook.

```md
One Memorable Move

Name:
Purpose:
How it supports the page:
Where it appears:
How to keep it subtle:
What it must not become:
```

The memorable move should create page order, not random decoration.

Examples:

| Domain | Possible memorable move |
|---|---|
| Healthcare | guided care path, soft clinic/service nodes, health journey line |
| Manufacturing | precision grid, product matrix wall, process chain, material section cut |
| SaaS | workflow loop, automation path, data pipeline, workspace timeline |
| Education | learning path, growth ladder, curriculum map |
| Government | service hall path, public-service grid, task-flow cards |
| Ecommerce | curated product wall, category islands, purchase path |

Do not reuse a previous project's memorable move by default. Derive it from the name, domain, audience, primary action, strongest content asset, or brand metaphor.

### 5. Page Narrative Map

Do not only list modules. Define narrative rhythm and visual weight.

```md
Page Narrative Map

Above the fold:
- first impression:
- main trust signal:
- primary action:
- visual weight:

Section 2:
- user need served:
- density:
- visual treatment:

Section 3:
- proof / service / product value:
- density:
- visual treatment:

Section 4:
- supporting content:
- density:
- visual treatment:

Final section:
- conversion / contact / next step:
- tone:
```

This tells the model where to be dramatic, where to be quiet, and where to prioritize usability.

### 6. Information Priority Ladder

```md
Information Priority Ladder

P0 — visible immediately above the fold:
P1 — must appear and be easy to find:
P2 — supporting content:
P3 — omit from the image prompt or defer to implementation docs:
```

Avoid putting P3 content into generated images. Move detailed copy, long policies, legal detail, and exhaustive lists into implementation/content docs.

### 7. Visual Variables

Select variables explicitly.

```md
Visual Variables

Composition: centered hero / split hero / editorial grid / product wall / service path / dashboard shell
Density: sparse / balanced / compact
Color behavior: restrained mono-accent / soft gradient / multi-zone palette / editorial contrast
Image behavior: abstract illustration / symbolic diagram / product photography / screenshot collage / no image
Component shape: sharp / soft rounded / pill / card-heavy / list-heavy
Trust mode: institutional / expert-led / evidence-led / service-led / community-led / brand-led / product-led
Conversion mode: CTA-led / information-led / consultation-led / content-led
```

Match trust mode to domain. For example, local hospitals are usually `institutional + service-led`; B2B manufacturing is often `evidence-led + product-led`; SaaS is often `product-led + evidence-led`.

### 8. Canvas Contract

Always specify what the image should look like as a deliverable.

```md
Canvas Contract

Canvas:
- desktop full-page website screenshot, 1440px-wide feel; or
- mobile phone screen, 390px CSS-width feel; or
- hero-only crop; or
- design board with two complete pages; or
- three complete mobile phone states.

Rules:
- no browser chrome unless requested;
- no cropped approval sections;
- no half-page preview as the only approval artifact;
- keep text readable at the requested board scale.
```

Use a single full-page image for homepages and key pages. Use two-page desktop boards only for secondary pages that remain readable. Use up to about three phone states for mobile/H5 flows when each state is complete.

### 9. Asset Strategy

```md
Asset Strategy

Use:
- provided real images:
- generated abstract illustration:
- symbolic icons:
- product screenshots:
- no people / no maps / no photos:

Implementation feasibility:
- prefer reusable components;
- prefer CSS-buildable backgrounds, gradients, cards, and icons;
- avoid impossible 3D scenes unless assets will be generated separately;
- distinctive does not mean hard to implement.
```

If no real photo assets exist, explicitly ban fake photos and use abstract or symbolic visuals.

## Typography, Spacing, and Copy Density

### Typography Floor + Spacing Coupling

When asking for larger text, also require:

- larger card padding;
- increased line-height;
- fewer words per card;
- stronger section spacing;
- lower information density.

Do not only increase font size. Bigger text without spacing and density changes makes the page feel cramped.

### Copy-to-Visual Compression

Generated images should not carry full content documents.

Rules:

- Hero: 1 headline + 1 subtitle + 1 short paragraph + 1-2 CTAs.
- Card: 1 title + at most 1 short sentence.
- News/list item: title only or title + very short metadata.
- Footer: factual contact/legal/navigation only.
- Long paragraphs, policies, detailed descriptions, and exhaustive lists belong in implementation docs, not image prompts.

## Prompt Budget

Balance the final prompt:

- 30% design intent and audience;
- 20% composition and narrative rhythm;
- 20% real content and section binding;
- 15% typography / spacing / component system;
- 15% negative constraints and safety.

If the prompt is mostly a content dump, the image will likely look cluttered. If it is mostly style adjectives, the image will likely hallucinate content or become generic.

## Model-Friendly Final Prompt Order

Compile the final prompt in this order:

1. Output type and canvas.
2. Project identity.
3. Audience and goal.
4. Visual maturity target.
5. Design DNA.
6. One Memorable Move.
7. Page Narrative Map.
8. Required content and content boundaries.
9. Typography and spacing rules.
10. Component and asset strategy.
11. Domain-specific safety constraints.
12. Negative constraints.

Do not start the final prompt with a giant list of all content. The model should understand the design direction before it sees section-level details.

## Prompt Lint

Reject or revise the prompt before image generation if any of these are true:

- more than 3 style references;
- references are named but not translated into concrete principles;
- no one memorable move;
- no page narrative map;
- no content evidence ledger for real/factual domains;
- no canvas contract;
- asks for many long paragraphs inside the image;
- says only “modern / premium / clean / high-end” without concrete visual rules;
- asks for exact real people, maps, certificates, logos, numbers, or photos without provided assets;
- asks for a full-page image but also demands too many small details;
- mixes desktop and mobile requirements in one image;
- asks for larger text without spacing/density adjustments;
- decoration competes with trust, readability, or CTA clarity.

## Refinement Rule

Each refinement prompt should optimize one main variable.

Good:

- Make the page more spacious while preserving structure and content.
- Increase color richness without changing layout.
- Make typography larger and reduce card copy density.

Bad:

- Make it more premium, colorful, spacious, lively, modern, and change the layout.

If multiple issues exist, choose the most product-breaking one first.

## Second-Pass Prompt Repair

| Symptom | Repair |
|---|---|
| Too generic | Strengthen One Memorable Move and composition |
| Too decorative | Make the visual hook serve structure; reduce ornament |
| Too colorful | Define color roles and reduce palette count |
| Too dense | Reduce copy density; increase spacing and card padding |
| Text too small | Apply typography floor plus spacing coupling |
| Off-domain style | Re-select trust mode and add industry visual禁区 |
| Fake content risk | Tighten Content Evidence Ledger and forbidden inventions |
| Visual feels scattered | Reduce references; reinforce Design DNA |
| Hard to implement | Add implementation feasibility filter and asset strategy |
| CTA unclear | Rework Page Narrative Map and action hierarchy |

## Anti-Patterns

Avoid:

- giant wishlist prompts with no design decisions;
- “make it like Apple/Stripe/Linear” without saying what to borrow;
- mixing too many style systems;
- generic hero + three cards as the whole concept;
- random 3D objects, blobs, waves, glass, or neon gradients with no product purpose;
- fake dashboards with meaningless metrics;
- fake doctors, fake maps, fake reviews, fake certificates, fake customer logos;
- long Chinese paragraphs in generated images;
- image prompts that double as full requirements documents.

## Stop Adding Detail

Stop adding prompt detail when:

- visual DNA is clear;
- page narrative is clear;
- content boundaries are clear;
- one memorable move is clear;
- typography/density rules are clear;
- negative constraints cover the main risks.

Move remaining detail to content docs, implementation docs, Visual IR, or page contracts. The image prompt is not the full product specification.

## Final Prompt Skeleton

```md
Create a [canvas contract] for [project/page].

This is for [audience] who need to [primary user goal]. The page must create [trust context] and guide users toward [primary action]. Target visual maturity: [distinctive/excellent], not a generic template.

Design DNA:
- [principle 1]
- [principle 2]
- [principle 3]

One memorable move:
- [name and purpose]
- It should appear in [locations] and support [hierarchy/navigation/trust].
- It must not become [risk].

Page narrative:
- Above the fold: [first impression, trust signal, CTA, visual weight]
- Section 2: [need, density, treatment]
- Section 3: [proof/value, density, treatment]
- Section 4: [supporting content, density, treatment]
- Final section: [next step, tone]

Use only these confirmed facts:
- [facts]

Allowed illustrative content:
- [abstract/symbolic assets]

Forbidden invented content:
- [domain risks]

Typography and spacing:
- [type scale]
- [line-height / padding / density rules]
- [copy density rules]

Components and assets:
- [buttons/cards/icons/images]
- [asset strategy]
- [implementation feasibility]

Negative constraints:
- [anti-slop]
- [off-domain style constraints]
- [safety constraints]
```
