---
name: market-research
description: Research the market for a product from its repository and a short summary, then produce the documents needed to position and launch it. Runs staged agent teams that study the product, write a product document, research the market, find and profile competitors (how they position themselves and the language they use, their growth strategy, what their users love and complain about), and finally write a product brief, go-to-market plan, pitches per audience, website content strategy, product opportunities and a step-by-step execution plan. Use whenever the user asks for market research, competitor or competitive analysis, positioning, value proposition, audience or ICP definition, go-to-market or growth strategy, pitch or messaging work, or website messaging for a product or repository, and to resume, refresh or extend an earlier run (for example adding a competitor). Not for a single factual question; use a general research skill for that.
---

# Market Research

Take a product from "here is the repository and a few sentences about it" to a set of documents its owner can act on: what the product is and who it is for, what market it sits in, who it competes with and how they talk to their customers, what those customers love and resent, and a positioning, go-to-market, pitch, website and execution plan built on that evidence.

The work runs as seven stages. Each stage writes files into one workspace, and each later stage reads only those files. That is what lets a run stop and resume, lets one stage be redone without the others, and lets the same skill be pointed at a different product next week. You are the lead: you hold the plan, brief the agents, check what comes back and keep the run log. The agents do the reading and the web research, because the material is far larger than one context can hold and because independent readers notice different things.

## Two registers, kept apart

Documents about **our product** are aspirational. Their job is to capture what the product is for and where it is going, so intent and projection are wanted. What they must not contain is an invented fact. Every statement about our product is one of four kinds, and the reader must be able to tell which:

- **Today**: it exists, and someone saw it.
- **Intended**: the owner said so, or a plan or design document says so.
- **Possible**: the writer's own reasoned view of what the product could become or be used for, labelled as the writer's.
- **Open**: unknown or undecided.

Documents about **competitors and the market** are evidence-led. Every claim carries a link to a page opened during this run, quotations are verbatim, and "not found" is an acceptable finding where a figure or a fact could not be sourced.

[references/standards.md](references/standards.md) states both registers in full. Every agent reads it before working, and you hold the final documents to it.

## Workspace

Use `market-research/<product-slug>/` under the working directory unless the user names another place or the repository's instructions say where such documents belong. Take the slug from the product's name, or from the repository's name until the product's name is known.

```
market-research/<product>/
  README.md                     run log: stage status, decisions, gaps, index
  intake.md                     stage 1: owner's summary, value propositions, audiences, context
  repo-map.md                   stage 2: components and study areas
  components/<area>.md          stage 3: one document per study area
  product.md                    stage 4: the product, its markets, users and value
  market.md                     stage 5: categories, size, buyers, trends, channels
  competitors.md                stage 5: long list, filter decisions, shortlist
  competitors/<company>-brief.md
  competitors/<company>-positioning.md
  competitors/<company>-growth.md
  competitors/<company>-feedback.md
  landscape.md                  stage 7: cross-competitor synthesis
  strategy/product-brief.md
  strategy/go-to-market.md
  strategy/pitches.md
  strategy/website-content-strategy.md
  strategy/product-opportunities.md
  strategy/execution-plan.md
  strategy/review.md            stage 7: the independent reviewer's findings
```

`<company>` is the slug the competitor scout assigns, in lowercase with hyphens. Write nothing outside the workspace, leave the product's source untouched, and commit only if the user or the repository's own instructions call for it.

## Before starting

**Which product.** A repository may hold one product or several. Take the product from the request. If the request does not say and the repository holds more than one, the product is the one the top-level README presents; record that reading in the run log and name the paths you treated as in scope.

**Which run.** Look for an existing workspace for this product and read its `README.md`. If several workspaces exist and the request does not name a product, say which you found and work on the most recently updated.

- **New run**: no workspace. Start at stage 1.
- **Resume**: the run log shows an unfinished or stale stage. Continue from the first one, and do not redo finished work.
- **Redo a stage**: the user wants one revisited (new value propositions, a different audience, a corrected competitor list). Before doing anything else, mark that stage and every later stage that read its output as stale in the run log, so that an interrupted redo cannot leave superseded documents looking finished. Then redo them in order. A strategy built on a superseded product document is wrong in ways nobody will notice.
- **Add a competitor**: add it to `competitors.md`, run stage 6 for that company only, then redo stage 7.
- **Drop a competitor**: move its four files to `competitors/dropped/`, record the reason in `competitors.md`, then redo stage 7.
- **Refresh**: competitor and market research is perishable. If those documents are more than about three months old, or the user asks, rerun stages 5 to 7 and keep stages 1 to 4 unless the product has changed.

**How deep.** Use the standard depth unless the user asks for another.

| Depth | Study areas | Competitors | Competitor research |
|-------|-------------|-------------|---------------------|
| Quick | up to 5 | 3 to 4 | one researcher per company writes all four documents |
| Standard | 6 to 14 | 6 to 8 | three researchers per company |
| Deep | as many as the repository needs | up to 12 | three researchers per company |

**Narrower requests.** A request for part of this work still needs the stages beneath it. Competitor analysis alone is stages 1 to 6 and `landscape.md`. A pitch, positioning or website request is stage 7's relevant documents, with `landscape.md` and `product-brief.md` first because the others depend on them. If the workspace already holds the earlier stages and they are current, use them. If it does not, run them at quick depth unless told otherwise, and say that you are doing so.

**Without parallel agents.** If the host cannot start agents, perform each role yourself in turn, one output file at a time, reading that role's brief before each. Keep the same files and the same order. Prefer the quick depth, and write each file before starting the next so that nothing depends on your remembering it.

Keep the host's task list current with the seven stages so the user can see where the run stands.

## Stage 1: intake, value propositions and audiences

The owner's own account of the product is the anchor for everything that follows, since the repository shows what was built and only the owner knows what it is for.

1. Collect what the request already gives: a summary of the product, its main value, who pays for it, and anyone else it must convince (investors, acquirers, partners, a community).
2. If there is no summary, ask for one, once, in plain words: a few sentences on what the product is, why someone would choose it, and who pays. Stage 2 does not depend on the answer, so map the repository first and ask afterwards. If no answer can be had (an unattended run, or the user says to carry on), write the summary yourself from the repository's own description of the product, mark it in `intake.md` as assumed and not confirmed by the owner, and continue.
3. If audiences are missing but a summary exists, propose them yourself and mark them as assumptions.
4. Research how the product describes itself now: the README, top-level documentation, any website copy, pitch or positioning notes in the repository, and any list of claims the project refuses to make. Note where this agrees with the owner's summary and where it does not.
5. Draft three to six value propositions. For each: the promise in one sentence, who it is for, the pain it removes, what backs it (Today, Intended or Possible), what would strengthen it, and how confident you are.
6. Describe each audience: paying audiences in priority order, then audiences that do not pay but matter. For each: who they are, the situation that makes them look, what they need to believe, their likely objection, and what they use today.
7. Record the context later stages plan around, from the request and the repository, writing "not stated" where neither says: the **product type** (for example a developer tool, a business application, a consumer app, an open-source project, a hardware product, a service), the product's stage (idea, pre-launch, launched, growing), team size, budget for marketing, pricing or the intended pricing, traction so far, competitors the owner named, geography and language, and any rules about what may be claimed.

Write `intake.md` with these sections: the owner's summary quoted verbatim; how the product describes itself today; value propositions; audiences; context; assumptions made at intake. Quote the owner exactly so that later agents read the original intent and not a paraphrase of it. [references/example-intake.md](references/example-intake.md) shows a finished one. These value propositions are hypotheses; stage 4 refines them against what the product really contains.

## Stage 2: map the repository

Work out what there is to study before sending anyone to study it. Read the top-level layout, the README files, manifests and documentation indexes, and the repository's agent instructions. For a large repository, give the survey to one read-only exploration agent and keep its conclusion.

Sort what you find into components, and say what each is: a product surface people use, a capability the product is built on, developer tooling, an example or demo, documentation or marketing, operations, or something to skip (vendored code, generated output, fixtures, abandoned experiments). Then group the components into **study areas**, each small enough for one agent to read properly and coherent enough to describe as one thing. Let the repository decide the number within the depth chosen: an area too large for one agent to read is split, and several small related components are merged. Examples and demos deserve an area of their own, because they show what the product is meant to be used for.

Write `repo-map.md`: the components, the study areas with their paths and rough size, what was skipped and why, and any rules about claims the repository imposes. If there is no repository, the study areas are whatever sources the user supplies (a website, documentation, a deck), divided the same way.

**Before the fan-out**, tell the user in two or three lines what is about to happen: the product as you understand it, the audiences (noting any you assumed), the depth, and roughly how many agents the run will start. Do not wait for a reply; this is so that a wrong premise can be caught while it is cheap.

## Stage 3: study every area

Launch one **component analyst** per study area ([references/roles/component-analyst.md](references/roles/component-analyst.md)), all in one message so they run together. Each writes `components/<area>.md`.

These documents feed a product brief, so they describe what an area does, why it matters and to whom, how it is used and run, what a person needs to know to use it, who it suits, its upsides and risks, and what it could become. They are not source documentation, and an agent that returns an inventory of files and functions has missed the assignment.

## Stage 4: write the product document

One **product writer** ([references/roles/product-writer.md](references/roles/product-writer.md)) reads `intake.md` and every component document and writes `product.md`: what the product is, the refined value propositions, the markets it fits, the people who would want it, and the search terms a competitor hunt should start from.

Read it yourself against `intake.md` when it returns. Where the repository contradicts or extends the owner's account, record the difference in the run log; it is one of the most useful things the run produces.

## Stage 5: the market and the competitors

Everything from here depends on reading the live web. Before launching anyone, confirm that it works in this session: run one search and open one page. If the host has no working web access, stop after stage 4, say so plainly, and record it in the run log. Competitor documents written from a model's memory would be out of date and unverifiable, and they would look exactly like real ones.

Launch two agents together:

- The **market analyst** ([references/roles/market-analyst.md](references/roles/market-analyst.md)) writes `market.md`: the categories, their size, how buyers buy, what is changing, where money is moving, and where the product's audiences pay attention.
- The **competitor scout** ([references/roles/competitor-scout.md](references/roles/competitor-scout.md)) builds a long list from `product.md`, filters it, and writes `competitors.md` with a ranked shortlist and the reasons for every cut.

Tell the scout the shortlist size for the chosen depth and every competitor the owner named. Proceed on the scout's shortlist without stopping to ask: the cut list and its reasons are in the file, and adding a company later is a cheap rerun.

## Stage 6: research each competitor

Run two waves, the second after the first has returned, so the later agents can read the brief and spend their effort on their own question.

**Wave A, one agent per competitor.** The **competitor profiler** ([references/roles/competitor-profiler.md](references/roles/competitor-profiler.md)) writes `<company>-brief.md` (the same product information we gathered about ourselves) and `<company>-positioning.md` (how they present themselves and the exact words they use).

**Wave B, two agents per competitor.** The **growth researcher** ([references/roles/growth-researcher.md](references/roles/growth-researcher.md)) writes `<company>-growth.md`. The **feedback researcher** ([references/roles/feedback-researcher.md](references/roles/feedback-researcher.md)) writes `<company>-feedback.md` from reviews, forum threads, social posts and news.

At quick depth, one researcher per competitor reads all three role files and writes the four documents in that order.

Launch each wave in batches of up to about ten agents at a time, since a larger burst of simultaneous web research tends to hit rate limits and return thinner work.

## Stage 7: synthesis and strategy

[references/strategy-documents.md](references/strategy-documents.md) defines every document in this stage. It runs in five steps, because the documents must agree with each other and a single agent writing all of them from forty inputs loses the thread.

1. **Landscape.** One writer reads `product.md`, `market.md`, `competitors.md` and every competitor document, and writes `landscape.md`. This is where the comparisons are made, once: which loved features we share, which competitor pain points we solve, the language everyone uses and the language nobody has claimed.
2. **Product brief.** One writer reads `intake.md`, `product.md`, `market.md` and `landscape.md` and writes `strategy/product-brief.md`, which fixes the positioning, the value propositions, and the table of markets and audiences with their priorities.
3. **Four writers in parallel**, each reading the landscape and the brief first and the source documents as needed: `go-to-market.md`, `pitches.md`, `website-content-strategy.md` and `product-opportunities.md`.
4. **Execution plan.** One writer reads all five and writes `execution-plan.md`, turning their recommendations into ordered steps.
5. **Review.** One reviewer who wrote none of them reads the six strategy documents against `product.md` and `landscape.md` and writes `strategy/review.md`. Fix what it finds: small inconsistencies yourself, anything larger by returning the document to a fresh writer with the finding.

## Briefing an agent

An agent starts with nothing but your brief, so the brief must stand alone. Use absolute paths, resolving the reference files against this skill's directory.

```
You are the <role> in a market-research run for <product>.

Read these first, in order:
1. <skill dir>/references/standards.md
2. <skill dir>/references/roles/<role>.md   (stage 7: references/strategy-documents.md; your document is "<document>")
3. <workspace>/intake.md, and <workspace>/product.md once it exists

Assignment: <the study area and its paths / the competitor, its scope and its URL / the document>
Other inputs: <files this agent should read, by absolute path>
Write: <absolute output path or paths>
Product type: <from intake.md>
Rules this product imposes on claims: <the rules found in stage 1 or 2, or "none found">
Today's date: <date>
```

Add anything specific the agent needs (a competitor the user singled out, a known gap to chase), and nothing it could misread as a conclusion to confirm. Use general-purpose agents, which can both search the web and write files. Tell every agent not to create branches or commits; the workspace is yours to manage.

## Receiving the work

An agent's report is a lead, and its file is the deliverable. After each wave, before starting the next stage:

- Confirm every expected file exists and follows its template.
- Read each one far enough to judge it. A component document that lists files, a competitor document without links, or a feedback document without quotations has failed and goes back to a fresh agent once, with the specific gap named.
- Check sources yourself, because a fabricated quotation is the likeliest serious failure and nothing else catches it. For each feedback document, open the pages behind three quotations and confirm the words are there. For each brief, positioning and growth document, and for `market.md`, open the page behind one claim the strategy is likely to lean on. If a quotation cannot be found on its page, treat the whole document as unreliable and have it redone.
- Record in the run log whatever stays thin after a second attempt. A stated gap is useful to the reader; a papered-over one damages every document downstream.

At the end, read the six strategy documents together with the reviewer's findings. Check that they use the same name for the product, the same value propositions and the same priorities as `product-brief.md`, that nothing marked Intended or Possible has turned into a present-tense claim, and that the links between documents resolve.

## The run log

Keep `README.md` current as you go; it is how the next run, and the owner, find their way back in.

```markdown
# Market research: <product>

Last run: <date>. Depth: <quick | standard | deep>. Status: <complete | stopped after stage N>.

## Stages
| Stage | Output | Status (done, stale, incomplete) | Date | Notes |

## Decisions made during the run
Each judgment call with its reason: the product's scope, assumed audiences,
how areas were grouped, which competitors were cut, anything interpreted.

## Where the repository and the owner's summary differ

## Gaps and things not verified
Including sources that could not be reached.

## Documents
Links to every file, strategy documents first.
```

## Closing the run

Report in the host's and the user's own conventions. Lead with where the six strategy documents are, then the decisions you made that the owner may want to overturn (the competitor shortlist and any assumed audience first), the gaps, and the two or three findings that most change how the product should be presented.
