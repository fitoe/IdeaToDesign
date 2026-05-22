# Domain Visual Risk Packs

Use this reference with `high-quality-visual-prompt-protocol.md` when generating design-source prompts for regulated, factual, trust-sensitive, or domain-specific pages.

The goal is not to make prompts timid. The goal is to keep the visual distinctive while preventing the image model from inventing unsafe facts, fake authority, or off-domain aesthetics.

## How to Use

1. Identify the domain and trust mode.
2. Apply the matching risk pack before writing the final prompt.
3. Add forbidden invented content to the Content Evidence Ledger.
4. Translate domain risk into positive design choices, not only negative bans.
5. If multiple domains apply, combine the strictest factual constraints.

Recommended final prompt clause:

```md
Domain constraints:
- Use [trust mode] rather than [off-domain style].
- Do not invent [people / credentials / metrics / maps / logos / claims].
- Prefer [safe visual language].
```

## Universal Factual Safety Pack

Use for any real company, institution, product, person, service, location, metric, case study, pricing, certification, or testimonial.

### Do not invent

- people names, staff portraits, titles, uniforms, badges, or photos;
- license numbers, certificates, awards, government approvals, or insurance status;
- maps, exact addresses, branch locations, routes, or emergency coverage;
- customer logos, partner logos, user counts, revenue, success rates, reviews, rankings;
- product specs, prices, discounts, guarantees, warranties, medical/legal/financial outcomes;
- screenshots of real software states unless provided;
- QR codes, barcodes, seals, signatures, or official emblems unless provided.

### Prefer

- abstract diagrams;
- symbolic icons;
- service-path visuals;
- neutral cards and lists with short placeholder labels;
- real provided copy only;
- generic role labels such as “服务团队” / “咨询顾问” only if safe for the project.

## Healthcare / Medical / Hospital / Clinic

### Trust mode

Institutional + service-led + patient-friendly.

### Safe visual language

- calm, clean, accessible, warm, organized;
- soft service-path diagrams, care journey lines, department/service cards;
- abstract medical symbols, appointment flow, patient guidance modules;
- restrained colors: white, soft blue/green, warm neutrals, gentle accents;
- high readability, clear CTAs, strong contact/appointment hierarchy.

### Do not invent

- doctor portraits, names, titles, departments, expert claims;
- treatment outcomes, cure rates, before/after images;
- medical licenses, insurance coverage, official certifications;
- emergency capability, ambulance, 24-hour claims, maps, hospital scale;
- patient testimonials, photos, case studies, star ratings;
- medical-device specs or procedure details not provided.

### Avoid aesthetics

- SaaS dashboard / cyber / dark neon / finance-tech style;
- luxury spa style that weakens medical trust;
- dramatic surgery imagery, blood, needles, or disease photos;
- fake hospital photography.

### Positive prompt clause

```md
Use an institutional and service-led healthcare visual system: clear appointment/service paths, soft medical geometry, calm blue-green accents, generous readability, and abstract care-flow illustrations. Do not show fake doctors, patients, certificates, maps, treatment claims, emergency claims, or medical outcomes.
```

## Government / Public Service

### Trust mode

Institutional + public-service + task-led.

### Safe visual language

- service hall, task-flow cards, public information modules;
- structured grids, clear status labels, accessible typography;
- civic colors used with restraint;
- inclusive, neutral, non-partisan imagery.

### Do not invent

- official seals, flags, emblems, signatures, stamps;
- government approvals, policy claims, legal interpretations;
- named officials, departments, addresses, phone numbers;
- emergency notices, deadlines, benefits, eligibility results;
- maps or jurisdiction boundaries unless provided.

### Avoid aesthetics

- campaign/political advertising style;
- crypto/fintech dashboards;
- over-luxury or entertainment tone;
- dark hacker/cyber visuals unless the service is explicitly cybersecurity.

### Positive prompt clause

```md
Use a calm public-service visual system with task-flow cards, accessible typography, and institutional clarity. Do not invent official seals, stamps, policy claims, named officials, maps, deadlines, or legal eligibility details.
```

## Finance / Insurance / Investment / Payments

### Trust mode

Evidence-led + compliance-aware + clarity-first.

### Safe visual language

- clear plans, calculators as abstract modules, secure transaction paths;
- stable grids, conservative color accents, strong readability;
- risk-awareness and disclosure-friendly layout;
- avoid implying guaranteed returns.

### Do not invent

- returns, APY, profits, rates, rankings, portfolio performance;
- bank licenses, regulatory approvals, insurance coverage;
- real payment cards, account numbers, transaction data;
- customer logos, testimonials, investment advice;
- “guaranteed”, “risk-free”, or “best” claims.

### Avoid aesthetics

- casino/gambling energy;
- meme-crypto neon;
- fake trading dashboards with green profit numbers;
- over-promising luxury wealth imagery.

### Positive prompt clause

```md
Use a compliance-aware finance visual system: stable grids, clear comparison modules, restrained accents, and risk-conscious hierarchy. Do not invent returns, rates, rankings, licenses, payment data, testimonials, or guaranteed outcome claims.
```

## Manufacturing / Industrial / Hardware / Tools

### Trust mode

Product-led + evidence-led + capability-focused.

### Safe visual language

- precision grid, product matrix, material texture, process chain;
- quality-control steps, engineering diagrams, production capability modules;
- robust typography, clean industrial spacing, strong product category hierarchy;
- real product images if provided; otherwise abstract product silhouettes or neutral icons.

### Do not invent

- factory photos, workers, equipment, production lines;
- certifications, export countries, volumes, patents, test reports;
- exact material grades, tolerances, standards, prices;
- customer logos, distributor networks, shipping promises;
- safety/compliance claims unless provided.

### Avoid aesthetics

- generic SaaS dashboard if the business sells physical products;
- soft lifestyle ecommerce that hides product capability;
- fake glossy 3D product renders that cannot be implemented or sourced;
- cluttered catalog walls with unreadable tiny labels.

### Positive prompt clause

```md
Use a product-led industrial visual system: precision grid, product category matrix, process-chain rhythm, material-aware neutrals, and evidence-led hierarchy. Do not invent factory scenes, certificates, export claims, production volumes, patents, exact specs, or customer logos.
```

## SaaS / Enterprise Software / AI Tools

### Trust mode

Product-led + workflow-led + evidence-led.

### Safe visual language

- workflow loop, data pipeline, automation path, workspace timeline;
- UI fragments only if representational or provided;
- clear feature hierarchy and implementation-feasible components;
- restrained gradients, layered cards, strong layout rhythm.

### Do not invent

- real customer names/logos, case-study metrics, user counts;
- exact dashboard data, revenue numbers, model benchmarks;
- security certifications, compliance badges, uptime claims;
- integrations unless provided;
- fake chat outputs that imply unsupported product behavior.

### Avoid aesthetics

- meaningless dashboard wallpaper;
- overused glassmorphism and floating cards without information hierarchy;
- AI cliché overload: robot faces, magic sparkles, brain clouds, neon circuits;
- tiny unreadable charts.

### Positive prompt clause

```md
Use a product-led SaaS visual system with workflow paths, readable interface fragments, layered but disciplined cards, and clear feature-to-action hierarchy. Do not invent customer logos, metrics, integrations, certifications, exact dashboard data, or unsupported AI outputs.
```

## AI / Automation Services

Use this pack in addition to SaaS when AI capability is central.

### Trust mode

Capability-led + human-in-control + outcome-aware.

### Safe visual language

- automation paths, review checkpoints, human approval nodes;
- prompt/result pipelines, knowledge graph motifs, process orchestration;
- show AI as a system capability, not magic.

### Do not invent

- benchmark scores, model names, evaluation results;
- autonomous guarantees, compliance guarantees, replacement claims;
- fake generated outputs that look like real customer data;
- privacy/security claims unless provided.

### Avoid aesthetics

- humanoid robots as the main visual unless requested;
- mystical magic language;
- dark sci-fi hacker style for business automation;
- overclaiming “fully autonomous” if humans remain involved.

## Ecommerce / Retail / Marketplace

### Trust mode

Product-led + conversion-led + service-assurance.

### Safe visual language

- curated category islands, product wall, shopping path;
- strong product imagery if provided, otherwise neutral placeholders;
- clear price/contact/availability states only if factual;
- delivery/returns/customer service modules only if provided.

### Do not invent

- prices, discounts, stock levels, delivery dates;
- reviews, ratings, sales counts, bestseller tags;
- brand logos, product photos, SKU details;
- guarantees, return windows, free shipping claims;
- payment badges unless actually supported.

### Avoid aesthetics

- fake luxury if products are practical/industrial;
- cluttered marketplace density for premium/boutique experiences;
- unreadable product cards;
- lifestyle photography without provided assets.

### Positive prompt clause

```md
Use a product-led ecommerce visual system with curated category structure, readable product cards, and clear conversion paths. Do not invent prices, discounts, stock, reviews, delivery promises, payment badges, product photos, or brand logos.
```

## Education / Training / Knowledge Products

### Trust mode

Learning-path + credibility-led + approachable.

### Safe visual language

- curriculum map, progress ladder, learning journey;
- instructor/course cards only with verified facts;
- calm, optimistic colors, readable modules;
- knowledge structure diagrams.

### Do not invent

- instructor names, degrees, school affiliations;
- certificates, accreditation, job-placement rates;
- course counts, student counts, ratings, outcomes;
- pricing, deadlines, admissions claims;
- testimonials or employer logos.

### Avoid aesthetics

- childish style for professional training;
- fake university prestige signals;
- too much gamification if trust and credibility matter;
- crowded course marketplace layouts unless requested.

### Positive prompt clause

```md
Use a learning-path visual system with curriculum maps, progress rhythm, and credible approachable typography. Do not invent instructors, degrees, certificates, accreditation, student counts, ratings, job outcomes, or testimonials.
```

## Real Estate / Architecture / Local Services

### Trust mode

Location-aware + service-led + evidence-aware.

### Safe visual language

- service process, neighborhood/service cards, contact modules;
- real photos only if provided;
- abstract location motifs rather than fake maps;
- practical trust cues: consultation steps, service scope, FAQ structure.

### Do not invent

- property photos, addresses, maps, prices, availability;
- licenses, awards, sales volume, agent names;
- customer reviews, rankings, neighborhood claims;
- before/after project photos unless provided.

### Avoid aesthetics

- fake luxury property renderings;
- misleading map pins;
- unrealistic lifestyle imagery;
- official-looking badges without evidence.

## Nonprofit / Community / Charity

### Trust mode

Mission-led + transparency-led + human-sensitive.

### Safe visual language

- mission flow, impact areas, donation path, volunteer journey;
- abstract community illustrations;
- warm, respectful, non-exploitative imagery;
- clear transparency modules.

### Do not invent

- beneficiary photos/stories;
- donation amounts, impact numbers, partnerships;
- legal charity status, audits, certifications;
- crisis claims or emergency appeals;
- testimonials.

### Avoid aesthetics

- poverty porn or sensational imagery;
- manipulative emotional visuals;
- fake photos of vulnerable people;
- over-polished corporate tone if it weakens authenticity.

## Legal / Professional Services

### Trust mode

Expert-led + discretion-led + clarity-first.

### Safe visual language

- consultation path, service scope cards, document/process motifs;
- reserved typography and color;
- structured FAQ and contact hierarchy.

### Do not invent

- lawyer names, bar licenses, case outcomes;
- legal guarantees, win rates, awards;
- client logos, testimonials;
- jurisdiction-specific advice;
- official seals or court imagery implying affiliation.

### Avoid aesthetics

- aggressive litigation advertising;
- fake courthouse photos;
- over-luxury prestige signals;
- tiny legal text inside generated images.

## Domain-Fit Checklist

Before final generation, answer:

- Does the trust mode match the domain?
- Are all factual claims confirmed or removed?
- Are fake people/photos/logos/metrics banned where needed?
- Is the visual hook domain-derived rather than decorative?
- Are off-domain aesthetics explicitly avoided?
- Does the prompt define safe alternatives, not only prohibitions?
- Is the page still distinctive after safety constraints?

If the answer to the last question is no, strengthen the One Memorable Move and Page Narrative Map instead of relaxing factual safety.
