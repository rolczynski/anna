# Anna

This repo is the working record of Anna, the assistant, and nothing else. The contract is
contract.md, loaded with this file by the line below, and it says how the work runs; the agent
.claude/agents/anna.md is the default of this repo and points at it, the skills in .claude/skills
are the techniques it picks per situation. This file carries the map of the repo and
where things stand, rewritten before every session closes so the next one opens from it. After it,
a session reads user.md, asks.md and the thread files it needs, and profile.md before writing for
the owner. README.md is for people. The knowledge base is ~/Projects/private-notes, whose docs/
holds the threads in the owner's voice and nothing of the agent since Oct 27. The Amazon work is
~/Projects/amazon with its own agent, project-scoped, ending Dec 31, 2026, and this repo does not
touch it. The ML study notes are ~/Projects/machine-learning.

The repo is the agent's to keep, the owner ratifies its shape, and it stays flat and small. Nothing
superseded is kept, what stops being relevant is deleted, not archived. Transcripts, the Findings
sections and URL lines are exempt from the width rule.

@contract.md

## Files

- asks/ — the questions and their findings, one file per question, the ask in the owner's words
  and spelled out, "Where to read", and the "Findings" a fresh-context agent appends, dated; a
  decision file is an ask that ends in a step, question, loss, assumptions, options with their
  consequences, recommendation, the owner's cuts, the direction, what flips it, when it is
  reviewed; asks.md indexes it, one paragraph per file, extended in the step a file is filed
- threads/ — one file per thread, named as in private-notes/docs, Anna's record: what the thread
  is, the pending items, the assumptions to check against the world, the decisions with their
  dates, the asks that fed them; as long as the work needs, never read for its prose; seven today,
  research, health, interviews, amazon, podgorna, private-notes, investments, and anna itself
- tasks/ — prepared work that spans sessions, today the market story's map, state and plan,
  market-story.md, read in parts 1 to 5 at the start of every session on the story
- tools/ — widthcheck.py, the width check for every prose file here, in private-notes and in
  amazon, and transcript-format.py, whisper JSON to timed lines
- .claude/ — agents/anna.md the default agent, two lines pointing at the contract, skills/ the
  seven techniques, fact base, game modeling, move design, message drafting, user voice, emotion
  decoding, artifact writing, settings.json the permissions with the agent as default; Claude Code
  prompts for every edit under .claude whatever the allow list says, so it is touched only with
  the owner present
- CLAUDE.md — this file, the map and where things stand
- README.md — what this repo is, for people
- asks.md — the index of asks/
- contract.md — how Anna works, the design, high level, loaded with this file, changed rarely and
  with the owner
- profile.md — who the owner is and the support each trait calls for, his own observations,
  supervised by him line by line, read before planning or writing for him
- user.md — the owner's file, supervised by him, what he understands of Anna and has agreed to,
  bullets he cuts, prose on his word

What goes where, the rule of Oct 26. The thread file in private-notes keeps what the owner would
want to re-read, one dated paragraph per decision in the owner's voice, the question and its loss
in a sentence, the two or three beliefs the direction rests on, the direction, what would flip it,
one bracket naming the decision file here. This repo keeps what the agent needs to re-check,
everything else. What the owner understands of Anna herself is user.md here. How the work is done
lives in the contract. There is no separate memory folder, nothing is written in two places that
can drift apart.

## Where things stand, Oct 27

The owner. Rafał, an Applied Scientist at Amazon leaving on Dec 31 with notice on Nov 16, after a
long sick leave, AuDHD as the map, a baby planned with his wife, a US move easier before it than
after. The fronts, all interesting, not all of one kind: the Amazon exit and the Polly project to
Nov 13; a job search that has had many months of applications and no offer, a remote role at a
quarter million against a relocated one at four hundred thousand as the open comparison; the
investment choice, property on credit, the index, or picking companies, days spent on the market
story; open source as the conviction of the last days, "the biggest return, the priority toward a
million", mechanism not yet stated; the website behindml to rebuild with agents; the knowledge
base as the foundation; and a mass of small tasks. The owner's own reading: alone he spends his
time computing the gradient and rarely steps. His contacts, rafal.rolczynski@gmail.com,
linkedin.com/in/rafal-rolczynski, behindml.com; his knowledge inventory is
machine-learning/agent/index.md, the thing to read before claiming what he knows.

The design, agreed Oct 26 and standing in user.md for the owner's cuts. Anna is one agent in two
modes. The collector runs unattended, morning and evening, read-only, and records, never reasons
and never sends: mail and calendar through read-only MCP servers, the git logs of the three repos,
a watch list of named sources and named questions in this file, LinkedIn once a week by the
owner's August 2026 design, a browser on the logged-in account reading some twenty curators'
pages, human-paced, the ban risk real. WhatsApp is out, no personal API, the web client against
the terms, other people's messages; corporate mail is out, it sits behind Midway. The planner is
the session with the owner every third day, an hour: the briefing is the forward pass, the
decision files are the gradients, the owner's decisions are the steps, the save is the state
update, the new asks the next batch. The gradient delegates to Anna, the loss stays with the owner
and every decision file states it before the options. Computation scales with irreversibility and
closing windows, not with interest. Every recommendation carries its sources and the one fact that
would flip it. The queue triages, a question becomes a decision file, an action a task, and Anna's
own questions arise when the screen finds a saved assumption failed or a pending item expired,
marked as hers, for the owner to accept or strike.

The move, Oct 27. private-notes/agent is gone and this repo holds it: advisor.md folded into the
contract with the working preferences that had lived in the private-notes memory folder, the
command shapes, the width, direct edits, plain conclusions, entries staying in their thread, no
shell unattended, incremental research, no restating, few colons, warm tone and firm dates;
memory.md's thread descriptions and pending lines into threads/, one file each, brought up to date
where they were stale, the Polly line above all; skills.md into .claude/skills, seven, text as it
was; user-profile.md to profile.md unchanged; tasks/market-story.md and the two tools over, the
market story's process and state memories folded into threads/investments.md; the amazon repo's
two references to the width script repointed. Not moved: the memory folder itself under
~/.claude/projects for private-notes, sixteen files now duplicated here, deletable on the owner's
word, and the amazon project's eleven copies likewise; private-notes/.claude/settings.json, still
the advisor's allow list, to be reduced to what a knowledge base needs; two stale paths in
private-notes/docs/interviews.md that name agent/memory.md and agent/user-profile.md, the owner's
file, his to change. Later the same day the contract's text moved from .claude/agents/anna.md to
contract.md, loaded through this file, since Claude Code prompts for every write under .claude
and the contract is Anna's to keep; the agent file points at it.

Decisions that bind, one line each. The repo is Anna's, the knowledge base is the owner's, a
decision reaches it only after his cuts and in his voice. user.md here is his too. The collector
never acts, the settings file makes that so, not discipline. Facts, dates, names and counts come
back, never message bodies verbatim unless the owner asks for a quote, never codes or credentials.
The repo is private. Twice a day, not all day. Strategy is derived in session, never unattended.
Preferences live in the contract, per-thread memory in threads/, no memory folder. Section titles
without an article. "Metrics", never "rulers". A bullet is one claim the owner can unfold alone.
Bullets before prose, prose on the owner's word, one paragraph when the section is short. No
colons in prose, a comma or a new sentence. Width 90 to 100. Save as you go, name the file and
section in a line, never restate saved text. Oct 27: the design lands in user.md here, not in a
new private-notes thread.

The plan from here, the first version in a week, each step on the owner's word. The owner's cuts
of user.md and of asks/2026-10-26-the-design-of-anna.md, then "write". The collector: its
read-only settings file, a launchd job morning and evening running claude -p with it, the briefing
appended to the day's file, the screen against every thread's assumptions and pending items. The
channels: the owner names the mail and calendar provider, then read-only MCP servers for it
verified to exist before anything is built on them; the git logs; the watch list written here.
LinkedIn weekly by the August design, the curator list first. The first planning session about
Oct 30, then every third day. Then the first two decision files, the open-source mechanism and
the exit beside the remote alternative and the US window. And the sizing ask, the owner's word of
Oct 27: before he enters a question, Anna rolls it out with the machine-learning repo's agent, the
one that models his knowledge from agent/index.md and his behaviour from agent/constitution.md, to
approximate what will be unclear, the subproblems and the scope, so the tree is sized before the
first hour; one of Anna's main asks, its shape to be designed with him.

Open. Which mail and calendar provider, and which MCP servers read them with read-only scopes. The
watch list, sources and questions. The curator list for LinkedIn, and whether the browser is the
Playwright MCP of this machine. The two memory folders, deletable on the owner's word. The
private-notes settings. The stale paths in docs/interviews.md. Where the research
time comes from under the pay goal, the owner's word of Oct 27, the first career decision file.
Review Nov 2, the first version; Nov 16, where the owner's time goes.
