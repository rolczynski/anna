# Ask — the world connections, read-only

Date: 2026-10-27. Status: to collect. A fresh-context agent reads and fetches, its findings are
appended below dated, then an execution brief follows, the logins and approvals stay with the
owner.

## The question

The owner's words, Oct 27: "first lets focus on interactions with the world ... we can give
access to email, linkedin, calendar and check if it works, set up skills and write section about
this." His answers the same day: Gmail and Google Calendar, one account; LinkedIn by the August
2026 design, a browser on the logged-in account reading some twenty curators' pages once a week,
human-paced; the order connect, test, then write. Spelled out: how does Anna read mail, calendar
and LinkedIn so that she cannot send, reply, draft, label, archive, delete or create anything,
what does it cost the owner once, in logins and approvals, what runs unattended and under which
permissions, and what is verified before user.md gets its section.

## The loss

The collector reads the world and cannot act on it. Prefer a read path that is read-only by
construction, Google's own read-only scopes or the calendar's secret address, over one that is
read-only by discipline. The owner's clicks are spent once. No secret, token, app password or
private URL enters any file in the repo.

## Where to read

- Claude Code docs, mcp.md, permissions.md and settings.md: MCP tools are named
  mcp__<server>__<tool>, allow and deny rules take them, a non-interactive run denies every tool
  not pre-approved, --settings passes a stricter settings file for one run, a project .mcp.json
  loads from the primary working directory and its first approval is interactive
- Community servers to evaluate: GongRzhe/Gmail-MCP-Server, taylorwilsdon/google_workspace_mcp,
  nspady/google-calendar-mcp, and any other widely used one
- Google: the scopes gmail.readonly and calendar.readonly; an OAuth app in Testing mode and the
  seven-day refresh token expiry; the calendar's secret address in iCal format as the no-OAuth
  read path
- private-notes/docs/private-notes.md, the entry "August 2026: LinkedIn weekly signal", the
  design for the LinkedIn read
- This machine on Oct 27: node v25.8.1 and npx present, no uv; no MCP servers configured except
  Playwright at local scope for the private-notes project

## Findings
