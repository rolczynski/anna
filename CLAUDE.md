# Anna

This repo is the working record of Anna, the assistant, and nothing else. The agent is
.claude/agents/anna.md, the default of this repo, and it says how the work runs. This file carries
the map of the repo and where things stand, rewritten before every session closes so the next one
opens from it. After it, a session reads asks.md and the thread files it needs. README.md is for
people. The knowledge base is ~/Projects/private-notes, whose docs/ holds the threads in the
owner's voice, and whose agent/ folder is the previous advisor, to be folded into this repo. The
Amazon work is ~/Projects/amazon with its own agent, project-scoped, ending Dec 31, 2026, and this
repo does not touch it. The ML study notes are ~/Projects/machine-learning.

The repo is the agent's to keep, the owner ratifies its shape, and it stays flat and small. Nothing
superseded is kept, what stops being relevant is deleted, not archived. Transcripts, the Findings
sections and URL lines are exempt from the width rule.

## Files

- asks/ — the questions and their findings, one file per question, the ask in the owner's words
  and spelled out, "Where to read", and the "Findings" a fresh-context agent appends, dated; a
  decision file is an ask that ends in a step, question, loss, assumptions, options with their
  consequences, recommendation, the owner's cuts, the direction, what flips it, when it is
  reviewed; asks.md indexes it, one paragraph per file, extended in the step a file is filed
- threads/ — one file per thread, named as in private-notes/docs, Anna's record: the pending
  items, the assumptions to check against the world, the open questions, the decisions with their
  dates, the asks that fed them; as long as the work needs, never read for its prose
- .claude/ — agents/anna.md the contract, settings.json the permissions with the agent as default
- CLAUDE.md — this file, the map and where things stand
- README.md — what this repo is, for people
- asks.md — the index of asks/

What goes where, the rule of Oct 26. The thread file in private-notes keeps what the owner would
want to re-read, one dated paragraph per decision in the owner's voice, the question and its loss
in a sentence, the two or three beliefs the direction rests on, the direction, what would flip it,
one bracket naming the decision file here. This repo keeps what the agent needs to re-check,
everything else. How the work is done lives in the contract. There is no separate memory folder,
nothing is written in two places that can drift apart.

## Where things stand, Oct 26

The owner. Rafał, an Applied Scientist at Amazon leaving on Dec 31 with notice on Nov 16, after a
long sick leave, AuDHD as the map, a baby planned with his wife, a US move easier before it than
after. The fronts, all interesting, not all of one kind: the Amazon exit and the Polly project to
Nov 13; a job search that has had many months of applications and no offer, a remote role at a
quarter million against a relocated one at four hundred thousand as the open comparison; the
investment choice, property on credit, the index, or picking companies, days spent on the market
story; open source as the conviction of the last days, "the biggest return, the priority toward a
million", mechanism not yet stated; the website behindml to rebuild with agents; the knowledge
base as the foundation; and a mass of small tasks. The owner's own reading: alone he spends his
time computing the gradient and rarely steps.

The design, agreed Oct 26 in the private-notes session. Anna is one agent in two modes. The
collector runs unattended, morning and evening, read-only, and records, never reasons and never
sends: mail and calendar through read-only MCP servers, the git logs of the three repos, a watch
list of named sources and named questions in this file, LinkedIn once a week by the owner's
August 2026 design, a browser on the logged-in account reading some twenty curators' pages,
human-paced, the ban risk real. WhatsApp is out, no personal API, the web client against the
terms, other people's messages; corporate mail is out, it sits behind Midway. The planner is the
session with the owner every third day, an hour: the briefing is the forward pass, the decision
files are the gradients, the owner's decisions are the steps, the save is the state update, the
new asks the next batch. The gradient delegates to Anna, the loss stays with the owner and every
decision file states it before the options. Computation scales with irreversibility and closing
windows, not with interest. Every recommendation carries its sources and the one fact that would
flip it. The queue triages, a question becomes a decision file, an action a task, and Anna's own
questions arise when the screen finds a saved assumption failed or a pending item expired, marked
as hers, for the owner to accept or strike.

The threads, as private-notes/agent/memory.md maps them until the move: Research, the ML
expertise, sprints in the machine-learning repo; Health, the contact with himself, docs/health.md;
Interviews, the company list and the direct reach, Synthesia, ElevenLabs, Kyutai open; Amazon
exit, docs/amazon.md, the letter Nov 16, the exit papers in December; Podgórna, the rental,
minutes and a vote asked by Oct 30; Private notes, the journal. Their pending lines live in that
file until threads/ takes them over.

Decisions that bind, one line each. The repo is Anna's, the knowledge base is the owner's, a
decision reaches it only after his cuts and in his voice. The collector never acts, the settings
file makes that so, not discipline. Facts, dates, names and counts come back, never message
bodies verbatim unless the owner asks for a quote, never codes or credentials. The repo is
private. Twice a day, not all day. Strategy is derived in session, never unattended. Preferences
live in the contract, per-thread memory in threads/, no memory folder. Section titles without an
article. "Metrics", never "rulers". A bullet is one claim the owner can unfold alone. Bullets
before prose, prose on the owner's word, one paragraph when the section is short. No colons in
prose, a comma or a new sentence. Width 90 to 100. Save as you go, name the file and section in a
line, never restate saved text.

The plan from here, the first version in a week, each step on the owner's word. The design as the
first ask, asks/2026-10-26-the-design-of-anna.md, bullets for the owner to cut, then its
paragraph into a new thread docs/anna.md in private-notes. The move of private-notes/agent into
this repo: advisor.md folded into the contract, memory.md's map into this file and its pending
lines into threads/, skills.md into .claude/skills, tasks/ and tools/ brought over, user-profile.md
placed by the owner's choice, the private-notes settings reduced to what a knowledge base needs.
The collector: its read-only settings file, a launchd job morning and evening running claude -p
with it, the briefing appended to the day's file, the screen against every thread's assumptions
and pending items. The channels: a mail and a calendar MCP server with read-only scopes, verified
to exist for the owner's provider before anything else; the git logs; the watch list written
here. LinkedIn weekly by the August design, the curator list first. The first planning session
about Oct 30, then every third day.

Open. Which mail and calendar provider, and which MCP servers read them with read-only scopes.
Where user-profile.md goes. The watch list, which sources and which questions. The curator list
for LinkedIn. Whether the browser for LinkedIn is the Playwright MCP of this machine. The first
two asks after the design, the open-source mechanism and the exit decision beside the remote
alternative and the US window, both for re-derivation. The eleven memories copied into the amazon
project's memory folder, duplicates of its contract, deletable at the next housekeeping.
