# The Layer Above the Architecture

*On the ontological audit — the layer that has to be read before any AI architecture goes in.*

**Substrate · Reading Room · Edition 06**

---

Most AI installations into operating businesses fail at the wrong layer.

The technical work is fine. The workspace is correctly structured, the models are credible, the agents do the work they were instructed to do. The architecture is sound. And the company gets less out of it than the architecture should be able to deliver.

The reason is structural. The architecture was installed around an inherited frame — the company's implicit theory of itself — and the frame was wrong. Not catastrophically wrong. Just wrong enough that every downstream choice now compounds in a direction that doesn't match what the business actually is.

Strategy applied to the wrong picture compounds in the wrong direction. Architecture applied to the wrong picture does the same thing faster.

This essay is about the layer that has to be read before any architecture goes in.

## The architecture is real

Interpretable Context Methodology, published by Van Clief and McDermott in March 2026, formalizes what serious AI practitioners had been arriving at independently for the prior two years. The thesis is direct: folder structure is the architecture. The workspace is laid out as a tree of folders, each holding a small amount of context relevant to the work routed to it, and the AI assistant reads its way through the tree by following the structure of the folders themselves. No orchestration code. No agent frameworks stacked on top of each other. The folders are the order of operations; the files inside them are the working memory; the AI is the thing that reads them.

This isn't a novel claim from someone selling a course. It's an old idea: computers have run on files in folders for fifty years, and Unix engineers have been doing this for nearly that long. ICM names the pattern, formalizes the five-layer architecture, and demonstrates why for the kind of work most operating businesses actually do, plain files win against more infrastructure.

For the practice I run, ICM is the technical foundation. I converged on the pattern independently before encountering the paper, and have been building workspaces this way across several ventures since. The methodology is real and examinable. I cite Van Clief and McDermott when I introduce it, and link to the paper when readers want the long version.

## Where the installations fail

Despite all of that, ICM installations into operating businesses tend to produce one of two outcomes.

The first outcome: the workspace accelerates existing work without changing what the work is *for*. The founder gets faster outputs of the same things they were already producing. The company can do more of what it was already doing. This sounds like a win. But if what the company was already doing was itself misaligned with what the company structurally is, the architecture has now made that misalignment harder to see and faster to compound. The team executes more efficiently on the wrong picture. Six months in, the founder cannot explain why a system that was supposed to clarify the work has made the work harder to course-correct.

The second outcome: the workspace fails to gain traction. The folder structure mirrors the org chart the founder grew up with — sales, marketing, ops, engineering — and the workspace ends up being a digital version of the same compartmentalization the company has been quietly outgrowing. People don't use it. The architecture is correct in form and wrong in fit.

Both outcomes have the same root cause. The architecture was built around an *unexamined* picture of the business. The picture itself was never read.

## What was missed

ICM's five layers, in the order the methodology presents them, are: CLAUDE.md (workspace identity), workspace CONTEXT.md (task routing), stage CONTEXT.md (stage contracts), reference material (standards and voice), and working artifacts (outputs). The methodology is rigorous about how these layers relate to each other and what they hold. It is silent on what the workspace identity *should be* — who the business actually is.

The silence is structural. ICM is an architecture for installing AI workspaces. The question of what the workspace should be installed *around* is not a workspace question. It's a business question that has to be answered first.

In practice, what fills the silence is the founder's existing self-description. The marketing site. The deck. The org chart. The story the company has been telling itself for long enough that the story has hardened into operating reality. The workspace gets built around that.

And here is the part most operators don't see until it's six months too late: the story almost never matches the operating reality. The decisions a company actually makes — what gets prioritized when the budget is tight, who gets escalations, what the team mobilizes for under pressure, what the customer is actually paying for — these reveal a different picture from the one in the deck.

The architecture is supposed to materialize the company's structure. If the structure encoded in the workspace is the one in the deck rather than the one in the operating reality, the architecture materializes the wrong thing.

## The layer above

What I install before the architecture is an ontological audit. It is a structured reading of the company's foundational frame, conducted through six questions:

**1. What is this business?** Not at the function level — what category, what industry, what segment — but at the level beneath the function. What does the company actually do when no one is watching? What does the team mobilize for under pressure? What is the underlying transaction the entire operation is organized around?

**2. What exists inside it?** What are the entities the work actually moves through — customers, products, regions, modes — and which of those are primary versus secondary? Which entities does the team treat as load-bearing in conversation, and which are background?

**3. What is the customer actually buying?** The stated answer is whatever the marketing site says. The real answer is whatever the customer would still pay for if you stripped everything else away. These are almost never the same answer.

**4. Where is the structural mismatch?** Between the founder's theory of the company, the team's experience of the company, and the customer's experience of the company. Mismatch is normal at the experience layer; mismatch at the substrate layer is where leverage leaks.

**5. What is leaking leverage?** Where is execution being applied to the wrong picture? Where is the team being asked to optimize for something the company isn't actually structured to deliver? The answers are usually visible to the team and invisible to the founder.

**6. What is the corrected frame?** A clean articulation, after the audit surfaces the distortions, of what the company actually is at the substrate level. This is what the architecture then gets built around.

The six questions take a structured set of conversations and a written document to answer. The document is the audit. For most founders who go through this, it is the clearest picture they have ever had of their own company — not because the founder didn't know, but because the structural picture was never extracted into a single document. The picture had been living distributed across the founder's intuition, the team's frustrations, and the customer's reported reasons for renewing.

## What changes when the audit runs first

Two things change.

The first thing: the architecture materializes the right picture. The workspace identity — the highest ICM layer — is grounded in what the company actually is, not what it was told to be. The routing follows the structural reality, not the inherited org chart. The reference material encodes the actual voice and standards of the company. The artifacts produced by the workspace map onto the work that the business actually does. The architecture works because it was applied to the corrected frame.

The second thing, which matters more: the architecture becomes interpretable to the team. When the workspace structure matches the operating reality, the team recognizes it. They use it. The folder tree feels like the company. The architecture stays in use after the installer leaves because it was built around something the team already implicitly knew but had never seen named.

Without the audit, the architecture is technically correct and operationally drifting. With the audit, the architecture is technically correct and structurally aligned, and the alignment is what makes the architecture compound rather than calcify.

## The order matters

The order is: audit, install, hand off. The audit reads the company. The install builds the architecture around the corrected picture. The hand-off trains the team to run it.

In practice, most consulting starts at install. Most strategy work starts at the strategy layer, which sits two levels above the substrate. Most AI deployment starts at the workspace layer with no audit at all. Each of these can produce visible outputs. None of them, by themselves, produces a system that compounds. Compounding requires the architecture to be installed around the right picture, and the right picture only surfaces after the substrate is read.

ICM's five layers are the architecture. The audit is the layer above them. The audit doesn't replace the architecture; it determines what the architecture is for.

That's the work.

---

*Full methodology: jaydenforshee.com — "The Ontological Layer." ICM source: Van Clief & McDermott, 2026 (arXiv:2603.16021).*

---

*Substrate · Practice of Jayden Forshee · 2026*
