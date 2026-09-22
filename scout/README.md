# Literature Scout

Literature Scout is a recurring discovery workflow for your Research OS. It uses `manifesto.md` to find papers, reports, research posts, blogs, and news that may matter to your research.

It produces candidates for **human review**. It does not automatically add them to `library/` or change `manifesto.md`.

## Quick navigation

- [How it works](#how-it-works)
- [Configure the search](#configure-the-search)
- [Run it manually](#run-it-manually)
- [Review candidates](#review-candidates)
- [Schedule it](#schedule-it)
- [Send reports by email](#send-reports-by-email)

---

## How it works

Each run:

1. reads `manifesto.md`, `library/_index.md`, `scout/scope.md`, and `scout/_seen.md`;
2. searches for work related to current questions, evidence gaps, uncertainties, and competing ideas using complementary retrieval methods;
3. removes items already indexed or previously reported;
4. ranks the strongest candidates;
5. saves a dated report under `scout/reports/`;
6. records each candidate in `scout/_seen.md`.

Each report explains what was searched, what each candidate says, why it may matter, what material was examined, and any limitations.

For scholarly discovery, the default strategy combines three channels when they are available:

- web search for broad and recent discovery, official sources, grey literature, terminology, and verification;
- OpenAlex for structured scholarly metadata, identifiers, citations, references, and related works;
- `paper-search-mcp`, or another available scholarly MCP, for multi-index retrieval and lawful open-access discovery.

The channels are complementary rather than interchangeable. A run continues when one is unavailable, but the report must identify the missing method and describe the resulting coverage as degraded. Literature Scout does not install or configure MCPs during a run.

---

## Configure the search

Edit [`scope.md`](scope.md) before the first run. Set:

- your research topics and search vocabulary;
- the retrieval methods to attempt and the fallback behavior when an MCP is unavailable;
- source types and specific websites;
- the lookback period and maximum number of findings;
- language and timezone;
- inclusion and exclusion rules;
- optional email delivery.

The default scope attempts web search, OpenAlex, and `paper-search-mcp` or another available scholarly MCP. It includes scholarly databases, primary repositories, official research organizations, research blogs, and broader web leads. Social posts are off by default. Adapt these choices to your field and available tools.

---

## Run it manually

Test the workflow once before scheduling it:

```text
Run Literature Scout once using scout/scope.md. Save the dated report,
but do not index candidates or change manifesto.md.
```

Check the new report under `scout/reports/`. If the results are too broad or narrow, revise `scope.md` and test again.

---

## Review candidates

For a useful candidate, ask:

```text
Index candidate 2 from the latest scout report and update my Research OS.
```

You can also ask ChatGPT Work to:

- mark a candidate as `watch` if you want to revisit it later;
- mark it as `dismissed` if it is not useful;
- leave it as `reported` while you decide.

The candidate's status is stored in `_seen.md`, which also prevents the same item from being recommended repeatedly.

---

## Schedule it

After a successful manual test, ask ChatGPT Work to create a scheduled task. For example:

```text
Create a local scheduled task that runs Literature Scout every Monday at 8:00 AM
Hong Kong time. Follow scout/scope.md, save the report, and do not index candidates
or change manifesto.md.
```

Change the day, time, and timezone to suit your project. A weekly run is a sensible starting point; fast-moving topics may benefit from daily scouting.

A local scheduled task needs the computer to be awake, the project available, and the ChatGPT app running. A web or cloud task can run independently of your computer, but it needs access to lasting project files through GitHub, project uploads, or connected services.

You can review and manage runs in **Scheduled**. See the official [ChatGPT scheduled tasks guide](https://learn.chatgpt.com/docs/automations).

---

## Send reports by email

Literature Scout can save the Markdown report and send a styled copy by email. Email is optional and disabled by default. Every email uses the persistent [`email-report-template.html`](../skills/scout-literature/assets/email-report-template.html), so its layout remains consistent across runs. Edit that file to change the email design.

### 1. Connect Gmail

In ChatGPT Work:

1. Open **Plugins**.
2. Find and install the **Gmail** plugin.
3. Connect your Gmail account when prompted and approve only the permissions you are comfortable granting.
4. Start a new ChatGPT Work task after installation so the connection is available.

Plugin availability can depend on your ChatGPT plan and workspace settings. See the official [Plugins guide](https://learn.chatgpt.com/docs/plugins).

### 2. Enable email in `scope.md`

Edit the **Email delivery** section:

```text
- Enabled: yes
- Authorized recipient: your-address@example.com
- Format: full-detail HTML rendered with `skills/scout-literature/assets/email-report-template.html`
```

Use an address you are authorized to email. Do not commit a personal address or any credentials to a public repository.

### 3. Test delivery manually

```text
Run Literature Scout once using scout/scope.md. Save the report and email a styled
copy to the authorized recipient. Do not index candidates or change manifesto.md.
```

Confirm that the message contains the complete report, readable headings, working source links, summaries, relevance explanations, and caveats.

### 4. Include email in the scheduled task

```text
Create a local scheduled task that runs Literature Scout every Monday at 8:00 AM
Hong Kong time. Follow scout/scope.md, save the report, and email a styled copy to
the authorized recipient. Do not index candidates or change manifesto.md.
```

The scheduled task must have access to the connected Gmail plugin. If sending fails, the Markdown report should still remain saved and the run should report the delivery failure.
