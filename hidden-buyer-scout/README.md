# hidden-buyer-scout

Find non-obvious cross-industry buyers for a product in a target market.

This skill is designed for **scenario-based buyer discovery**, not standard distributor or importer lookup.

Use it when the user wants to know:
- who else may buy this product besides the obvious industry players
- what hidden demand exists in the target market
- which segments may purchase in volume even though the product is not in their core catalog

## How It Differs From `b2b-lead-scout`

- `b2b-lead-scout`: finds buyers inside the normal product distribution chain
- `hidden-buyer-scout`: finds buyers outside the obvious chain based on scenario logic and bulk-purchase possibility

Use `hidden-buyer-scout` when the buyer is discovered by **usage logic**, not just by category matching.

## Core Workflow

1. Fill missing essential inputs if needed
2. Generate buyer hypotheses
3. Present a second-interaction buyer-direction analysis
4. Let the user confirm the search direction
5. Search and verify companies
6. Output a structured lead list and a short review summary

## Interaction Model

This skill should use **at most 2 interactions** before final lead generation.

### Interaction 1

Only ask for missing essentials:
- product
- target country
- preferred hidden-buyer angle, if truly needed

### Interaction 2

Present a short buyer-direction analysis with:
- strong logic segments
- non-traditional but high-potential segments
- experimental segments

Each proposed direction should explain:
- usage scenario
- buying logic
- likely buyer role
- likely purchase frequency

Then ask the user whether to:
- search all directions
- search selected directions
- adjust the search direction

## Output Philosophy

The result should not be a random long list of loosely relevant companies.

The result should:
- reflect actual purchase logic
- prefer fewer strong candidates over noisy volume
- explain why each company is worth considering
- separate stronger and weaker patterns in the summary

## Included Examples

- `examples/interaction-2-analysis.md`
- `examples/final-lead-table.md`
- `examples/final-lead-table.csv`

These examples show:
- how the second interaction should look
- how final lead output should look
- how to balance creative discovery with commercial logic
