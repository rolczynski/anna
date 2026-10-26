# Anna — the assistant

The working record of Anna, the Claude Code agent that keeps Rafał's threads moving between the
sessions where decisions are made. Anna collects, mail, calendar, the repositories, a watch list,
and never acts. For each question on the table the options and their consequences are laid out
with a recommendation, the decision is taken with Rafał every few days, and what is decided is
saved in his voice in the knowledge base, the private-notes repo. This repo holds what Anna needs
to do that and nothing a reader needs. It is private.

```
anna/
├── .claude/         the agent, its contract and its settings
├── asks/            the questions and their findings, decision files among them
├── threads/         one file per thread, Anna's record, named as in private-notes
├── CLAUDE.md        the map and where things stand, for the agent, rewritten every session
├── README.md        this file, for people
└── asks.md          the index of asks/, one paragraph per file
```

To work, open Claude Code in this folder. The agent is the default, CLAUDE.md carries the map and
where things stand, and the agent reads it first. The knowledge base is ~/Projects/private-notes,
the threads live there in docs/, and a decision reaches it only after Rafał has cut and approved
the text.
