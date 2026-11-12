# Market Research Skill

Market Research is a skill for coding agents that takes a product from "here is the repository and a few sentences about it" to a set of documents its owner can act on: what the product is and who it is for, who it competes with and how those companies talk to their customers, what their users love and resent, and a positioning, go-to-market, pitch, website and execution plan built on that evidence.

Asked for market research in one sitting, an agent tends to write a plausible strategy from what it already believes about the category, with a few searches for colour. The result reads well and rests on very little: the product is described from its README, the competitors are the ones the model happened to remember, and nothing separates what was checked from what was assumed. This skill replaces that with a staged procedure in which teams of agents study every part of the product, research each competitor from three independent angles, and write everything down, so that the final documents can point to what they rest on.

It is generic. Nothing in it is tied to a product, a market or a company, and it is designed to be run repeatedly: on a different product, or again on the same one when the product or its competitors have changed.

## How it works

The run has seven stages. Each writes files into one workspace, and each later stage reads only those files, which is what allows a run to stop and resume, a single stage to be redone, and a competitor to be added afterwards. One agent acts as the lead: it holds the plan, briefs the other agents, checks what they return and keeps a run log.

| Stage | What happens | Who | Output |
|-------|--------------|-----|--------|
| 1. Intake | Collects the owner's summary of the product, drafts value propositions and describes the audiences. Asks for a summary once if none was given. | Lead | `intake.md` |
| 2. Map | Surveys the repository, sorts it into components and groups them into study areas. | Lead | `repo-map.md` |
| 3. Study | One analyst per study area writes a product-minded account of it: what it does, why it matters, how it is used and run, who it suits, its upsides and risks, and where it is heading. | Team, in parallel | `components/<area>.md` |
| 4. Product | One writer reads all of that and describes the product as a whole: refined value propositions, the markets it fits, the people who would want it. | One agent | `product.md` |
| 5. Market and competitors | An analyst researches the market itself (categories, size, buyers, trends, where money is moving, where the audiences pay attention) while a scout builds a long list of competitors, filters it and ranks a shortlist. | Two agents, in parallel | `market.md`, `competitors.md` |
| 6. Competitors | For every shortlisted competitor: a profiler writes a brief and a record of its positioning and language; then a growth researcher and a feedback researcher cover how it grew and what its users say. | Three agents per competitor, in two waves | `competitors/<company>-brief.md`, `-positioning.md`, `-growth.md`, `-feedback.md` |
| 7. Strategy | One writer makes the cross-competitor comparisons in a landscape document; a second fixes the positioning and priorities in the product brief; four writers then produce the go-to-market plan, the pitches, the website content strategy and the product opportunities; one turns them into an execution plan; and a reviewer who wrote none of them checks the set. | Eight agents, in five steps | `landscape.md`, `strategy/*.md` |

The stages are described in full in [skill/SKILL.md](skill/SKILL.md), which is short enough to read before you install it. Each role has its own brief under [skill/references/roles](skill/references/roles), the final documents are specified in [skill/references/strategy-documents.md](skill/references/strategy-documents.md), and the mechanics of running the agents are in [skill/references/orchestration.md](skill/references/orchestration.md).

### How the agents are kept honest

A run of this size fails in predictable ways: agents describe a thorough search more readily than they perform one, coverage is quietly thinned when the work gets long, and the lead loses track of what was done. Three mechanisms address this.

**A ledger.** Every assignment is a unit in `run.json` with its outputs and a status: planned, in progress, done, thin, blocked, deferred, stale or dropped. A small script, `skill/scripts/ledger.py`, checks the ledger against the files after every update: that each finished unit has its documents, that evidence documents carry links, that links between strategy documents resolve, that anything thin, blocked or deferred says why, and that a run marked complete has nothing open. A run ends as complete or as incomplete with a stated reason, and in no other way. The script confirms that the record and the files agree; it cannot tell you whether the research is good.

**Independent checks.** Nobody checks their own work. After the competitor research, a source checker per competitor opens the cited pages and looks for every quotation and a sample of the facts, and a document with several quotations that are not on their pages is thrown away and rewritten by a different agent. A coverage critic, which planned nothing, looks for parts of the repository nobody studied and for a competitor a buyer would name that the shortlist missed; what it finds becomes a follow-up wave. A reviewer who wrote none of the strategy reads all of it for inconsistency, overclaiming and unsupported statements.

**Self-contained briefs.** An agent inherits nothing from the lead, so every brief names the files to read, the one thing to write, what the neighbouring agents own, and five rules repeated word for word. Each agent must say in its report that it read the standards, and reports in a fixed form that includes what it could not find. Each also has stop conditions: when the assignment is not what the brief says, or web access does not work, it stops and reports instead of improvising.

### Two registers

The skill keeps two kinds of document apart, because they fail in opposite ways.

Documents about your own product are aspirational. Their job is to capture what the product is for and where it is going, so intent and projection are wanted; a brief that describes only what has shipped undersells the product. What they may not contain is an invented fact. Every statement about the product is recognisably one of four kinds: **Today** (it exists and an agent saw it), **Intended** (you said so, or a plan says so), **Possible** (the writer's own view of what the product could become, labelled as an opinion), or **Open** (unknown or undecided). The distinction is carried through to the pitches and the website copy, which draw only on Today and Intended and mark the lines that depend on something not yet built.

Documents about competitors and the market are evidence-led. Every claim carries a link to a page the agent opened during the run, and nothing may be cited from the model's memory. Quotations are verbatim, because the words competitors and their users choose are themselves the data, and "not found" is an accepted answer where a figure is unpublished or a site could not be reached.

Invented quotations are the likeliest serious failure in work of this kind, which is why the source checkers exist. Before any web research starts the lead also confirms that the host's web access works, and stops with the product documents if it does not.

The full standard is in [skill/references/standards.md](skill/references/standards.md).

## What you get

```
market-research/<product>/
  run.json                          the ledger: every unit, its outputs and its status
  README.md                         run log: decisions, gaps, questions for you, index
  intake.md                         your summary, value propositions, audiences
  repo-map.md                       components and study areas
  components/<area>.md              one document per study area
  product.md                        the product, its markets, users and value
  market.md                         categories, size, buyers, trends, channels, why now
  competitors.md                    long list, filter decisions, shortlist
  competitors/<company>-brief.md
  competitors/<company>-positioning.md
  competitors/<company>-growth.md
  competitors/<company>-feedback.md
  competitors/checks/<company>.md   the source checker's verdict on each citation
  landscape.md                      cross-competitor synthesis
  strategy/product-brief.md         description, positioning, pitch, market, audiences
  strategy/go-to-market.md          growth strategy and every channel
  strategy/pitches.md               one pitch per market and audience combination
  strategy/website-content-strategy.md
  strategy/product-opportunities.md
  strategy/execution-plan.md        ordered steps with owners and done-when
  strategy/review.md                the independent reviewer's findings
```

The landscape is where the comparisons are made: a table of the features users love in competitors that your product also has, a table of the competitor pain points your product solves or could do better (including the rows where the honest answer is that it does not), the language the whole category uses, and the ground nobody has claimed.

The run log records every judgment call the lead made on your behalf, such as which competitors were cut and why, along with the places where the repository and your own summary of the product disagree. That last list is often the most useful thing a run produces.

## Scale

This is a large job. A standard run on a repository with ten study areas and seven shortlisted competitors starts about fifty agents, most of them doing web research, and takes a correspondingly long time and a large number of tokens. The skill has three depths, and you can name one when you start:

| Depth | Study areas | Competitors | Independent checks | Agents, roughly |
|-------|-------------|-------------|--------------------|-----------------|
| Quick | up to 5 | 3 to 4, one researcher each | the lead samples sources | 20 |
| Standard (default) | 6 to 14 | 6 to 8, three researchers each | a source checker per competitor, each critic once | 45 to 60 |
| Deep | as many as the repository needs | up to 12, three researchers each | checkers including the market, critics until clean | 80 or more |

Depth changes how much is covered and how much is double-checked. It never relaxes the rules about sources.

You can also set a budget as a maximum number of agents. The lead then reserves the synthesis and the checks first, spends what is left on study areas and competitors in priority order, and records whatever the budget excludes as deferred, so that a cheaper run is visibly a partial one and never a thinner one presented as complete. If the budget cannot fund a usable run, it says so before starting anything.

Before the first team is launched, the lead says in a few lines what it understood the product and audiences to be, the depth, and how many agents it is about to start, so that a wrong premise can be caught while it is cheap.

The full run starts only when you ask for the research or its documents. A question ("who are the obvious competitors here?"), a review of one pitch, or advice on positioning is answered in the conversation, using the skill's method and any workspace that already exists, without starting teams or writing files. A request for part of the work runs only the stages it needs: competitor analysis alone stops after the landscape document, and a pitch or positioning request on an existing workspace rewrites only the relevant strategy documents.

## Install

Clone the repository once:

```sh
git clone https://github.com/chrischabot/market-research-skill.git ~/Projects/market-research-skill
```

Then link its `skill` folder into the skills directory of each host you use.

### Claude Code

```sh
mkdir -p ~/.claude/skills
ln -s ~/Projects/market-research-skill/skill ~/.claude/skills/market-research
```

Invoke with `/market-research` or ask Claude to research the market for the product in the current repository.

### Codex

```sh
mkdir -p ~/.agents/skills
ln -s ~/Projects/market-research-skill/skill ~/.agents/skills/market-research
```

Invoke with `$market-research`.

### Pi

```sh
mkdir -p ~/.pi/agent/skills
ln -s ~/Projects/market-research-skill/skill ~/.pi/agent/skills/market-research
```

Invoke with `/skill:market-research`.

### Cursor

```sh
mkdir -p ~/.cursor/skills
ln -s ~/Projects/market-research-skill/skill ~/.cursor/skills/market-research
```

Invoke `/market-research` or ask Agent to use the skill.

Cursor and Pi also read `~/.agents/skills`, and Cursor also reads `~/.claude/skills`, so a link made for Codex or Claude Code may already serve them. Each host should see only one copy.

### Updating

Every host links to the same clone, so one pull updates them all:

```sh
git -C ~/Projects/market-research-skill pull --ff-only
```

## Usage

Run it from the product's repository, and give it a few sentences on what the product is, why someone would choose it, and who pays. Name any other audience it has to convince, such as investors, and any competitor you already know about.

```text
/market-research Tallyroom is stock control for independent bookshops. A shop can see what it has without closing for a stock-take, and the ordering suggestions stop the owner over-buying. Customers are owners with one to three branches; later, distributors may pay for anonymised sell-through data.
```

If you leave the summary out, the skill maps the repository and then asks for it, once. After that it runs to the end without further questions, making its own decisions and recording them in the run log where you can overturn them.

Later runs work on the same workspace:

```text
/market-research resume
/market-research add Shelfwise as a competitor
/market-research the audience has changed: we are now selling to chains, not single shops
/market-research refresh the competitor research
/market-research quick run, four competitors at most
/market-research standard depth, no more than 30 agents
```

Changing an early stage marks every later stage that read its output as stale and redoes them, because a strategy built on a superseded product document is wrong in ways that are hard to notice. Adding a competitor researches that one alone and then rewrites the synthesis and strategy; dropping one sets its documents aside and does the same.

A later run costs less than the first. Each study area records the commit it was written against, so a refresh re-studies only the areas whose source has changed. Competitors that were considered and cut stay cut unless the evidence has changed, and decisions you made in an earlier run are kept.

A product without a repository works too: point the skill at a website, documentation or a deck, and those become the study areas. The skill is not limited to software sold to businesses. The intake records what kind of product it is (a developer tool, a business application, a consumer app, an open-source project, a physical product, a service), and each researcher adapts its sources and channels to that.

## What it depends on, and its limits

The skill is a set of instructions, not a program. The agent researches with whatever web search, browsing and social search tools its host provides, and those tools set the reach of the competitor research. It was written for hosts that can run agents in parallel; where a host cannot, the lead performs each role in turn, which is slower and puts more strain on one context.

The quality of a run depends on the model doing the work and on the summary you give it. Competitor research goes stale within months, which is why the skill has a refresh mode. User feedback gathered from public posts is a sample with biases, and the skill reports themes in words and does not count them. None of this replaces talking to customers; the execution plan it writes will usually tell you to do so.

Researchers only read public pages. They do not create accounts, start trials, submit forms or contact anyone, and they keep unreleased details of your product out of search queries.

## Development

```
skill/
  SKILL.md                          the lead's procedure
  agents/openai.yaml                Codex display name and default prompt
  scripts/ledger.py                 checks run.json against the workspace; prints the stage table
  references/
    orchestration.md                ledger, budget, briefs, reports, checks, carry-over
    standards.md                    the two registers, stop conditions, report format; read by every agent
    example-intake.md               a worked example of stage 1
    strategy-documents.md           every stage 7 document
    roles/                          one brief per agent role
tests/test_ledger.py                tests for the ledger script
```

There is nothing to build. The ledger script needs Python 3.8 or later and only the standard library; without Python the lead keeps the ledger by hand under the same rules. An edit reaches every host linked to your clone.

```sh
python3 -m unittest discover tests
```

## Acknowledgements

The orchestration borrows from two skills that do multi-stage, multi-agent work well. From [shadcn/improve](https://github.com/shadcn/improve): briefs written for a reader with no context, critical rules repeated in every brief because agents do not inherit them, stop conditions in place of improvisation, the lead re-checking what agents report, and stamping work with the commit it was written against so a later run can detect drift. From [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill): the separation of a guidance mode from the full workflow, a ledger of coverage units that is validated by a script, coverage critics, the rule that the agent that checks a claim is never the one that made it, budgets that reserve verification before exploration, and explicit terminal states.

## License

[MIT](LICENSE).
