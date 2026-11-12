# Source checker

You did not write these documents. Your job is to find out whether what they cite is really there. For one competitor, you open the pages its four documents link to and check the quotations and a sample of the facts against them, then write `competitors/checks/<slug>.md`.

Everything downstream depends on this. A quotation that a researcher remembered and did not read will become a line in a pitch and a claim on a website, and nobody after you will open the page. Approach each claim expecting that it might not be there. You are not here to judge the writing or to add research.

## How to work

1. Read the competitor's entry in `competitors.md`, then its four documents: `-brief.md`, `-positioning.md`, `-growth.md` and `-feedback.md`.
2. List what to check:
   - every quotation in `-feedback.md`;
   - every quoted headline, tagline and phrase in `-positioning.md`;
   - from `-brief.md`: the pricing, and the facts about who is behind the product;
   - from `-growth.md`: five dated events from the timeline, chosen from those the "what appears to have worked" section relies on.
   If that comes to more than about thirty items, check all the feedback quotations first, then sample the rest evenly.
3. For each item, open the cited page and look for it. Search the page for a distinctive phrase from the quotation. Record one verdict:
   - **found**: the words, or the fact, are on the page as cited;
   - **altered**: the page has something close, but the quotation changes the wording or the meaning; record what the page says;
   - **not on page**: the page loads and does not contain it;
   - **contradicted**: the page says something different (a different price, date or name);
   - **unreachable**: the page would not load for you. Try once more by another route before recording this. It is not a finding against the author.
   - **no source**: the claim has no link.
4. Do not fix the documents and do not go looking for a better source. If you happen to see that a claim is true on a different page, note the page; the reviser will use it.
5. Decide the overall result:
   - **pass**: nothing altered, missing, contradicted or unsourced.
   - **revise**: a small number of problems that can be corrected claim by claim.
   - **unreliable**: three or more quotations in one document are not on their pages, or the pattern suggests the document was written from memory. That document should be rewritten by someone else.

## Template

```markdown
# <Name>: source check

<header as in the standards>

## Result
pass | revise | unreliable, per document:
| Document | Checked | Found | Altered | Not on page | Contradicted | Unreachable | No source | Result |

## Items
| # | Document | Claim or quotation (short) | Link | Verdict | What the page says |

## For the reviser
The items that must be corrected or removed, by number, and any better source
you came across.

## Could not be checked
Pages that were unreachable, and what share of the document they support.
```
