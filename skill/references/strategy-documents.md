# Strategy documents

Stage 7 turns the research into documents the owner can act on. This file defines all of them. Read the whole file even though you are writing one, so that you know what the neighbouring documents cover and can refer to them instead of repeating them.

## Contents

- Rules for every strategy document
- `landscape.md`
- `strategy/product-brief.md`
- `strategy/go-to-market.md`
- `strategy/pitches.md`
- `strategy/website-content-strategy.md`
- `strategy/product-opportunities.md`
- `strategy/execution-plan.md`
- `strategy/review.md`

## Rules for every strategy document

**What to read.** Everyone reads `intake.md` (for the owner's intent and the context: product type, stage, team, budget) and `product.md`. Then:

| Document | Reads closely | Consults for detail |
|----------|---------------|---------------------|
| `landscape.md` | `market.md`, `competitors.md`, every file in `competitors/` (not `competitors/dropped/`) | `components/*.md`, to check what our product has |
| `product-brief.md` | `market.md`, `landscape.md` | the `-positioning.md` files |
| `go-to-market.md` | `landscape.md`, `product-brief.md`, `market.md` | the `-growth.md` files |
| `pitches.md` | `landscape.md`, `product-brief.md` | the `-positioning.md` and `-feedback.md` files |
| `website-content-strategy.md` | `landscape.md`, `product-brief.md` | the `-positioning.md` and `-feedback.md` files |
| `product-opportunities.md` | `landscape.md`, `product-brief.md`, `market.md` | the `-feedback.md` files, `components/*.md` |
| `execution-plan.md` | the five strategy documents | `landscape.md` |
| `review.md` | the six strategy documents, `landscape.md` | whatever a finding needs checking against |

**The product brief is fixed.** Once `product-brief.md` exists, every other document uses its name for the product, its positioning statement, its value propositions, and its table of markets and audiences with their priorities, word for word where they are quoted. If you think the brief is wrong, say so in your report to the lead; do not quietly diverge, because six documents that each position the product slightly differently are worse than one imperfect position.

**Trace recommendations to evidence.** A recommendation should name what it rests on: a competitor's result in a `-growth.md`, a complaint in a `-feedback.md`, a figure in `market.md`, a capability in `product.md`. Link to the file. A recommendation that rests on your judgment alone is allowed and should say so.

**You may check a fact on the web.** The research documents are your sources, and you are not asked to redo them. Where a recommendation needs a specific fact they lack (whether a publication accepts contributed articles, what an advertising channel requires), look it up under the same standards and cite it.

**Persuade with true things.** Pitches and website copy are meant to persuade, and they may speak about where the product is going. Copy for publication may draw on Today and Intended only, and any line that depends on something Intended must be marked, so the owner knows which lines can be used now and which wait on the product. Possible belongs in `product-opportunities.md` and in sections about the future, labelled as such. Carry the product's own rules about claims into every document.

**Fit the plan to the product.** Take the product type, stage, team size and budget from `intake.md`. Where they are not stated, assume a small team with little money and say that you did. A plan that needs twelve people is no use to three, and a channel that suits a developer tool is wrong for a consumer app.

**Borrow the customer's words.** Where the feedback documents show how buyers describe their problem, use those words in preference to ours or a competitor's.

## `landscape.md`

Written first, at the top of the workspace. This is where the comparisons are made, once, so that the other documents can rely on them.

The two tables in the middle are the reason this document exists. Before writing "No" in the column that says whether we have a feature, check the capability table in `product.md` and then the relevant files in `components/`; a product document compresses, and a capability lost in the compression would otherwise become a false gap. Before writing "Today", confirm a component document describes it as existing. Include the rows where the honest answer is unfavourable.

```markdown
# <Product>: competitive landscape

<header as in the standards>

## The market in a page
From market.md and the briefs: the categories, who leads each, how buyers
choose, and what is changing.

## Comparison
| | Our product | Competitor A | Competitor B | … |
Rows: who it is for; the core promise; pricing model; how it is adopted;
strongest point; weakest point; growth motion.

## How the market talks
- Standard language: words and claims nearly every competitor uses, which a
  buyer now expects and which no longer distinguish anyone.
- Owned language: phrases one competitor has made its own, which we should not
  echo.
- Open ground: problems and promises that buyers voice in the feedback
  documents and that no competitor's positioning addresses.

## What users love elsewhere that we also offer
| What they love | Where it is loved (links) | Do we have it? (Today / Intended / No) | Where in our product | How to say so |

## Competitor pain points we solve or could do better
| Pain point | Who suffers it, and where (links) | Our answer (Today / Intended / Possible / none) | How strong the claim is |

## Where we are behind
What buyers get elsewhere that we cannot offer, and whether it matters to our
audiences.

## Substitutes and the status quo
From competitors.md: why people build it themselves, make do or do nothing,
and what would move them.

## Growth lessons
The moves that worked for several competitors, the ones that worked once, and
the routes now closed.

## White space
The positions, segments and channels nobody has taken.
```

## `strategy/product-brief.md`

The single reference for what the product is and how it is described. It also sets the priorities the other documents follow, so that the pitches and the go-to-market plan, which are written at the same time, do not each choose their own.

```markdown
# <Product>: product brief

<header as in the standards>

## One line
## Description
In 25 words, in 100 words, and in a page.

## Positioning statement
For <audience> who <situation>, <product> is a <category> that <benefit>.
Unlike <alternative>, it <difference>. Follow with the reasoning: why this
position, given the landscape, and what was considered and set aside.

## The pitch
A version to say in thirty seconds and a version for two minutes.

## Market
The category we claim, the neighbouring categories, how buyers find products
in it, and its size, taken from market.md with its sources and caveats. Where
market.md found no credible figure, say so and describe the scale in words.

## Markets and audiences
| Market | Audience | Priority (first / next / later / not now) | Leading value proposition | What they compare us with |
A market is a category or a customer segment; an audience is who we speak to
within it. Include the audiences that do not pay. Name the one combination to
win first, and give the reason.

## Audiences
Each audience in priority order: who, the trigger, what they need to believe,
and the value proposition that leads for them.

## Value propositions
Each with its proof Today, what is Intended, and the competitor weakness or
user wish it answers.

## What makes it different
Three or four differences that are true, that matter to the buyer and that a
competitor cannot easily claim.

## Objections and answers
The hard questions each audience would ask, with honest answers.

## What we do not claim
Claims to avoid: untrue today, unprovable, owned by a competitor, or ruled out
by the project's own rules.

## Messaging pillars and vocabulary
The few themes all communication returns to, the words we use, and the words
we avoid.
```

## `strategy/go-to-market.md`

Take the first market and audience from the product brief; do not choose another. Cover every channel listed, including the ones you recommend against, so the owner can see each was considered. Add channels this kind of product calls for (app stores, retail, resellers) and say where a listed one does not apply.

```markdown
# <Product>: go-to-market plan

<header as in the standards>

## Goal and starting point
What this plan is meant to achieve in the next six to twelve months, and the
stage, team and money it assumes.

## Who first
The first market and audience from the product brief and what winning it looks
like; the order of the others.

## Growth strategy
The motion (self-serve, sales-led, community-led or a mix), the loop that makes
each customer bring the next, pricing and packaging as hypotheses to test, and
which competitor's path this resembles or deliberately avoids.

## Channels
One section each for: social media; news and press; blogs and long-form
content; advertising campaigns; influencers, creators and prominent
practitioners; community; launches; partnerships and integrations; events.
For each: why it suits this audience, with evidence from the growth documents
and from "where the audiences pay attention" in market.md; what to do;
concrete first pieces or campaigns with working titles; cadence; cost in time
and money; and how to tell whether it is working. Say plainly which channels
to skip for now and why.

## Launch plan
What to launch, where, in what order, with what assets.

## Measures
The few numbers that show whether the plan is working, and the level that
would mean changing course.

## Risks
What could make this plan fail and what to watch for.
```

Name publications, communities, events and creators only when a research document or a page you opened shows they exist and reach this audience, and link them. Otherwise describe the kind to look for.

## `strategy/pitches.md`

A pitch for each combination of market and audience in the product brief's table that is marked first, next or later. Copy the table at the top, with its priorities unchanged. Include the audiences that do not pay, such as investors and acquirers, whose pitch is about the market, the timing and the company more than the features, and draws on `market.md`.

```markdown
# <Product>: pitches

<header as in the standards>

## Combinations
The table from the product brief.

## <Market> × <Audience>
- Who they are and the situation they are in
- What triggers the search
- One line
- Thirty seconds, spoken
- A short written version (an email or a message)
- Proof to offer, Today and Intended kept apart
- Objections and answers
- The comparison they will make, and the fair contrast to draw
- What to ask them to do next
- Words to use, and words to avoid, with this audience
```

## `strategy/website-content-strategy.md`

```markdown
# <Product>: website content strategy

<header as in the standards>

## What the site must do
For each audience: what they arrive wanting, what they must leave believing,
and the action we want.

## Site map
The pages, and the path each audience takes through them.

## Page by page
For each page: purpose; audience; the one message; sections in order;
two or three headline and sub-headline options; proof to show; call to action;
which lines depend on something Intended.

## Comparison and alternative pages
Which competitors deserve one, and the fair contrast each should draw.

## Content pillars
The recurring subjects for articles, guides and examples, each tied to an
audience and a value proposition.

## Search and discovery
The terms buyers use (from the feedback and positioning documents), the
questions they ask, and the pages that should answer them. Include how the
product should appear to AI assistants that recommend products.

## First pieces to publish
A list of titles with audience, purpose and source material.

## Voice
How the site should sound, with a few before-and-after examples.

## What competitors' sites teach
Patterns worth adopting and habits to avoid, with links.
```

## `strategy/product-opportunities.md`

Things the product could add, change or package differently to reach a larger market. This is advice to the owner about the product itself, grounded in what the research found people want. It is the home of the Possible: draw on the "what it could become" sections of the component documents as well as on competitor feedback.

```markdown
# <Product>: product opportunities

<header as in the standards>

## Summary
The few opportunities that matter most and why.

## Opportunities
For each, in order of value:
- The opportunity, in a sentence
- The evidence: the complaint, request, segment, market shift or competitor
  gap behind it, with links
- Who it would win and what market it opens
- What it would take, as a rough size (days, weeks, months) and the main
  unknown
- Risk, including the risk of distracting from the core
- How to test demand before building

## Expected features we are missing
Things buyers in this market assume, whose absence loses them.

## Packaging and pricing opportunities
## Partnerships and integrations
## Opportunities considered and rejected
With the reason, so they are not proposed again without new evidence.
```

## `strategy/execution-plan.md`

Written after the other five. It adds no new strategy; it puts their recommendations in order and makes each one a step somebody can start on.

```markdown
# <Product>: execution plan

<header as in the standards>

## Before anything else
Decisions only the owner can make, each with a recommendation, and the
prerequisites nothing can start without.

## Phases
Phase 0: foundations (positioning agreed, site, basic assets, measurement).
Then phases by time: first two weeks, first month, months two and three,
months four to six. Adjust the horizon to the plan's scale.

For each step:
| # | Step | Why now | Source document | Who (role) | Effort | Depends on | Done when |

## What to prepare
The assets to produce (copy, pages, demos, decks, examples), each pointing to
the section of the document that specifies it.

## Checkpoints
At the end of each phase: what to measure, what result means continue, and
what result means change course.

## What is deliberately left out
Recommendations from the other documents that this plan defers, and why.
```

Every step must come from one of the other documents; if a necessary step has no source, add it and say that it is new. Write "done when" as something observable. Size the plan to the team in `intake.md`.

## `strategy/review.md`

Written last by a reviewer who wrote none of the others. Read the six strategy documents as a sceptical member of each audience would, and check them against `product.md` and `landscape.md`. You are looking for defects, not rewriting; the lead decides what to change.

```markdown
# <Product>: strategy review

<header as in the standards>

## Verdict
Whether the set is fit to act on, in two or three sentences.

## Findings
| # | Document and section | Kind | What is wrong | Suggested fix |
Kinds:
- inconsistent: a name, value proposition, priority or audience that differs
  from the product brief
- overclaimed: something Intended or Possible written as present fact, or a
  claim the product's own rules exclude
- unsupported: a factual statement about a competitor or the market with no
  trace to a research document
- unusable: a recommendation too vague to act on, or beyond the team's means
- missing: something the document's template requires that is absent
- broken link

## Checked and sound
What you verified and found correct, briefly, so the lead knows the extent of
the review.
```

Open the research document behind at least five factual claims across the set, chosen from those the strategy leans on hardest, and confirm each says what the strategy document says it does.
