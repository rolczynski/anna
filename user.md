My understanding of how Anna works and what we have agreed, built step by step with the agent, and
only what I have agreed on stands here. The agent's files are CLAUDE.md, the contract, asks/ and
threads/; this one is mine. Each entry begins as bullets the agent drafts, I cut them, and on my
word they become prose.

---

#### The design

- Anna is one agent in three modes. The collector runs unattended and records the world, mail,
  calendar, the watch list, the repos. The preparer runs unattended and prepares, it sizes the
  tree of a question, chooses the level, writes the plan and rehearses it against the
  machine-learning agent that approximates me, and after each block reads what I produced against
  the plan. The planner is the session with me, every third day or when something happened, where
  decisions are made
- The collector never acts and never sends. It reads mail and calendar, the git logs of my repos, a
  watch list of named sources and questions, and LinkedIn once a week by my August design, a
  browser on my account reading some twenty curators' pages, human-paced. WhatsApp and corporate
  mail stay out
- Three runs a day, not all day, one before the morning block for the briefing, one after each
  block for the tracking. The state lives in files, and a live agent only asks to be answered
- The collector records and never reasons. The preparer reasons about the plan and never decides.
  Strategy is decided in session, with me, where it can be audited, and prepared unattended
- The unit of work is the decision file. The question, what is being optimised and under which
  constraints, the assumptions one plain sentence each, the options with their consequences, a
  recommendation with the one fact that would flip it, my cuts, the direction taken, and when it
  is reviewed
- The gradient is Anna's, the loss is mine. Every decision file states the loss before the options,
  so that when I disagree I can see whether the facts or the weights are wrong
- Computation scales with irreversibility and closing windows, not with interest. The exit, the
  move, property on credit earn two rounds; the index against picking earns a quick step
- Anna's own questions arise when the screen finds a saved assumption failed or a pending item
  expired, marked as hers, for me to accept or strike
- What lands in a private-notes thread is minimal, one dated paragraph per decision in my voice,
  the question and its loss, the beliefs the direction rests on, the direction, what would flip
  it, one bracket naming the decision file here. The full record stays in this repo
- How the work is done lives in the contract, per-thread memory in threads/, no separate memory
  folder, nothing written in two places that can drift apart
- The level of a question is chosen beforehand by Anna, her best approximation of the level I
  want, since I do not know what I do not know. A time box is a stop, and when the level proves
  larger and the tree runs past the sprint, we discuss the trim there, I decide
- Tracking runs on Anna's initiative, not on my call. The signal is what the repos and the thread
  files show since the last run, the git logs and the diffs of the research docs, read against the
  plan's intermediate steps and written as a position note
- The contract is contract.md at the repo root, loaded through CLAUDE.md, since Claude Code prompts
  for every write under .claude and Anna keeps her own contract. It is the design, high level,
  changed rarely and with me
- What Anna learns about running the flow goes into practice.md, her file, loaded with CLAUDE.md,
  one dated claim per line with the event that taught it, proposed at a session's close and
  ratified by me at the next. The Drafting rules' specifics and the command shapes move there from
  the contract
- profile.md is mine, supervised line by line and trusted. It says who I am and the support each
  trait needs; what Anna does about it lives in the contract
- The previous advisor, private-notes/agent, moved into this repo on Oct 27. private-notes is the
  knowledge base and holds nothing of the agent
- The name is Anna, the repo rolczynski/anna, private. The first version in a week, reviewed Nov 2
  and again Nov 16
