---
name: market-research
description: Research the market for a product from its repository and a short summary, then produce the documents needed to position and launch it. Runs staged agent teams that study the product, write a product document, research the market, find and profile competitors (how they position themselves and the language they use, their growth strategy, what their users love and complain about), and finally write a product brief, go-to-market plan, pitches per audience, website content strategy, product opportunities and a step-by-step execution plan. Use whenever the user asks for market research, competitor or competitive analysis, positioning, value proposition, audience or ICP definition, go-to-market or growth strategy, pitch or messaging work, or website messaging for a product or repository, and to resume, refresh or extend an earlier run (for example adding a competitor). Run the full staged workflow only when the user asks for the research or its documents; for a question or a single piece of advice, use the relevant parts as guidance.
---

# Market Research

Take a product from "here is the repository and a few sentences about it" to a set of documents its owner can act on: what the product is and who it is for, what market it sits in, who it competes with and how they talk to their customers, what those customers love and resent, and a positioning, go-to-market, pitch, website and execution plan built on that evidence.

## Two ways to use this skill

Loading this skill does not by itself authorize a run that starts dozens of agents and writes a directory of documents.

- **Guidance.** For a question, a review of one pitch or page, advice on positioning, or a look at a single competitor, use the relevant parts: the registers below, a role's method, a document template. Answer in the conversation. Start no workspace and no teams. If a workspace for this product already exists, read it and answer from it.
- **Full run.** When the user asks for market research, a competitive analysis, a go-to-market plan or the document set, or asks to resume, refresh or extend an earlier run, follow the staged workflow below.

If a request could mean either, ask one question before creating files or starting agents.

## How a full run works

The work runs as seven stages. Each stage writes files into one workspace, and each later stage reads only those files. That is what lets a run stop and resume, lets one stage be redone without the others, and lets the same skill be pointed at a different product next week. You are the lead: you hold the plan, brief the agents, check what comes back and keep the ledger and the run log. The agents do the reading and the web research, because the material is far larger than one context can hold and because independent readers notice different things.

Three habits carry the quality of the run, and each stage below relies on them:

- **The ledger is the record.** Every assignment is a unit in `run.json` with a status. What was covered, what was thin and what was left out is read from the ledger, never asserted from memory.
- **Nobody checks their own work.** Coverage is reviewed by a critic who did not plan it, sources are checked by an agent who did not cite them, and the strategy is reviewed by a reader who did not write it.
- **A stated gap beats a filled one.** An agent that cannot find something says so, and a unit the budget cannot reach is recorded as deferred. Nothing is thinned silently.

[references/orchestration.md](references/orchestration.md) covers the ledger, the budget, the brief every agent receives, the report it returns, the checks, and how work is carried over from earlier runs. Read it before the first fan-out.

## Two registers, kept apart

Documents about **our product** are aspirational. Their job is to capture what the product is for and where it is going, so intent and projection are wanted. What they must not contain is an invented fact. Every statement about our product is one of four kinds, and the reader must be able to tell which:

- **Today**: it exists, and someone saw it, either in the source or in the product a customer uses. The two can differ, and the documents say which.
- **Intended**: the owner said so, or a plan or design document says so.
- **Possible**: the writer's own reasoned view of what the product could become or be used for, labelled as the writer's.
- **Open**: unknown or undecided.

Documents about **competitors and the market** are evidence-led. Every claim carries a link to a page opened during this run, quotations are verbatim, and "not found" is an acceptable finding where a figure or a fact could not be sourced.

[references/standards.md](references/standards.md) states both registers in full. Every agent reads it before working, and you hold the final documents to it.

## Workspace

Use `market-research/<product-slug>/` under the working directory unless the user names another place or the repository's instructions say where such documents belong. Take the slug from the product's name, or from the repository's name until the product's name is known.

```
market-research/<product>/
  run.json                      the ledger: every unit, its outputs and its status
  RUN-LOG.md                    run log: decisions, findings, questions for the owner, gaps
  README.md                     written at the close: the page a reader navigates from
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
  competitors/checks/<company>.md   stage 6: the source checker's verdicts
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

The workspace is internal. It will hold candid assessments of the product, research on named companies and advice the owner may not want seen, so say so in the first lines of the run log and of `README.md`, and never commit it to a repository that is public or will become so. If the owner wants the set kept or shared with a team, a private repository of its own is the natural home, and the workspace is laid out to become one.

## Before starting

**Which product.** A repository may hold one product or several, and one product may span several repositories. Take the product from the request. If the request does not say and the repository holds more than one, the product is the one the top-level README presents; record that reading in the run log and name the paths you treated as in scope. When the user names more than one repository, study them as one product, record each with its commit in the ledger, and say in `repo-map.md` which part of the product lives where.

**Which run.** Look for an existing workspace for this product and read its `run.json` and `RUN-LOG.md` (a workspace from an earlier version keeps the run log in `README.md`). If several workspaces exist and the request does not name a product, say which you found and work on the most recently updated.

- **New run**: no workspace. Start at stage 1.
- **Resume**: the ledger has units that are planned, in progress or stale. Continue from the earliest stage that has one, and do not redo finished work.
- **Redo a stage**: the user wants one revisited (new value propositions, a different audience, a corrected competitor list). Before doing anything else, mark that stage's units and every later unit that read their output as `stale` in the ledger, so that an interrupted redo cannot leave superseded documents looking finished. Then redo them in order. A strategy built on a superseded product document is wrong in ways nobody will notice.
- **Add a competitor**: add it to `competitors.md`, run stage 6 for that company only, then redo stage 7.
- **Drop a competitor**: move its files to `competitors/dropped/`, mark its units `dropped`, record the reason in `competitors.md`, then redo stage 7.
- **The owner answers a question**: an answer to one of the run's open decisions is recorded in the ledger's `owner_decisions` and in the run log the day it arrives. If it confirms what the documents recommend, change the passages that called it open and nothing else. If it overturns it, treat it as a redo from the product brief onward.
- **Refresh**: research goes out of date. Follow "Carrying work over from earlier runs" in the orchestration reference: re-study only the areas whose source changed, redo competitor and market documents older than about three months, and keep earlier decisions.

**How deep.** Use the standard depth unless the user asks for another.

| Depth | Study areas | Competitors | Competitor research | Independent checks |
|-------|-------------|-------------|---------------------|--------------------|
| Quick | up to 5 | 3 to 4 | one researcher per competitor writes all four documents | the lead samples sources; no critics |
| Standard | 6 to 14 | 6 to 8 | three researchers per competitor | a source checker per competitor; each coverage critic once |
| Deep | as many as the repository needs | up to 12 | three researchers per competitor | source checkers including the market; critics repeated until clean |

Depth changes how much is covered, never the rules about sources. A run starts about 40 per cent more agents than it plans units, because of follow-up waves, revisions and relaunches: a standard run on a large repository is about a hundred agents and most of a day. If the user sets a limit on cost or on the number of agents, plan against it as the orchestration reference describes: reserve the synthesis and the checks first, and record what the limit excludes as deferred.

**Narrower requests.** A request for part of this work still needs the stages beneath it. Competitor analysis alone is stages 1 to 6 and `landscape.md`. A pitch, positioning or website request that asks for documents is stage 7's relevant documents, with `landscape.md` and `product-brief.md` first because the others depend on them. If the workspace already holds the earlier stages and they are current, use them. If it does not, run them at quick depth unless told otherwise, and say that you are doing so.

Keep the host's task list current with the seven stages so the user can see where the run stands. Once the run is under way, carry it to the end: when a wave returns, start the next step, and do not end a turn between stages to ask whether to go on. If the session is interrupted, the ledger says where to pick up.

## Stage 1: intake, value propositions and audiences

The owner's own account of the product is the anchor for everything that follows, since the repository shows what was built and only the owner knows what it is for.

1. Collect what the request already gives: a summary of the product, its main value, who pays for it, and anyone else it must convince (investors, acquirers, partners, a community).
2. If there is no summary, ask for one, once, in plain words: a few sentences on what the product is, why someone would choose it, and who pays. Stage 2 does not depend on the answer, so map the repository first and ask afterwards. If no answer can be had (an unattended run, or the user says to carry on), write the summary yourself from the repository's own description of the product, mark it in `intake.md` as assumed and not confirmed by the owner, and continue.
3. If audiences are missing but a summary exists, propose them yourself and mark them as assumptions.
4. Research how the product describes itself now: the README, top-level documentation, any website copy, pitch or positioning notes, product or design briefs, decision records, and any list of claims the project refuses to make. Note where this agrees with the owner's summary and where it does not. Where a recorded decision and the owner's summary for this run disagree, do not choose between them: the summary is later and may supersede the record, or the owner may have forgotten it. List the difference, and let it become a question for the owner.
5. Draft three to six value propositions. For each: the promise in one sentence, who it is for, the pain it removes, what backs it (Today, Intended or Possible), what would strengthen it, and how confident you are.
6. Describe each audience: paying audiences in priority order, then audiences that do not pay but matter. For each: who they are, the situation that makes them look, what they need to believe, their likely objection, and what they use today.
7. Record the context later stages plan around, from the request and the repository, writing "not stated" where neither says: the **product type** (for example a developer tool, a business application, a consumer app, an open-source project, a hardware product, a service), the product's stage (idea, pre-launch, launched, growing), team size, budget for marketing, pricing or the intended pricing, traction so far, competitors the owner named, geography and language, and any rules about what may be claimed. Record two more things that later stages trip over. First, whether there is a **live product** (a hosted service, a store listing, a public site) and whether this run observed it: if every statement about the live product will rest on records in the repository, that is a gap to state from the start. Second, **names to keep out**: prospects, customers and people who appear only in internal notes, which no document may repeat.

Write `intake.md` with these sections: the owner's summary quoted verbatim; how the product describes itself today; value propositions; audiences; context; assumptions made at intake. Quote the owner exactly so that later agents read the original intent and not a paraphrase of it. [references/example-intake.md](references/example-intake.md) shows a finished one. These value propositions are hypotheses; stage 4 refines them against what the product really contains.

Create `run.json` now, with the depth, the budget if one was given, the repository's current commit, and the intake as its first unit.

## Stage 2: map the repository

Work out what there is to study before sending anyone to study it. Read the top-level layout, the README files, manifests and documentation indexes, and the repository's agent instructions. For a large repository, give the survey to one read-only agent and keep its conclusion.

Sort what you find into components, and say what each is: a product surface people use, a capability the product is built on, developer tooling, an example or demo, documentation or marketing, operations, or something to skip (vendored code, generated output, fixtures, abandoned experiments). Then group the components into **study areas**, each small enough for one agent to read properly and coherent enough to describe as one thing. Let the repository decide the number within the depth chosen: an area too large for one agent to read is split, and several small related components are merged. Examples and demos deserve an area of their own, because they show what the product is meant to be used for.

Three kinds of material are easy to pass over because they are not the product's code, and each deserves an area whenever it exists:

- **The existing positioning, website and marketing copy.** The website strategy has to say what to keep and what to change, which it cannot do for a site nobody read.
- **The owner's recorded decisions, plans and pitch.** Without them the strategy reopens what was settled, or fails to notice that a decision is out of date.
- **How the product is sold and run for customers**: the licence, what is public and what is not, pricing, hosting, and what happens to a customer's data at an upgrade. Buyers ask about these before they ask about features.

A project that sits beside the product in the same repository is read at least as far as its README before it goes on the skip list.

Write `repo-map.md`: the components, the study areas with their paths and rough size, what was skipped and why, and any rules about claims the repository imposes. Add one ledger unit per study area, recording its paths and the commit. If there is no repository, the study areas are whatever sources the user supplies (a website, documentation, a deck), divided the same way.

**Before the fan-out**, tell the user in two or three lines what is about to happen: the product as you understand it, the audiences (noting any you assumed), the depth, and roughly how many agents the run will start, counting the checks and follow-up waves and not the planned units alone. Do not wait for a reply; this is so that a wrong premise can be caught while it is cheap.

## Stage 3: study every area

Launch one **component analyst** per study area ([references/roles/component-analyst.md](references/roles/component-analyst.md)), all in one message so they run together. Each writes `components/<area>.md`.

These documents feed a product brief, so they describe what an area does, why it matters and to whom, how it is used and run, what a person needs to know to use it, who it suits, its upsides and risks, and what it could become. They are not source documentation, and an agent that returns an inventory of files and functions has missed the assignment.

## Stage 4: write the product document

One **product writer** ([references/roles/product-writer.md](references/roles/product-writer.md)) reads `intake.md` and every component document and writes `product.md`: what the product is, the refined value propositions, a table of capabilities, the markets it fits, the people who would want it, and the search terms a competitor hunt should start from.

Read it yourself against `intake.md` when it returns. Where the repository contradicts or extends the owner's account, record the difference in the run log; it is one of the most useful things the run produces. If a difference bears on who the product is sold to first or on what it may claim, tell the owner in a line now, without waiting for a reply. An answer that arrives before stage 7 costs nothing; one that arrives after it can cost the strategy.

At standard and deep depth, then launch the **product critic** ([references/roles/coverage-critic.md](references/roles/coverage-critic.md)) to look for parts of the repository nobody studied and capabilities the product document missed. Run a follow-up wave for what you accept, and have the product writer update `product.md` if anything new was found.

## Stage 5: the market and the competitors

Everything from here depends on reading the live web. Before launching anyone, probe it from this session: run one search, then open one page of each kind the research will lean on. That means a vendor's site, a forum or aggregator thread, a review site, and a social network through whatever search tool the host has for it. Review sites and social networks very often refuse automated readers, and a search tool can be connected and still have no credit. Record what you found in the ledger's `web` field and the run log, put the list of closed sources in every research brief so that twenty agents do not each rediscover it, and tell the user in a line which kinds are closed and what would open them. Do not wait for a reply; if access arrives later, the affected feedback documents are a cheap rerun.

If the host has no working web access at all, stop after stage 4, mark the run `incomplete` with that reason, and say so plainly. Competitor documents written from a model's memory would be out of date and unverifiable, and they would look exactly like real ones.

Launch two agents together:

- The **market analyst** ([references/roles/market-analyst.md](references/roles/market-analyst.md)) writes `market.md`: the categories, their size, how buyers buy, what is changing, where money is moving, and where the product's audiences pay attention.
- The **competitor scout** ([references/roles/competitor-scout.md](references/roles/competitor-scout.md)) builds a long list from `product.md`, filters it, and writes `competitors.md` with a ranked shortlist and the reasons for every cut.

Tell the scout the shortlist size for the chosen depth and every competitor the owner named, and on a later run give it the previous `competitors.md` so that earlier cuts stand unless the evidence has changed. Proceed on the scout's shortlist without stopping to ask: the cut list and its reasons are in the file, and adding a company later is a cheap rerun.

## Stage 6: research each competitor

Run two waves, the second after the first has returned, so the later agents can read the brief and spend their effort on their own question.

**Wave A, one agent per competitor.** The **competitor profiler** ([references/roles/competitor-profiler.md](references/roles/competitor-profiler.md)) writes `<company>-brief.md` (the same product information we gathered about ourselves) and `<company>-positioning.md` (how they present themselves and the exact words they use).

**Wave B, two agents per competitor.** The **growth researcher** ([references/roles/growth-researcher.md](references/roles/growth-researcher.md)) writes `<company>-growth.md`. The **feedback researcher** ([references/roles/feedback-researcher.md](references/roles/feedback-researcher.md)) writes `<company>-feedback.md` from reviews, forum threads, social posts and news.

At quick depth, one researcher per competitor reads all three role files and writes the four documents in that order.

**What buyers do instead.** The strongest competitor is often no product at all: the buyer builds the thing in-house, assembles it from tools already owned, or carries on without it. It has no website, so a shortlist of companies leaves it out, and a strategy that never studied it will be surprised by it. At standard and deep depth, add one unit in wave A for the status-quo entry the scout names: a profiler writes `competitors/<slug>-brief.md` from first-person accounts of how organisations do the job today (engineering and operations write-ups, conference talks, published practices, job descriptions). It needs no positioning or growth document.

**Checks.** At standard and deep depth, launch one **source checker** per competitor ([references/roles/source-checker.md](references/roles/source-checker.md)), which opens the cited pages and writes `competitors/checks/<company>.md`. Send the claims it marks back for correction and confirm the corrections were made, and have a document the checker calls unreliable rewritten by a fresh agent. Then launch the **competitor critic** to look for a competitor a buyer would name that the shortlist missed and for sources nobody reached, run a follow-up wave for what you accept, and put that wave's documents through one more source checker. At quick depth, sample the sources yourself as the orchestration reference describes.

Do not begin stage 7 until these checks are finished and acted on, the follow-up wave's included.

## Stage 7: synthesis and strategy

[references/strategy-documents.md](references/strategy-documents.md) defines every document in this stage. It runs in five steps, because the documents must agree with each other and a single agent writing all of them from forty inputs loses the thread.

1. **Landscape.** One writer reads `product.md`, `market.md`, `competitors.md` and every competitor document, and writes `landscape.md`. This is where the comparisons are made, once: which loved features we share, which competitor pain points we solve, the language everyone uses and the language nobody has claimed.
2. **Product brief.** One writer reads `intake.md`, `product.md`, `market.md` and `landscape.md` and writes `strategy/product-brief.md`, which fixes the positioning, the value propositions, the table of markets and audiences with their priorities, and the exact wording of every claim that is easy to overstate. Read it before going on. If it recommends something other than what the owner said (a different first audience, a claim set aside), check that it says so to the owner in a passage of its own, keeps the owner's statement on the record, and gives the cost of deciding the other way.
3. **Four writers in parallel**, each reading the landscape and the brief first and the source documents as needed: `go-to-market.md`, `pitches.md`, `website-content-strategy.md` and `product-opportunities.md`. Each ends with the decisions it needs from the owner.
4. **Execution plan.** One writer reads all five and writes `execution-plan.md`, turning their recommendations into ordered steps and gathering every decision only the owner can make into one numbered table. From then on, that table is the only list of owner decisions, and every other document refers to its numbers.
5. **Review.** One reviewer who wrote none of them reads the six strategy documents against `product.md` and `landscape.md`, trying to find what is inconsistent, overclaimed or unsupported, and writes `strategy/review.md`. Fix what it finds: small inconsistencies yourself, anything larger by returning the document to a writer with the finding.

Then read the six strategy documents together and sweep them:

- They use the same name for the product, the same value propositions and the same priorities as `product-brief.md`, and quote its fixed wordings exactly.
- Nothing marked Intended or Possible has turned into a present-tense claim, and copy meant for publication carries its markers.
- A search of the whole workspace for each phrase the product's claim rules forbid, and for each name that must be kept out, finds nothing. Search for the exact strings; a loose pattern produces false alarms and hides real ones.
- Decisions for the owner are cited by number, and the effort the execution plan totals fits the capacity the intake records, or the plan says what gives.

The review is applied once. Say in the run log that the set was revised after the review and not reviewed again, unless the depth is deep, in which case run a second reviewer over the revised set.

## The run log

`run.json` holds the status of every unit; `RUN-LOG.md` is the account of the run a person reads. Keep it current as you go, since it is how the owner, and the next run, find their way back in.

```markdown
# Run log: <product> market research

Internal. Last run: <date>. Depth: <quick | standard | deep>. Status: <complete | incomplete: reason>.

## Stages
A summary by stage, and the command that prints the full unit table
(`ledger.py table`).

## Decisions made during the run
Each judgment call with its reason: the product's scope, assumed audiences,
how areas were grouped, which competitors were cut, critic proposals accepted
and rejected, anything interpreted, any departure from this procedure, any
agent relaunched on another model. Decisions the owner made are marked as
theirs and dated, so that a later run does not reverse them.

## Where the repository and the owner's summary differ

## What the research found that changes the picture
The findings that should alter how the owner thinks about the product,
unfavourable ones included.

## Questions for the owner
The decisions that unlock most, by their numbers in the execution plan, each
with the recommendation. The full list stays in the execution plan. Add
anything only the owner can supply, such as access to a closed source.

## Gaps and things not verified
Thin, blocked and deferred units with their reasons; sources that could not
be reached; whether the live product was observed; what was not independently
checked; whether the strategy was reviewed again after it was revised.

## Running it again
```

## The navigation page

When the strategy is done, write `README.md` as the page a reader starts from. The set is long (a standard run produces dozens of documents), and a person who was not there needs to reach the right one in a click. Keep it to what helps them find things:

- what this is, the date, and that it is internal;
- **if you have five minutes**: the position in one line, who to sell to first, and where the next actions are;
- **find what you need**: a table from tasks to documents ("describe the product in one line", "know what we must never claim", "pitch a given audience", "answer why not a given competitor", "see what the product really has today");
- the strategy documents, in order, with what each holds;
- the research underneath, a grid of competitors against their documents and check records, and the component documents grouped by part of the product;
- how to read the labels and markers;
- what to keep in mind: the commits the product was read at, how fast the research ages, the main gaps;
- how it was made and how to run it again.

## Closing the run

Set the run's status in the ledger to `complete`, or to `incomplete` with the reason, and run the ledger check one last time. A run does not end in any other state.

Report in the host's and the user's own conventions. Lead with where the six strategy documents are, then the decisions you made that the owner may want to overturn (the competitor shortlist and any assumed audience first), the gaps, and the two or three findings that most change how the product should be presented. Then put the questions only the owner can answer in the message itself, numbered as in the execution plan and each with your recommendation, so that the owner can reply with a number and a word without opening a file. If the run was quick, limited by a budget or incomplete, say that it is a partial pass.

## What goes wrong

1. Strategy written before the research is checked, so that an invented quotation becomes a line in a pitch.
2. A competitor described from what the model remembers instead of from its pages as they are now.
3. A sample of public posts reported as a count or a percentage.
4. A competitor drawn as a strawman, which produces positioning that fails in front of a real buyer.
5. Something Intended or Possible written in the present tense in copy meant for publication.
6. Six strategy documents that each position the product a little differently.
7. Component documents that inventory files instead of explaining what the area is for.
8. Coverage thinned silently to fit a budget, and the report presented as complete.
9. An agent's account of its own thoroughness taken as evidence of it.
10. A full run started for a request that wanted an answer.
11. An agent cut off before it had written anything, because it held its document in context until the end.
12. A flat statement that a competitor lacks something, which one more search would have disproved.
13. A closed source discovered separately by every researcher, when one probe would have told the user in time to open it.
14. A competitor's incident offered as proof of our product's design.
15. Decisions for the owner scattered through six documents instead of standing in one numbered list.
16. The same claim worded six ways, one of them stronger than the product supports.
17. The lead stopping between stages to ask whether to continue, so that the run waits on a person who had already asked for it.
