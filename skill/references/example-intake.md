# Example: a finished `intake.md`

This is an invented product, shown so the lead can see the level of detail and the handling of Today, Intended, Possible and Open that stage 1 should reach. Do not copy its content.

```markdown
# Tallyroom: intake

Product: Tallyroom. Date: 2026-03-02. Written by: lead.
Inputs: the owner's request; README.md; docs/overview.md; docs/roadmap.md; site/copy/home.md; site/copy/pricing.md.

## The owner's summary, verbatim

> Tallyroom is stock control for independent bookshops. The main thing is that
> a shop can see what it actually has without closing for a stock-take, and the
> ordering suggestions mean the owner stops over-buying. Customers are shop
> owners with one to three branches. Later I want distributors to pay for
> anonymised sell-through data.

## How the product describes itself today

The README leads with "inventory that keeps itself honest" and describes
barcode scanning from a phone. The home page copy leads with saving time on
stock-takes. Neither mentions ordering suggestions, which the owner's summary
treats as central. docs/roadmap.md lists distributor reporting as planned for
later in the year. No list of claims to avoid was found.

## Value propositions (hypotheses, to be refined in stage 4)

| # | Promise | For whom | Pain removed | Backing | Confidence |
|---|---------|----------|--------------|---------|------------|
| 1 | Know what is on the shelves without closing the shop | Owners of small bookshops | The annual stock-take and the guesswork between | Today: rolling counts by phone scan are described in the README | High |
| 2 | Stop over-buying | The same owners | Cash tied up in stock that does not sell | Intended: the owner's summary; a suggestions module exists in the source but the documentation does not describe it | Medium |
| 3 | Sell-through data for distributors | Book distributors | No view of what sells in independent shops | Intended: roadmap only | Low |

What would strengthen them: a measured figure for time saved on a stock-take
(Open); evidence that suggestions reduce purchasing (Open).

## Audiences

**Paying, primary: owners of independent bookshops with one to three branches.**
They look when a stock-take goes badly or cash runs short. They need to believe
it works with the till they already have and takes no more staff time than
today. Likely objection: "I tried a system before and nobody kept it up to
date." Today they use the till's own stock module, a spreadsheet, or memory.

**Paying, later: book distributors.** Stated by the owner as a future source of
revenue. Trigger, objection and current alternative are Open.

**Not paying: none named.** Assumption: a small grant-funded or bootstrapped
product; investors are not treated as an audience unless the owner says so.

## Context

- Product type: a business application for small retailers.
- Stage: launched; the README says a handful of shops use it. The number is
  not stated.
- Team size: not stated. Budget for marketing: not stated. The run assumes a
  team of one or two with little money for marketing.
- Pricing: a monthly fee per branch, according to site/copy/pricing.md.
- Traction: not stated beyond the above.
- Competitors named by the owner: none.
- Geography and language: not stated.
- Rules about claims: none found.
- Live product: a hosted service at the address in the README. This run did
  not sign in to it; statements about the running service rest on the
  repository.
- Names to keep out: none found.

## Assumptions made at intake

- The primary market is English-speaking independent bookshops; the owner did
  not name a country.
- Ordering suggestions are treated as Intended until stage 3 establishes what
  the module does.
```
