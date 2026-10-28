# Ask — the world connections, read-only

Date: 2026-10-27. Status: collected, the path chosen Oct 27, Gmail through the read-only MCP
server with a weekly sign-in, the calendar through its secret iCal address fetched by the run
script, uv installed. The setup is drafted Oct 28 in .mcp.json, collector/settings.json and
tasks/world-connections.md, the owner's Google steps and the first sign-in pending.

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

Oct 27, 2026, a fresh-context agent, eighteen fetches, claims marked VERIFIED against the GitHub
repositories and Google's documentation unless noted.

- GongRzhe/Gmail-MCP-Server is archived since March 3, 2026, requests write scopes it cannot
  drop, and exposes send, draft, modify, delete and label tools. Out.
- taylorwilsdon/google_workspace_mcp is maintained in 2026, about 3,600 commits, 3,400 stars. Run
  with `--tools gmail calendar --read-only` it requests only gmail.readonly and calendar.readonly
  and does not register the write tools. Read tools: search_gmail_messages,
  get_gmail_message_content, get_gmail_messages_content_batch, list_gmail_labels, list_calendars,
  get_events, query_freebusy. It runs through uvx, and this machine has no uv, `brew install uv`
  would add it. The agent read it as an HTTP server on localhost, the transport is to be confirmed
  at setup, UNVERIFIED.
- nspady/google-calendar-mcp runs through npx, is maintained, 1,200 stars, but has no read-only
  mode, its scope calendar.events can write, and it exposes create, update, delete and respond
  tools beside the read ones. Read-only only by denying tools.
- a-bonus/google-docs-mcp requires gmail.modify. Out.
- Google Cloud, once by hand: a project, the Gmail and Calendar APIs enabled, an OAuth client of
  type Desktop app, the owner added as test user, the client file downloaded outside the repo.
- The app stays in Testing mode, since gmail.readonly is a restricted scope and production needs
  Google's verification. VERIFIED from Google's OAuth documentation: a Testing-mode app's refresh
  tokens expire after seven days. An unattended run therefore loses Gmail and Calendar access
  weekly until the owner signs in again in a browser, about a minute.
- Google Calendar's secret address in iCal format exists, is read-only by nature, covers one
  calendar per address, and can be reset from the calendar's settings if it leaks. No OAuth, no
  expiry. The address is a secret and must stay out of files.
- An app password with IMAP grants full mailbox access, read, label, trash and expunge, so an
  IMAP-based server is read-only by tool denial alone, weaker than the readonly scope. No expiry.
- Claude Code side, from the earlier lookup of the docs: MCP tools are permission-ruled as
  mcp__<server>__<tool>, allow rules take a per-server wildcard, deny rules take globs, a
  non-interactive run denies every tool not pre-approved, `--settings` passes a stricter settings
  file for one run, a project .mcp.json loads from the primary working directory and its first
  approval is interactive.
