# Why Folder Structure is Architecture

*On Interpretable Context Methodology, and why the cleanest AI system is one that does not look like an AI system.*

**Substrate · Reading Room · Edition 02**

---

Most AI systems being sold to companies right now are too complicated for what they actually need to do.

The standard picture goes like this: you hire a developer or a consulting firm to build you an AI system. They use a framework — LangChain, CrewAI, AutoGen, something similar. They write Python code that orchestrates multiple AI agents talking to each other. They deploy it on a server. They build dashboards to monitor it. They charge you anywhere from twenty thousand to several hundred thousand dollars depending on the scope. When something goes wrong, only they can fix it, because only they understand the code that holds the whole thing together.

For the rare workflow that genuinely needs concurrent multi-agent coordination, this is the right architecture. For the vast majority of business workflows that get sold this way, it is overkill — and the overkill carries real costs. The system is opaque. Your team cannot modify it without involving the developer. Every change requires a deployment. Every update is a project. The technology you bought to make your business faster ends up making your business slower, because the technology now has its own maintenance overhead.

There is a cleaner way. It is documented in a 2026 paper by Jake Van Clief and David McDermott called *Interpretable Context Methodology* — ICM for short. The methodology takes ideas from Unix engineering in the 1970s, multi-pass compilation in the 1980s, and infrastructure-as-code in the 2010s, and applies them to a problem that has only existed for a few years: how do you structure AI systems so they actually work for the businesses operating them?

This essay is about why I install ICM-based architecture for every client, and why I think it is the correct technical foundation for almost every AI system a real business actually needs.

---

## The central claim

ICM's claim is structural: **folder structure is agent architecture.** Instead of writing application code to coordinate AI agents, you organize the prompts, context files, and reference material into a hierarchical folder system. One agent reads the right files at the right moment. The folder structure does the work that a multi-agent framework would otherwise do in code.

When you read this for the first time, it sounds like a downgrade. Folders are old. Files are old. Markdown is plain text. Surely a modern AI system needs something more sophisticated than that. But the simplicity is the point. Here is what folder-based architecture actually gets you that framework-based architecture cannot:

**Anyone can read it.** Every instruction, every context file, every routing decision is a plain markdown file. A non-technical operator on your team can open the folder, read what the system does at each step, and edit any of it with a text editor. The system has no hidden state, no proprietary configuration, no black box. *The architecture and the documentation are the same thing.*

**Anyone can modify it.** Changing how the system behaves does not require a developer. It requires editing a markdown file. If a workflow needs an additional step, you add a folder. If a prompt is producing the wrong tone, you edit the text. If the order of operations is wrong, you renumber the folders. The control surface that would normally live in code now lives in the filesystem, and the filesystem is something every operator already knows how to use.

**Everything is portable.** A workspace is a folder. You can copy it, version it in Git, email it as a zip file, hand it to another team member, or move it to a different machine. There is no server to deploy, no environment to configure, no dependency to manage. *The architecture goes wherever the folder goes.*

**Every intermediate output is inspectable.** When an AI agent finishes one stage of work and hands off to the next stage, the handoff is a file. You can open the file, read what was produced, and edit it before the next stage runs. If something goes wrong, you can see exactly where. There is no need to build a dashboard to monitor the system, because the system's state is already a folder full of files you can look at.

---

## Why this works

This is not new architecture. It is borrowed architecture, applied to a new problem.

The Unix designers in the 1970s figured out that small programs connected through plain text were more powerful than large programs that tried to do everything. The principle was: each program does one thing well, the output of one program becomes the input to another, and plain text is the universal interface. Pipelines like `find | grep | sort | uniq` are still in daily use fifty years later, because the architecture is fundamentally sound.

The compiler engineers of the 1980s figured out that complex transformations were more reliable when broken into stages, with each stage reading the output of the previous one and writing its own intermediate representation. A modern compiler has lexing, parsing, semantic analysis, optimization, and code generation as separate passes, and each pass is independently inspectable and replaceable.

The infrastructure-as-code movement of the 2010s figured out that production systems should be defined as files in a repository, not as configurations in a server somewhere. Terraform, Kubernetes manifests, Ansible playbooks — all built on the idea that the deployment artifact and the source of truth should be the same thing, and that thing should be plain text in a folder.

ICM applies these three traditions to AI systems. **Each stage of the workflow does one thing well. The output of one stage becomes the input to the next. Everything is plain markdown in a folder structure that doubles as both the source of truth and the deployment.** This is fifty years of software engineering wisdom, finally applied to AI orchestration.

The reason it works is not that the methodology is clever. The reason it works is that the methodology refuses to be cleverer than it needs to be. It uses the simplest possible substrate — folders and text files — and lets the structure of those substrates do the work that more complicated architectures spend code trying to recreate.

---

## What an ICM workspace actually looks like

A workspace for a content production pipeline might look like this:

```
my-business/
├── CLAUDE.md
├── CONTEXT.md
├── stages/
│   ├── 01_research/
│   │   ├── CONTEXT.md
│   │   ├── references/
│   │   └── output/
│   ├── 02_draft/
│   │   ├── CONTEXT.md
│   │   ├── references/
│   │   └── output/
│   └── 03_publish/
│       ├── CONTEXT.md
│       ├── references/
│       └── output/
└── _config/
    ├── voice.md
    └── conventions.md
```

That is the entire system. There is no application code anywhere. The numbered folders represent the stages of the workflow. Each stage's `CONTEXT.md` is a markdown file that tells the AI what to do at that step — what inputs to read, what process to follow, what outputs to produce. The `references/` folders hold the company-specific knowledge each stage needs: voice guidelines, design conventions, domain knowledge. The `output/` folders are where the agent writes its work, and where the next stage reads from. The `_config/` folder holds the company's reference material that every stage might need to access.

When the agent runs, it reads the workspace's `CLAUDE.md` to understand the overall structure, then navigates to whichever stage it is currently executing, reads that stage's `CONTEXT.md`, loads the relevant references, and produces output to the `output/` folder. The next stage reads from there, and the cycle continues.

A non-technical operator who wants to change how the system writes can open `_config/voice.md` and edit the voice guidelines directly. The next time the workflow runs, the new guidelines are in effect. There is no deployment, no compile step, no developer needed. The text file *is* the configuration.

This is what I install for every client. The exact folder structure differs based on what the audit surfaced — every business has a different ontology, and the architecture has to mirror the specific structure of each business — but the underlying methodology is the same. **Folders for stages. Markdown for context. Plain text everywhere. Git for version control. No server. No proprietary platform. No vendor lock-in.**

---

## Why this is the right foundation for ontological work

The reason ICM is the correct technical foundation for ontological work specifically is that *the architecture has to be able to mirror the structure of the business with high fidelity.* You cannot install a generic AI system on top of a corrected ontology and expect the correction to hold. The architecture has to reflect the specific structural reality of the company — what is primary, what is secondary, what relates to what, where the work actually flows.

In a framework-based AI system, the structure of the business is hidden inside application code. The developer encodes the workflow logic, and the workflow logic encodes some implicit picture of what the business is. If that picture is wrong, or if the picture changes, the code has to be rewritten. The cost of misalignment is high, and the cost of correction is high, so the system tends to stay misaligned.

In an ICM workspace, the structure of the business is explicit. The folder names are the structural categories of the company. The numbered stages are the actual workflow. The reference files are the actual knowledge. **If the audit surfaces that a software company is really a knowledge-transfer service, the workspace can be rebuilt to reflect that — the folders rename, the stages reorder, the references update, and the corrected ontology is now encoded in the operating layer of the business.** This kind of rebuilding is essentially free in ICM. In framework-based systems, it is a project.

The other reason ICM is the right foundation is that the architecture has to remain editable by the team for the long term. The audit produces a correct ontology at one moment in time, but the company will continue to evolve. The team needs to be able to update the architecture as the business changes, without calling me back every six months. Because everything is plain markdown, they can. The architecture grows with the company. It does not freeze the company at the moment of installation.

---

## The deeper principle

What ICM gets right at a deeper level is that **the best technology for a business is technology the business can operate without depending on its installer.** The whole point of the install is to leave the company with something they own and can run.

Most AI consulting fails this test. The system gets built, the consultant leaves, and within six months the system is either degraded (because nobody can maintain it) or dependent (because the consultant is still on retainer). Neither is a good outcome. The company spent significant money and ended up either with broken infrastructure or with a long-term cost center.

ICM passes this test by design. The architecture is portable, inspectable, editable, and built on tools every team already has — folders, text files, Git. There is no special skill required to operate it after installation. The training session at the handoff teaches the team how to extend the architecture themselves, and the playbook documents the structural reasoning so future team members can pick it up.

This is the standard I hold for every install. **If the team cannot operate the system without me afterward, the install was incomplete.** ICM is the only methodology I have encountered that lets me meet this standard reliably, because it builds on the simplest possible substrate.

If you want to read the full paper, it is linked from the main page of this site. The paper is short — twenty-one pages — and worth reading in full if you are seriously considering installing AI architecture in your business. Even if you do not work with me, understanding ICM will help you evaluate any other vendor you talk to. Most of what is being sold as "AI infrastructure" is more complicated than your business actually needs, and now you have a reference for what simpler looks like.

---

*Substrate · Practice of Jayden Forshee · 2026*
