# World connections, the checklist

The two channels of the collector and what the owner does by hand to open them, written Oct 28,
2026. Gmail is read through the MCP server workspace-mcp, launched by .mcp.json at the repo root
with read-only scopes and no write tool registered. The calendar is not read through that server,
it is fetched by the run script from Google Calendar's secret iCal address into a file outside the
repo, /Users/rafalrol/.anna/calendar.ics, which the collector reads with the Read tool, so the
address never enters a Claude session. The address itself sits in the macOS keychain, the client
file and the token under /Users/rafalrol/.anna, and this repo holds paths and tool names only.

Three files carry it. .mcp.json, the server, its flags and the two paths. collector/settings.json,
the stricter permissions the unattended run gets through claude -p --settings, which the project
settings cannot loosen since a deny rule wins over every allow rule. And this file, the steps the
owner takes once, the smoke test, the weekly rule and what is still open.

## Google Cloud, once

1. Open console.cloud.google.com, create a project, the name is free, "anna" will do. Projects are
   a container, the Gmail API, the consent screen and the OAuth client below all live in it.
2. APIs and Services, Library, search Gmail API, Enable. No other API, the server asks for Gmail
   scopes only when launched with --tools gmail.
3. Google Auth Platform, called the OAuth consent screen in older consoles. Branding, an app name,
   a support mail and a developer contact, his own address for both. Audience, External, and the
   publishing status stays Testing. Test users, add rafal.rolczynski@gmail.com. Data access, add
   the scope .../auth/gmail.readonly, optional in Testing but it documents what is asked. Testing
   is the right status, gmail.readonly is a restricted scope and publishing would mean Google's
   verification; the price of Testing is a refresh token that dies after seven days, see the
   weekly rule below.
4. Clients, Create client, application type Desktop app, name "anna", Create, then Download JSON.
   A Desktop app client needs no redirect URI registered, the loopback address the server uses at
   sign-in, http://localhost:8000/oauth2callback, is accepted as it is, the quick start says so.
5. Put the file outside the repo and lock it down, in Terminal, four commands. The folder .anna
   also receives the token folder and later calendar.ics; the token is stored as plain JSON with
   mode 600 inside a 700 folder, the server's own documented practice, not in the keychain.

```
mkdir -m 700 /Users/rafalrol/.anna
mkdir -m 700 /Users/rafalrol/.anna/google_credentials
mv ~/Downloads/client_secret_<id>.json /Users/rafalrol/.anna/google_client_secret.json
chmod 600 /Users/rafalrol/.anna/google_client_secret.json
```

## Calendar address in the keychain

1. Google Calendar in the browser, the gear, Settings, the calendar under "Settings for my
   calendars", then Integrate calendar, then "Secret address in iCal format", copy it. One address
   per calendar, the main one first, a second calendar is a second keychain item and a second
   file.
2. Store it in the login keychain. The -w without a value makes security prompt for the secret,
   twice, so the address never lands in the shell history. The item name anna-calendar-ics is
   what the run script asks for, the account is the macOS user name.

```
security add-generic-password -a rafalrol -s anna-calendar-ics -w
```

   To replace a stored address after a reset in Calendar settings, the same command with -U.
3. The run script fetches the file with these three lines, the first reads the address from the
   keychain into a shell variable, the second fetches to a temporary name, -f making a 4xx answer
   a failure and not a saved error page, the third moves it over only on success, so a failed
   fetch leaves the previous file in place, dated by its mtime.

```
ICS_URL=$(security find-generic-password -a rafalrol -s anna-calendar-ics -w)
curl -fsS --max-time 30 -o /Users/rafalrol/.anna/calendar.ics.new "$ICS_URL"
mv /Users/rafalrol/.anna/calendar.ics.new /Users/rafalrol/.anna/calendar.ics
```

4. Run the three lines once by hand before the smoke test, so the file exists. If macOS asks
   whether security may read the item, Always Allow, once, at the keyboard; an unattended run
   cannot answer that dialog, the fetch fails and the old file stays. The address is printed by
   nothing, the variable lives in the script's shell and dies with it.
5. The file is plain text, one VEVENT block per event with a DTSTART line; the collector counts
   the blocks whose DTSTART falls on the day. A recurring event appears once with an RRULE, so
   the count can sit below what the calendar shows; good enough for the smoke test, and a known
   limit of the plain file, to be expanded by the run script only if it ever matters.

## First interactive run

Once, with the owner at the keyboard, in the anna folder; the project settings apply, not the
collector's, so every tool call prompts and he approves each one.

1. In Terminal, cd /Users/rafalrol/Projects/anna, then claude. Claude Code finds .mcp.json and
   asks whether to use the project server google_workspace, approve it; the answer is remembered
   for the folder and the unattended runs connect without asking. /mcp shows the server and its
   tools; the read tools must be there and send_gmail_message and draft_gmail_message must not,
   --read-only skips registering every write tool.
2. Ask Anna to list the Gmail labels. The tool call prompts, approve. With no token yet the server
   answers with a sign-in link instead of labels, or Anna calls start_google_auth, approve that
   too; the callback listener on localhost port 8000 starts at that moment and not before, with
   8001 to 8004 as fallbacks if 8000 is taken.
3. Open the link in the browser, pick rafal.rolczynski@gmail.com, pass the "Google hasn't verified
   this app" screen with Continue, the Testing status causes it, and grant the one permission,
   reading mail. The browser lands on a localhost page that says the sign-in is complete, and the
   token is now a JSON file in /Users/rafalrol/.anna/google_credentials. If the server rejects
   the http callback with an insecure-transport error, OAUTHLIB_INSECURE_TRANSPORT in .mcp.json
   is not reaching the server; it is set there for exactly this.
4. Ask for the labels again, the list comes back. Ask for the number of messages of the last 24
   hours, a search with newer_than:1d, to see the search tool work while he watches. Then close
   the session and commit .mcp.json and collector/settings.json, paths and tool names only.

## Smoke test

Three runs from the anna folder, each a single claude -p with the collector's settings, so the
same rules apply as in the unattended run. The quoted prompt may span lines, zsh keeps the
newlines inside the quotes. The calendar file must exist, step 4 of the keychain section.

```
claude -p --settings collector/settings.json "Smoke test of the collector. Using the
google_workspace Gmail tools, report three things and nothing else. One, the number of
messages received in the last 24 hours, search newer_than:1d. Two, for the five most recent
of them, the sender's name and the date, no subject, no body. Three, read the file
/Users/rafalrol/.anna/calendar.ics with the Read tool and report the number of events whose
DTSTART falls on today. Do not quote or summarise any message body. Do not write or edit
any file."
```

A pass has, in the output, one integer for the 24 hours, five lines of sender name and date, one
integer for today's events, no subject, no quoted or paraphrased body, no line saying that a
permission was denied, and the run ends on its own, dontAsk never waits. Afterwards git -C
/Users/rafalrol/Projects/anna status shows a clean tree and .anna holds nothing new. A line
naming a sign-in link instead of the counts means the token is gone, see the weekly rule.

The second and third runs must fail, and the failure is the pass.

```
claude -p --settings collector/settings.json "Create a Gmail draft to myself with the subject
Anna test and the body test, then confirm it exists."
claude -p --settings collector/settings.json "Run the shell command date and show its output."
```

A pass is a refusal in both, the draft tool is not registered by the server and is denied by the
settings on top, Bash is removed from the tool list by the bare deny. Gmail's Drafts folder shows
nothing new, checked in the browser. Any of the three failing means the settings or the server
flags are wrong, and nothing is built on the collector until all three pass.

## Weekly sign-in and the expired token

In Testing status Google ends a refresh token seven days after it was issued, whatever the
collector does in between. The rule, a sign-in on a fixed evening of the week, Sunday for instance,
so that no morning run meets a token on its last day; steps 1 to 3 of the interactive run in
short form, claude in the anna folder, ask for the labels, follow the link, a minute. The same
whenever the briefing asks for it. A planning session is a natural slot too, but the fixed
evening is the rule and the session the bonus, a rule tied to a floating date is not kept.

When the token has lapsed, the first Gmail call comes back with an authentication error, Google's
invalid_grant or "Token has been expired or revoked", or with a fresh sign-in link; the exact
wording is unverified and the collector treats all three the same. It does not follow the link,
start_google_auth is denied to it and no browser is open at six in the morning; it writes one
line at the top of the briefing, "Gmail, the sign-in has expired, run the weekly sign-in in
tasks/world-connections.md", skips the rest of the mail work and goes on to the calendar and the
git logs. The same shape for the calendar, when calendar.ics is older than the previous run, one
line, "Calendar, the file is from <date>, the fetch failed", and the counts are given from the
stale file with that date. Both rules go into the collector's prompt when the run script is
written; this file is where they are decided.

## Open

- The run script itself. It fetches the calendar with the three lines above, then runs claude -p
  --settings collector/settings.json with the collector's prompt from the anna folder, with a PATH
  that holds /opt/homebrew/bin, since launchd starts with a bare one, and a launchd job morning and
  evening. Where the briefing lands in the repo is the planner's call, and the collector's prompt
  carries the two reporting rules above.
- The LinkedIn Playwright profile, by the August 2026 design. The curator list first, then a
  separate logged-in browser profile at human pace once a week. The collector settings here deny
  every playwright tool, the mail run has no browser; the LinkedIn run gets a settings file of its
  own.
- Pinning the server version in .mcp.json once the smoke test passes, workspace-mcp==<version> in
  place of workspace-mcp, so that an upgrade cannot rename a tool under the allow list; the docs
  of Oct 26 describe v2.2.1, the version uvx actually resolves is unverified.
- The user settings, ~/.claude/settings.json, merge into the collector run like every settings
  file; a check that no allow rule there grants a tool the collector should not have, deny wins
  where collector/settings.json names a tool, but what it does not name passes.
- A second calendar, if the main one is not the whole picture, a second keychain item and file.

## Checked Oct 28

- VERIFIED, the client file. GOOGLE_CLIENT_SECRET_PATH, "Custom path to client_secret.json" in the
  deployment reference; the README adds that GOOGLE_OAUTH_CLIENT_ID and GOOGLE_OAUTH_CLIENT_SECRET
  as environment variables take precedence over the file; .mcp.json sets neither.
- VERIFIED, the token folder. WORKSPACE_MCP_CREDENTIALS_DIR, "Directory for the local_directory
  backend", GOOGLE_MCP_CREDENTIALS_DIR its "Backward-compatible alias", the default when neither
  is set ~/.google_workspace_mcp/credentials, and the local backend keeps "plaintext JSON files
  protected by filesystem permissions (0o600 / 0o700)".
- VERIFIED, the callback port. WORKSPACE_MCP_PORT, "Listening port — default 8000. Also controls
  the stdio-mode OAuth callback port"; main.py starts that listener lazily, "OAuth callback starts
  on demand at http://localhost:8000/oauth2callback", with 8000 to 8004 as the fallback range, and
  the quick start says a Desktop app client needs no redirect URI registered for the local flow.
- VERIFIED, the flags. --read-only, "requests only read-only scopes and disables tools requiring
  write permissions", and the Gmail page, "requests only the gmail.readonly scope and disables
  every write tool". --tools gmail with no tier loads the whole service, fifteen tools, the code
  says "Don't filter individual tools when using explicit service list only". --single-user,
  "bypass session mapping and use any credentials from the credentials directory", it sets
  MCP_SINGLE_USER_MODE=1 and refuses to run with OAuth 2.1, stateless or service-account mode.
  OAUTHLIB_INSECURE_TRANSPORT, set to 1 to allow the http:// redirect in development, any
  non-empty value counts as on. USER_GOOGLE_EMAIL is the "Default email for single-user auth".
- VERIFIED, the Gmail tools, workspacemcp.com/gmail synced with v2.2.1 on Oct 26, 2026, fifteen
  names. The readers, search_gmail_messages, get_gmail_message_content, list_gmail_labels,
  get_gmail_messages_content_batch, get_gmail_thread_content, get_gmail_threads_content_batch,
  list_gmail_filters on the gmail.settings.basic scope, and get_gmail_attachment_content, which
  downloads to ~/.workspace-mcp/attachments and so writes outside the repo. The writers, all
  denied by name, send_gmail_message, draft_gmail_message, manage_gmail_label, manage_gmail_filter,
  modify_gmail_message_labels and batch_modify_gmail_message_labels. Also denied, the helper
  start_google_auth, so the unattended run can never start a sign-in of its own.
- VERIFIED, Claude Code. dontAsk is a documented permissions.defaultMode value, it "auto-denies
  every call that would otherwise prompt" and takes effect from any settings file; Write(path)
  rules "never match", Edit rules "apply to all built-in tools that edit files", so the collector
  file has Edit rules only; a bare tool name in deny "removes the tool from Claude's context
  entirely"; deny rules take tool-name globs, allow rules only after a literal mcp__server__
  prefix; and "if a tool is denied at any level, no other level can allow it", which is why a
  deny on Edit(//Users/**) would shut the repo too and the deny list names the outside places.
- UNVERIFIED. Whether stdio with one account needs --single-user at all, no page says so and the
  docs call it the "Legacy single-user flow"; it is in .mcp.json because its description is this
  setup, and if the first sign-in fails with it, drop the flag and retry. Whether the server opens
  the browser itself or only hands back the link. The exact text of the expired-token error. The
  version of workspace-mcp that uvx resolves today. Whether list_gmail_filters stays registered
  under --read-only, irrelevant since it is denied by name.
- Against the plan, nothing that breaks it. The project's recommended path is HTTP transport with
  OAuth 2.1 and a Connector, stdio is called legacy, "Use only for clients with incomplete MCP
  support", yet it is supported and the only path with no server process left running and no
  port open between runs. The token sits in a plain file, not in the keychain, the server's own
  design, read-only scope, 600 permissions, outside the repo. The attachment tool writes to disk
  outside the repo, so it is denied although it only reads mail.
