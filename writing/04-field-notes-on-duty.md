# Field Notes — Installing the Architecture in a Co-Founded Company

*Build log from On Duty, a fleet safety platform in active development.*

**Substrate · Reading Room · Edition 04 · Field Notes from the Build**

---

On Duty is a B2B SaaS platform for fleet driver safety — coaching, compliance, and retention for companies that operate commercial vehicles. I co-founded it with my stepdad. He owns the sales and client side; I own the technical and architectural side. The company is in active development with mock data, four active tenants, and a pilot in progress with a commercial concrete operator running roughly ten drivers through the system.

This is a build log from the operating architecture I have been installing inside it for the last year. The methodology is the same one I install for clients. The reason I am publishing the build log in the Reading Room is that the question of *whether the methodology works in a real business environment with a real non-technical operator running it daily* has to be answered somewhere, and the most direct way to answer it is to show what the architecture looks like and what it has produced.

---

## What the audit surfaced

When I started installing the architecture, the stated picture of On Duty was *"a fleet safety SaaS platform."* That is the label. It is on the marketing materials. It is how the company is described at industry conferences. It is what an investor would expect to evaluate.

The audit found something different underneath.

What On Duty actually is — when you watch what the customers are responding to, what the pilot operator is paying attention to, what determines whether a tenant renews or churns — is a **compliance and litigation defense product wearing safety language.** Fleet operators do not buy safety platforms because they want their drivers to be safer in the abstract. They buy them because the legal exposure of operating commercial vehicles in the current US tort environment is catastrophic, and they need a documented system that demonstrates due diligence in the event of a nuclear verdict. The safety is real. The reason they pay for it is liability.

This sounds like a small distinction. It is not. The stated ontology — safety SaaS — implies that the most valuable output of the product is improved driver behavior. The actual ontology — compliance and litigation defense — implies that the most valuable output is a comprehensive, court-admissible audit trail. *Those are different products even though they look the same from the outside.* If we built the product around the stated ontology, we would optimize for driver coaching engagement metrics. If we built it around the actual ontology, we would optimize for the documentation, traceability, and defensibility of the system itself.

The architecture I installed reflects the corrected picture.

---

## The shape of the install

The workspace has eight top-level domains, each mapped to a specific function the company actually performs. I will describe them in shape only — the specifics of the routing logic, the context files, and the reference material are bespoke to On Duty and not the kind of detail a build log should expose. What is useful here is the structural pattern.

**Sales and outreach.** The workspace used daily for prospect identification, outreach sequencing, and pipeline management. The architecture is calibrated to the specific buyer — operations directors and safety officers at fleet operators between $5M and $50M in revenue. Every output the system produces is calibrated to that buyer's specific vocabulary, decision criteria, and procurement process. The material it produces lands differently from generic sales copy because the architecture knows the buyer at a structural level.

**Compliance and audit preparation.** This is the workspace that translates the actual ontology into operating output. When a tenant is preparing for a DOT audit or building documentation for legal defensibility, this workspace produces the artifacts they need in the format their auditors and attorneys expect. The corrected ontology is encoded directly into the routing logic — the system treats compliance documentation as the primary output, not as a side effect of safety coaching.

**Client success and retention.** Onboarding new tenants, monitoring health scores, running the 30-day pilot framework, executing the renewal playbook. Each of these is its own stage with its own context, but they share a coherent picture of what success looks like inside On Duty — calibrated to the corrected ontology rather than the inherited one.

**Three other operational workspaces** handle marketing content, internal operations, and the technical build itself. They mirror the same structural pattern: numbered folders for stages, plain markdown for context, reference material that captures industry knowledge in a form the AI can use.

The architecture is built on Interpretable Context Methodology. Every file is plain markdown. The whole system lives in a Git repository that can be cloned, edited, extended, and operated without my involvement. **There is no platform to depend on. There is no proprietary configuration. There is no vendor lock-in.**

---

## What is working

A few patterns have surfaced over the last year of running the system.

**The non-technical operator pattern is real.** My co-founder uses the architecture daily. He edits the markdown files himself when he notices something off. He has added two workspaces on his own that I did not build, by copying existing ones and modifying them. **The system has grown beyond what I installed, in directions I did not anticipate, because the architecture was designed to be operable rather than dependent.** This is the most important validation of the methodology, because it is the hardest thing for AI consulting to deliver. Most installs degrade or become dependent within six months. This one has compounded.

**The corrected ontology produced unexpected operational clarity.** Once the workspace was built around compliance-and-litigation-defense rather than around safety-as-such, decisions that had been chronically slow started resolving quickly. Pricing conversations got easier because the value proposition was clearer. Sales calls converted faster because the messaging matched what the buyer actually wanted to hear. Product roadmap discussions stopped fragmenting because there was now a stable picture of what the company was prioritizing for. **None of this was the architecture's direct output. It was the side effect of operating from the corrected frame daily.**

**The audit document keeps paying compound interest.** When I wrote the audit, I treated it as a one-time artifact — a document that explained what I had surfaced so the install could be built against it. A year in, my co-founder still references it when he is making decisions that aren't covered by any workspace. The corrected ontology has become the foundation for how he reasons about the company, not just the foundation for what the system produces. **The audit was the highest-leverage piece of work in the entire engagement, even though most of the visible output came from the install.**

---

## What is not working

A build log that only reports wins is marketing. Here is what is still rough.

**The CSV duplicate user issue is unresolved.** When tenants upload driver lists, the deduplication logic has a known bug that creates duplicate user records in edge cases. This is a technical problem, not a methodological one, but it shows up here because it is the kind of friction the corrected ontology cannot fix. *Architecture can solve coordination problems. It cannot solve implementation bugs.* Distinguishing between those two has been a useful discipline.

**Email delivery from the platform to external recipients has been unreliable.** Same category as the CSV problem. The architecture is sound; the technical execution at the platform layer has gaps that are being worked through.

**The non-technical operator has hit a ceiling on workspace creation.** Existing workspaces extend well. New workspaces created from scratch — for a function the existing architecture didn't already cover — run into the limits of what the methodology can do for someone without technical training. **The architecture is operable but not yet teachable, for the non-technical operator at this skill level.** This is an open problem.

**The architecture has been revised twice.** The audit was correct, but the install's first version did not fully reflect the corrected ontology — there were workspaces that, on six months of use, turned out to be calibrated to the stated picture rather than the actual one. Revising them required reopening the audit, refining the corrected ontology, and rebuilding three workspaces. **The methodology is iterative in practice even when it appears clean on paper.**

---

## What the build log is for

The methodology works. The architecture has held up. The non-technical operator has been able to run and extend the system. The corrected ontology has produced compounding clarity over twelve months.

This is the evidence. The reason it is in the Reading Room is that anyone evaluating the practice can read it and see the work in motion — what the audit produces, what the install consists of, what the install does over time, where it is solid and where it is still being refined. Most AI consulting work is invisible after delivery. This one is open.

More Field Notes will follow as the build continues and as new things become worth reporting.

---

*Substrate · Practice of Jayden Forshee · 2026*
