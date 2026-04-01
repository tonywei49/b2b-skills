---
name: hidden-buyer-scout
description: Search for non-obvious cross-industry B2B buyers in a target country based on usage scenarios, buying logic, and bulk-purchase signals.
homepage: https://github.com/tonywei49/b2b-skills
user-invocable: true
metadata: {"openclaw":{"emoji":"🔎","homepage":"https://github.com/tonywei49/b2b-skills","always":true}}
---

# Hidden Buyer Scout

## Purpose

Use this skill to find **non-obvious potential buyers** in a target country or region.

This skill is **not** for finding only traditional distributors, importers, or wholesalers that already sell the user's product category.

This skill is for identifying companies or organizations that may have **real bulk purchasing demand** even when the product is **not part of their core catalog**.

Examples:
- hotels or resorts that may purchase balls for kids clubs or recreation programs
- schools or education groups that may purchase sports items for classes or activities
- event companies that may purchase products as campaign materials or giveaways
- rehabilitation centers that may use balls as therapy or training tools
- shopping malls, camps, or family entertainment operators that may need activity equipment

The goal is to help the user discover **hidden demand**, **cross-industry buyers**, and **alternative purchasing paths**.

---

## When To Use This Skill

Use this skill when the user asks things like:
- find non-obvious buyers for this product in Saudi Arabia
- search cross-industry customers for children's balls in UAE
- who else may bulk buy this product besides sports distributors
- build a hidden buyer list for this product in Germany
- find institutional buyers or scenario-based buyers in Japan

Use this skill when the user already knows the product and country, and wants a **buyer list** from a **different angle than normal industry matching**.

Do **not** use this skill if the user only wants:
- traditional distributors only
- manufacturers only
- a pure importer / wholesaler list
- a simple company directory scrape without reasoning

For those cases, a normal B2B distributor scouting skill is more suitable.

---

## Interaction Rules

This skill should use **at most 2 user interactions** before final lead generation.

### Interaction 1: Fill Missing Core Inputs

If the initial request is missing critical information, ask for only the missing essentials:
- `product`
- `target_country`
- preferred hidden buyer angle, only if necessary

If the user already provided enough information, skip this interaction.

### Interaction 2: Buyer-Direction Confirmation

Before searching for companies, generate a short **buyer-direction analysis** and ask the user to confirm the search direction.

This second interaction should include:
- the most promising buyer segments
- why each segment may purchase in volume
- likely usage scenarios
- which directions look strongest vs weaker
- a recommended search focus

Then ask the user whether to:
- search all suggested directions
- search only selected directions
- adjust the direction before search

Only after user confirmation should the skill run company-level search and output the final lead list.

Do not exceed 2 interactions unless the user explicitly changes scope mid-task.

---

## Required Inputs

Before searching, confirm or infer these fields:

- `product`: what is being sold
- `target_country`: country or market to search
- `target_count`: desired number of companies, optional, default `15`
- `candidate_segment`: target cross-industry segment
- `usage_scenario`: where or how the product may actually be used
- `buying_logic`: why this segment may purchase in volume
- `buyer_type`: one of `end_buyer`, `institutional_buyer`, `procurement_intermediary`, `project_based_buyer`
- `priority`: `high`, `medium`, or `low`

If the user does not provide all fields, infer a reasonable version from context and continue.

---

## Buyer Hypothesis Step

Before searching companies, generate **3 to 8 buyer hypotheses**.

Each hypothesis should include:
- `candidate_segment`
- `usage_scenario`
- `buying_logic`
- `buyer_type`
- likely purchase frequency
- likely purchase route
- why this segment may buy in volume

Search each hypothesis separately and merge results later.

Do not jump directly from product name to company search without first forming buyer hypotheses.

---

## Search Mindset

Do not think like a category directory scraper.

Think in this order:

1. What kind of organization may actually use this product?
2. In what scenario would they use it?
3. Would usage imply repeated or bulk purchasing?
4. Is this organization likely to purchase directly, through procurement, or through project suppliers?
5. What evidence on their website or reliable sources suggests this demand is plausible?

Search for **buyer possibility**, not just keyword overlap.

---

## Buyer Direction Analysis Rules

During the second interaction, generate a broad but commercially logical list of possible buyer segments.

Do not restrict thinking to traditional industry categories.

Think expansively across:
- functional use
- environmental use
- emotional use
- institutional use
- event use
- bundled-service use
- gifting use
- therapeutic use
- educational use
- symbolic or promotional use

A segment may be proposed even if it is unconventional, as long as:
1. there is a plausible usage scenario
2. there is a plausible buying reason
3. there is a plausible purchasing path
4. the idea can be tested with real-world evidence

The goal is not to be conservative.
The goal is to produce high-upside buyer hypotheses that are commercially defensible.

### Output Structure for Interaction 2

The second interaction should group candidate directions into:

1. **Strong logic segments**
   High-confidence hidden buyer directions with clear bulk-purchase logic.

2. **Non-traditional but high-potential segments**
   Unusual directions that still have strong commercial logic.

3. **Experimental segments**
   Higher-variance directions worth testing on a smaller scale.

For every suggested segment, explain:
- why this type of entity may buy
- what scenario triggers the purchase
- who may own the purchase decision
- whether the demand is one-off, seasonal, or recurring

Do not list a segment without explaining the purchase logic.

---

## Search Strategy

Always search from multiple angles.

### Angle A: segment-first search
Search by company type or industry segment in the target country.

Examples:
- hotel group UAE
- resort operator Saudi Arabia
- rehabilitation center Germany
- school activity provider Japan
- event agency Dubai
- family entertainment center Malaysia

### Angle B: scenario-first search
Search by usage scenario instead of the product category.

Examples:
- kids club activities UAE
- recreation equipment supplier Saudi Arabia
- therapy training equipment Germany
- school PE activity procurement Japan
- promotional event merchandise UAE
- summer camp activity operator Malaysia

### Angle C: demand-signal search
Search for signals that suggest bulk or recurring purchases.

Examples:
- facilities
- programs
- children activities
- school programs
- camps
- therapy services
- procurement
- group packages
- recreation equipment
- activity center
- educational supplies
- events and giveaways

### Angle D: local-language search
When possible, search in both:
- English
- the main local language of the target market

Do not rely on English-only search if the country commonly uses another language.

### Angle E: adjacency search
Search neighboring solution categories where the product may appear as a supporting item.

Example for balls:
- physical training
- sensory play
- PE tools
- kids play equipment
- therapy exercise tools
- branded giveaways
- team building materials

### Angle F: use-case reverse search
Search how similar or adjacent products are used in the target market, then identify organizations behind those scenarios.

Examples:
- sensory play supplier school UAE
- therapy exercise tools rehabilitation center Germany
- kids activity equipment resort Saudi Arabia
- promotional sports giveaway event agency Dubai

---

## Candidate Types

Possible target entities include:

- hotel groups
- resorts
- schools
- education groups
- training centers
- therapy centers
- rehabilitation clinics
- camps
- family entertainment centers
- shopping malls with children facilities
- event agencies
- promotional merchandise firms
- corporate gifting suppliers
- project suppliers
- institutional procurement providers
- sports program operators
- community facility operators

Do not restrict the search to companies already selling the product.

---

## Inclusion Rules

A company may be included if there is enough evidence that:

1. it is a real organization
2. it operates in the target country or serves that market
3. its business model or facilities match the target segment
4. there is a plausible usage scenario for the product
5. there is a plausible bulk or repeated purchasing reason
6. there is at least one reliable source supporting the inference

Strong candidates have direct evidence such as:
- kids club or recreation facilities
- therapy or rehabilitation programs
- school or institutional operations
- events, gifting, or promotional procurement
- activity spaces or program packages
- repeated service delivery that requires supplies or equipment

Do not include a company based only on facility presence. A valid lead should have both:
- a plausible usage scenario
- an operational reason for repeated or bulk purchasing

---

## Exclusion Rules

Exclude candidates when:

- the company is unrelated to the scenario
- there is no plausible buying logic
- it is only a blog, media page, marketplace listing, or random directory entry without entity evidence
- it is clearly a manufacturer when the target buyer type is not manufacturer
- it is a duplicate of an already captured lead
- the company has no evidence of operating in the target market
- the product need is only incidental and there is no operational evidence of repeated purchasing

Do not include companies only because the keyword appears once on a page.

---

## Verification Rules

Prefer official or primary sources:
- official company website
- official about page
- official services page
- official facilities page
- official contact page
- LinkedIn company page
- official brochures or catalogs
- trusted business directories when primary sources are weak

For every lead, verify as many of these as possible:
- official company name
- website
- country / city
- segment match
- scenario match
- demand signal
- possible contact route
- source URL
- evidence URL

---

## Lead Fields

For each accepted lead, capture these fields when possible:

- `company_name`
- `country`
- `city`
- `website`
- `company_type`
- `buyer_type`
- `buyer_fit_type`
- `candidate_segment`
- `usage_scenario`
- `buying_logic`
- `why_possible_buyer`
- `bulk_purchase_signal`
- `evidence_type`
- `purchase_likelihood`
- `outreach_angle`
- `next_action`
- `contact_name`
- `contact_role`
- `email`
- `phone`
- `linkedin`
- `source_url`
- `evidence_url`
- `verification_status`
- `confidence_score`
- `notes`

If some contact fields are missing, still keep the lead if the buyer logic is strong.

### Field Notes

- `buyer_fit_type`: `direct_hidden_buyer`, `plausible_hidden_buyer`, `channel_proxy_buyer`, `weak_signal`
- `evidence_type`: `direct_program_evidence`, `facility_evidence`, `service_evidence`, `procurement_evidence`, `inferred_only`
- `purchase_likelihood`: `high`, `medium`, `low`
- `outreach_angle`: the most practical pitch angle or use case to open the conversation
- `next_action`: the next commercial step, such as contact operations manager, procurement team, program director, or partnership lead

---

## Scoring Rules

Score each lead from 0 to 100.

Suggested scoring dimensions:
- `industry_match` = 0 to 20
  - 20 = exact hidden-buyer segment fit
  - 10 = adjacent but commercially plausible
  - 0 = weak fit
- `scenario_match` = 0 to 20
  - 20 = direct and explicit use scenario
  - 10 = plausible but indirect scenario
  - 0 = weak scenario fit
- `buyer_signal` = 0 to 20
  - 20 = clear recurring or bulk purchase signal
  - 10 = partial or seasonal signal
  - 0 = no meaningful signal
- `contact_quality` = 0 to 20
  - 20 = strong named contact and route
  - 10 = partial route only
  - 0 = no useful contact signal
- `source_reliability` = 0 to 20
  - 20 = official primary evidence
  - 10 = mixed evidence
  - 0 = weak directory-only evidence

Interpretation:
- `80-100` = strong hidden buyer candidate
- `60-79` = plausible candidate worth review
- `40-59` = weak candidate, keep only if list size is limited
- `<40` = exclude by default

Do not inflate scores without evidence.

---

## Deduplication Rules

Deduplicate by:
- primary website domain
- normalized company name
- same entity appearing across multiple directories
- same group brand with repeated regional pages unless they represent separate real buyer locations

Keep the best verified entry when duplicates exist.

---

## Output Rules

Produce two outputs whenever possible:

1. a structured lead table
2. a short review summary

### Lead table
The table should contain one row per company.

### Review summary
The summary should include:
- how many leads were found
- which segments appeared strongest
- which segments looked promising at first but turned out weak
- what demand signals were most common
- what data gaps remain
- what follow-up search angle should be tried next

---

## Output Style

The final answer should not just dump company names.

It should:
1. briefly restate the search target
2. explain the strongest buyer pattern found
3. provide the lead list
4. identify weak spots or missing contacts
5. suggest the next search angle only if useful

Be concise, evidence-based, and commercially practical.

---

## Search Quality Rules

Do not use only one query pattern.

Every search task should combine:
- segment keywords
- scenario keywords
- demand-signal keywords
- local-market wording when useful

The result should reflect **reasoned buyer discovery**, not simple keyword scraping.

---

## Example Requests

- find 25 hidden buyers for children's balls in UAE targeting hotels and resorts
- search non-obvious buyers for therapy exercise balls in Germany
- build a prospect list of schools and activity centers in Japan that may buy training balls
- find event and promotional companies in Saudi Arabia that may bulk buy branded sports items
- search institutional buyers in Malaysia for children's play and physical activity products

---

## Agent Behavior Rules

- Be skeptical.
- Do not assume a company is a buyer without evidence.
- Do not treat every relevant company as equally valuable.
- Prefer fewer, better, evidence-backed leads over large noisy lists.
- Always explain why a company is included.
- Focus on purchase logic, not surface keyword similarity.
