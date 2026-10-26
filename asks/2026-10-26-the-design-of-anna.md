# Decision — the design of Anna

Date: 2026-10-26. Status: to supervise, bullets for the owner to cut; on his word the paragraph
goes into docs/anna.md in private-notes and this file is the record behind it.

## The question

The owner's words, Oct 26: "I want to create the separate repository for the agent and
private-notes will become my knowledge base." Then: the model works in one conversation, it does
not run agents with fresh context, split a task, collect, research; there is no place to collect
asks and answers, write conclusions, ask follow-ups, do a daily briefing, control what has been
done; he spends his time computing the gradient and rarely steps. Spelled out: how should the
assistant be built, where should it live, what should it read and do unattended, how often, and
how does a decision get made and saved so that his time goes to supervision and steps.

## The loss

Optimise the owner's attention, spent on decisions and steps rather than on collection, with his
options kept open. Constraints: the knowledge base stays readable without any agent; nothing acts
on his behalf; nothing he would not want in a private repo enters one; the Amazon agent stays
project-scoped and untouched.

## Assumptions

- A working record, asks, reports, briefings, is not notes and would swamp the knowledge base
  within a month [the agent's reading of the amazon repo, where the record is the bulk]
- Skills and agents load only from the folder a session starts in, so an agent with its own
  skills needs its own folder [Claude Code, seen in the amazon split]
- The gradient delegates and the loss does not; the owner holds the weights, the baby, the risk,
  the worth of a year in the US against a year remote [agreed Oct 26]
- Computation should scale with irreversibility and closing windows, not with interest; most of
  the days spent so far went to reversible decisions [the agent's reading, agreed]
- An unattended agent that reasons about the owner's life produces plausible stories no one
  audits; the collector must record and never reason [the advisor contract's first warning,
  agreed]
- Twice-daily collection is enough, the state lives in files, and a live agent only asks to be
  answered [the agent's reading, agreed]
- LinkedIn automation risks the account, and the account is the job search's one channel; the
  weekly curator design is the safe form [the owner's journal, August 2026]
- WhatsApp has no API for a personal account, the only road is the web client against the terms,
  and it reads other people's messages [the agent's reading, to verify]
- Read-only MCP servers exist for the owner's mail and calendar provider [the agent's belief, to
  verify before anything is built on it]
- Preferences belong in the contract, per-thread memory in threads/, and a separate memory folder
  would drift from them [the owner, Oct 26]
- The thread file in private-notes stays minimal, one paragraph per decision, one bracket to the
  decision file here [the owner, Oct 26]

## Options and their consequences

- The agent folded into private-notes' dotfolder, one repo. A clean tree and one commit per close,
  but the collection lands in the knowledge repo and swamps it once the collector runs. Right for
  a thin agent, wrong for this one
- A separate repo for the assistant, private-notes the knowledge base. Two repos and a save that
  crosses them, the paragraph into the thread and the record here, against a knowledge base that
  stays plain and an agent that can grow. Chosen
- One agent across all repos, amazon, machine-learning, private-notes. Coherent, but it folds back
  the amazon agent, which is project-scoped by design and ends Dec 31, and makes every save cross
  three repos. Rejected
- Channels. Mail and calendar in, read-only. The three repos' git logs in. A watch list of named
  sources and named questions in. LinkedIn in, weekly, by the August design. WhatsApp out of the
  first version, corporate mail out
- Cadence. All day, rejected, nothing a live agent does that two collections do not, and it asks
  to be answered. Morning and evening, chosen. The planning session every third day, an hour
- The name. Julia, rejected for the language of that name. Anna, chosen, and it sorts beside
  amazon

## The direction

Build Anna as one agent in two modes in its own repo, rolczynski/anna, private, on the amazon
pattern: asks/ with asks.md for the collection and the decision files, threads/ for the agent's
record per thread, CLAUDE.md as the map and the state, the contract in .claude/agents/anna.md
holding how the work is done, no memory folder. The collector runs morning and evening under a
read-only settings file, records and never sends, and raises its own questions when a saved
assumption fails or a pending item expires. The planner is the session every third day, where
each question comes with its gradient, the loss stated first, and the owner decides. A decision
is saved twice, in full here and as one paragraph in the thread in private-notes, in his voice.
The first version in a week: the repo and this file today, the move of private-notes/agent into
the repo, the collector and its scheduler, mail and calendar once their servers are verified, the
git logs, the watch list, LinkedIn weekly, the first planning session about Oct 30.

## What would flip it

If two weeks of collection yield nothing a planning session acts on, the collector drops to
weekly. If LinkedIn draws a warning, its collection stops that day. If the mail and calendar
servers do not exist with read-only scopes for the owner's provider, those channels wait for a
manual export rather than a wider scope. If the two-repo save proves heavier than the clean tree
is worth, the agent folds back into the dotfolder, which is a move of files and nothing else.

## Review

Nov 2, one week: did the first version land. Nov 16, after two planning cycles: is the owner's
time going to steps.

## Where to read

- the private-notes session of Oct 26, the transcript on this Mac under
  ~/.claude/projects/-Users-rafalrol-Projects-private-notes/, for a detail, never copied
- ~/Projects/amazon, the template, CLAUDE.md, the contract, asks.md, desk/run.sh for the
  headless reader
- private-notes/agent/advisor.md, the previous advisor's contract, to be folded in
- private-notes/docs/private-notes.md, the August 2026 entry "LinkedIn weekly signal"
