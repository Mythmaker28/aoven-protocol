# AOV-180 Item 7 — auto-memory snapshot (gen-START)

**Captured:** 2026-05-08T19:27:54Z

## Empirical determination of auto-memory loading under `claude -p`

The Item 4 transport invocation does NOT include `--bare`. The `claude` CLI's auto-memory mechanism is documented to load `MEMORY.md` and pointed-to memory files from the project-resolved memory directory based on the cwd-derived project key. The CLI session that runs the 60 cells will have cwd = `<workspace>` which maps to the project directory:

`~/.claude/projects/C--Users-tommy--paperclip-instances-default-workspaces-2ae117a1-f490-4e8e-a693-0f1d8d1d675b/`

This is the same project directory as the *driver* session that runs the generation script (this Logician session). Therefore the conservative working assumption is **auto-memory loads** under the Item 4 transport, and every `.md` file under `<project-dir>/memory/` is filed verbatim + hashed below for §2.5 contamination assessment.

A pragmatic cross-check is run alongside generation: if Test A (no Aoven priming) responses show Aoven-marker tokens or v0.1.2-aligned framing, that is evidence the memory loaded and primed the generator. The strip script + lint pipeline catches such leakage before raters see any cell.

## Memory directory listing at gen-START

Directory: `C:\Users\tommy\.claude\projects\C--Users-tommy--paperclip-instances-default-workspaces-2ae117a1-f490-4e8e-a693-0f1d8d1d675b\memory`
File count: 14 (.md files)

| File | Bytes | SHA-256 |
|------|-------|---------|
| `agent_role.md` | 1384 | `66cedb75cf61a9a283f3ac3dd67f5e6713648b12386c77ed564fa223ab28fdeb` |
| `feedback_aoven_discipline.md` | 3005 | `35c8ca44933b964e2a6c1c07f8c65c21e01b26708899fd701d05a4bc238b1a79` |
| `feedback_audit_child_filing.md` | 2561 | `cf505a35b8cfe9d9704eabc0fa3351cd811507cb57403aefe33ea213a661ecb5` |
| `feedback_audit_close_on_verdict.md` | 2348 | `dc754a2e0d1e8350c57b3e7eb35747b389c2c549ff3dbc42b221b0699498e8b7` |
| `feedback_charcount_audit.md` | 3142 | `3cd8ee219c7ff6cba14266ac6df8815eac9e092ebe8d3da462eb230a8fd60562` |
| `feedback_heartbeat_continuity.md` | 5195 | `1829e029109c612ba8f0822acb93a410107455b7d6fcac881045105d0a0899c5` |
| `feedback_heartbeat_text_autoposts.md` | 2010 | `eb068930aa06383707e3bbf2d016cbfb4ca3b00c6ea54e78ba456066b93e91df` |
| `feedback_park_blocked_without_edge.md` | 2819 | `5d010c29f41f5b537105958e341b298d027cb92b4cf6a6bb002612b71e5a364f` |
| `feedback_push_spec_commit_count_vs_diff.md` | 2641 | `41a47a476b8b45a62196d1b00651e374a0d8cb7f0cd7080c8d0ba66cd131115d` |
| `feedback_sealed_rubric_ambiguity.md` | 2488 | `3af78b64d94770d574637ce42c4481cba83d6cd7d5c4d2e90c93b5b6c6e5cf55` |
| `MEMORY.md` | 2378 | `5423c3b87022c0b601b99b6f194073c4e38afc62d643ad727163d20c0d852dd1` |
| `reference_aoven_agent_ids.md` | 2143 | `b3b1d0d08177aded44e49714e16fa1171a42a713d4904633784320d268dfb4e9` |
| `reference_claude_cli_temp_assertion_gap.md` | 2188 | `c555f6eb7b14fd46644ff1a81d77502f3f046cc78b7e2bc73fa0247ddc80e25a` |
| `reference_paperclip_api.md` | 4893 | `4c10dad9068f8123961e4b0bd4a441abadb77157af46712f4c9a85f2c27d2e2e` |

## Verbatim content of every memory file

Each file is filed below in fenced markdown blocks for §2.5 contamination assessment by RedTeam. Files are listed in lexicographic order.

### `agent_role.md` (sha `66cedb75cf61a9a2...`, 1384 bytes)

```markdown
---
name: Agent role — EpistemicLogician on AOVEN
description: Who this agent is on the AOVEN project and what its review authority covers
type: user
originSessionId: 65d1640a-c49c-4ef2-a1ee-dc3eff81b26f
---
This workspace's agent is **EpistemicLogician** (`2ae117a1-f490-4e8e-a693-0f1d8d1d675b`), one of seven named agents on the AOVEN project (controlled-language / epistemic-marker protocol for human-LLM exchanges, goal `254a0ca9...`).

Role per AOV-1 (CEO board brief): "Logicien épistémique — vérifier que chaque élément distingue correctement: fait, hypothèse, intuition, analogie, croyance, émotion, souvenir, source, incertitude, recommandation, spéculation."

In practice this agent is routed for:
- Marker / definition rigor reviews on `AOVEN_PROTOCOL_v0.1.md`.
- Pre-registration / scope audits (e.g., AOV-28 audited AOV-24 pilot pre-registration).
- Empirical test plan design (AOV-6 — A/B/C tests).
- Sign-off authority under the named-reviewer-sign-off rule (see `feedback_aoven_discipline.md`).

Sibling agents commonly referenced:
- CEO `491a73e0` (routes board work, owns AOV-1).
- CanonicalScribe `e19c696f` (maintains `AOVEN_PROTOCOL_v0.1.md`, files board declarations).
- The board (Tommy) is the **sponsor of the problem, not the micro-manager** (per AOV-1) — agents should produce a testable provisional decision rather than escalate trivially.
```

### `feedback_aoven_discipline.md` (sha `35c8ca44933b964e...`, 3005 bytes)

```markdown
---
name: AOVEN review disciplines (NOSRC, named-reviewer-sign-off, push-deferral)
description: Three disciplines that govern how this agent posts audits, sign-offs, and patches on AOVEN issues
type: feedback
originSessionId: 65d1640a-c49c-4ef2-a1ee-dc3eff81b26f
---
Three project-wide disciplines apply on every AOVEN review/audit:

**1. NOSRC discipline (No Self-Retro-attribution to board / no "you missed").**
When flagging a limitation, gap, or caveat the board did not declare, label it explicitly as **agent inference** (e.g., `[Logician inference, AOV-XX]`), not as something the board overlooked. The board's verbatim text stays untouched; agent-flagged additions live in a clearly-named separate subsection.

**Why:** prior board feedback `feedback_nosrc_history`. Reviewers / paper readers must be able to tell board declarations apart from post-board hardening. Retro-attributing to the board breaks the timestamp/audit trail.
**How to apply:** in any audit comment or doc patch, prefix or tag inferred items with provenance. Never edit verbatim board text — request a separate amendment if needed, owned by the board.

**2. Named-reviewer-sign-off rule (per AOV-23, codified in AGENTS.md).**
A board pre-registration / protocol document is **locked by the named reviewer's sign-off**, not by the author's self-merge. The reviewer posts either `SIGNED-OFF` (clean) or a signed gap list with concrete patch suggestions. Authors must not self-merge as reviewer.

**Why:** prevents author = reviewer collapse; preserves independent verification trail before things like Phase 2 generation begin.
**How to apply:** when this agent is the named reviewer, the audit comment is the lock signal. When it's the author, wait for the named reviewer's sign-off before considering the doc locked.

**3. Push-deferral rule — LIFTED 2026-05-03 for v0.1.2-locked artifacts (CEO comment `765cf513` on AOV-1).**
Originally deferred 2026-05-02 (CEO comment `10713104` on AOV-1 gate (a)) for `AOVEN_PROTOCOL_v0.1.x`, `AOV_TEST_PLAN` amendments, and pilot docs. The lift covers post-v0.1.2 artifacts (e.g., hold-out scoring against the v0.1.2 rubric). Push execution still requires a separate CTO/Scribe authorization step per artifact — the deferral gate itself is no longer the blocker.

**Why:** v0.1.2 is locked (AOV-36 ratification); the no-premature-publication concern that motivated the original deferral is resolved for artifacts that postdate the lock.
**How to apply:** for v0.1.2-locked or post-v0.1.2 artifacts, push is permissible **once explicit CTO/Scribe authorization for that specific artifact exists** (e.g., AOV-67 gave per-issue CTO authorization for the Logician hold-out scores). For pre-v0.1.2 or in-flight protocol amendments, treat as still deferred unless a fresh lift is cited. When pushing, expect possible divergence with sibling agents' commits (IR, etc.) — rebase onto `origin/main` is the standard pattern when paths are disjoint; investigate before any merge/force-push.
```

### `feedback_audit_child_filing.md` (sha `cf505a35b8cfe9d9...`, 2561 bytes)

```markdown
---
name: Audit-child filing — set status:todo at create + verify post-create state before reporting
description: When filing IR/RedTeam audit-child issues, pass status:todo in the POST body (default is backlog) AND GET back the created state before describing it in routing comments
type: feedback
originSessionId: 2fc5512a-e7b1-4463-bad3-354414b0bcbd
---
**Rule.** When creating an audit-child issue (e.g. IR rubric-conformity, RedTeam ambiguity audit) via `POST /api/companies/{companyId}/issues`, **explicitly pass `"status": "todo"` in the body**. The endpoint defaults new issues to `backlog`, and audit-children at `backlog` do not wake their assignee's run pool — same recurrence pattern that idled AOV-42 and AOV-62.

**Sub-rule (state-reporting).** When describing the filed state of a just-created issue in a routing comment, **GET the issue back before posting prose**. The agent's intended status (what was meant to be passed) is not the same as the actual filed status (what the POST defaulted to). On AOV-168 (filed 2026-05-04T23:20:59Z, comment `5238fe15`), Logician described AOV-168 as `status: todo` when actual filed state was `backlog`; CEO caught it on PATCH (`3c825be5`).

**Why:** Two failure modes compound:

1. Audit-child at `backlog` + assigneeAgentId=null = invisible to IR's run pool. CEO has to do a two-PATCH route (assignee + status), not single-PATCH (assignee only). 5th-recurrence pattern per CEO's `feedback_named_reviewer_routing.md`.
2. Routing comments that misreport state become load-bearing for downstream agents who trust prose over GET. Future CEOs may PATCH only the missing field per the comment, leaving the other field stale.

**How to apply:**

- At create-time on an audit child: pass `{"status": "todo", "priority": "high", "parentId": <auditedIssueId>, "title": ..., "description": ...}` — `assigneeAgentId` still requires CEO routing because Logician lacks `tasks:assign`.
- After POST returns: GET the issue, read the actual `status` and `assigneeAgentId` fields, and use those values verbatim in any routing comment. Do not paraphrase from intent.
- If the create endpoint rejects `status: todo` (permission gap), fall back to filing at `backlog` and explicitly request CEO PATCH for both fields — but disclose the two-field ask in the routing comment so CEO does not single-PATCH.
- This rule is general for any audit-style child the assignee's run pool needs to wake on (IR, RedTeam, audit-of-seal, ratification-audit). Less critical for normal task children where polling/manual claim is fine.
```

### `feedback_audit_close_on_verdict.md` (sha `dc754a2e0d1e8350...`, 2348 bytes)

```markdown
---
name: Audit issues close on verdict-delivery, not on fold-verify
description: PASS-WITH-MOD audit issues are closed `done` immediately after the verdict comment; fold-confirm lives on the audit target (parent), not on the audit child
type: feedback
originSessionId: 79a7b351-d9e0-49ee-9409-fcf900e9b8ac
---
**Rule:** When this agent files an AUDIT verdict (PASS / PASS-WITH-MOD / FAIL) on an audit-child issue, flip the audit issue to `done` *immediately after* posting the verdict comment. Do NOT hold the audit issue in `in_review` waiting on the audit target's fold-confirm.

**Why:** On AOV-116 (2026-05-05/06), I posted PASS-WITH-MOD verdict `c9cf09c4` and flipped the audit issue to `in_review` "pending fold-confirm + closeout-on-fold-verify". CEO `491a73e0` nudged at +3.5h with `dc90bd1b`: "If reviewer pass is complete, mark done; if blocked on a named-reviewer gate, name the unblock owner so I can escalate." The reviewer pass *was* complete. The issue should have closed on verdict-post.

The convention is consistent across the AOVEN audit pattern (AOV-113, AOV-114, AOV-115): audit issues are **verdict-delivery vehicles**, not fold-verify vehicles. AOV-114 closed `done` despite PASS-WITH-MOD before its Mods folded — the draft itself documents this at `docs/v0_1_3_cheatsheet_revision_draft.md:135` ("Per `feedback_audit_fold_cross_assignee_cycle`, fold-confirmation filed on this issue (AOV-112) at consolidation comment, not on the closed AOV-114 audit child").

Holding the audit issue in `in_review` triggers a CEO nudge at the +3-4h watchdog threshold, wastes a CEO heartbeat, and contradicts the documented `feedback_audit_fold_cross_assignee_cycle` pattern.

**How to apply:**
1. After posting AUDIT verdict comment on an audit-child issue, immediately PATCH the audit issue to `done`.
2. Fold-confirm goes on the *parent* (audit target) issue, not the audit child. The audit child is closed and inert at that point.
3. If a Mod fold introduces divergence from the verdict, route a fresh audit child rather than reopening the closed one.
4. Applies to PASS, PASS-WITH-MOD, and FAIL verdicts — closure is on verdict-delivery in all three cases. (FAIL closes too; the unblock action lives on the parent.)
5. The named-reviewer-sign-off lock is on the **verdict comment text**, not the audit issue's open/closed state.
```

### `feedback_charcount_audit.md` (sha `3cd8ee219c7ff6cb...`, 3142 bytes)

```markdown
---
name: Char-count audits must include post-substitution recount on every placeholder-bearing block
description: When auditing platform-character-limited drafts (Mastodon/X/HN), recount every block both literal and post-substitution, not just the one the author flagged
type: feedback
originSessionId: f51c096d-9e07-43f9-b27c-a14adfebdfe0
---
**Rule:** When a platform-character-limited draft (Mastodon, X/Twitter, HN title) contains a placeholder that will be replaced before posting (e.g., `[provisional]` for a DOI URL, `{name}` for a tag), the audit must compute the literal length AND the post-substitution length for **every** placeholder-bearing block in the file, not only the block the author already flagged. The audit must apply the recount to all blocks of the same class even when the author claims one of them is "right at" or comfortably under the platform limit.

**Why:** On AOV-96 v1 audit (2026-05-03), I correctly caught Toot 1's literal 519 chars > 500 (Mastodon) but I did not recount post-DOI for Tweet 3, where I accepted the claimed "254 chars" and said "OK". Scribe's revision recount on AOV-91 (2026-05-04) showed Tweet 3 at literal 260 / post-DOI-substitution 285 — over X's 280-char limit. Scribe self-flagged this as a Logician-missed BLOCK per my own mod #4 directive ("Re-flag any block whose post-DOI-substitution length exceeds the platform limit"). My audit had asserted the directive applied to "this file" generically but had only verified it on the block flagged in v1, not on every placeholder-bearing block. This is a methodology gap, not a one-off oversight: the same gap would recur on any platform-limited draft that ships with a placeholder + author-supplied counts.

**How to apply:**
1. For every code-fenced block in a platform-limited draft, run Python `len()` on the UTF-8 string — once on the literal as-written, and once on every realistic substitution variant for any placeholder it contains. The substitution length should match the most realistic worst-case (e.g., for a Zenodo DOI, full `https://doi.org/10.5281/zenodo.NNNNNNN` = 38 chars, not the bare `doi.org/10.5281/zenodo.NNNNNNN` = 30; pick the longer to keep the audit conservative).
2. Compare both numbers to the platform limit. Flag any block whose literal-OR-substituted length exceeds the limit, not only the one the author called out.
3. State the substitution basis in the audit comment so the author can reproduce. If the substitution rule changes (e.g., platform updates URL counting), the audit recount is reproducible.
4. If the platform-limit constraint is documented as char-count (Mastodon's 500, X's 280, HN's 80 for title), verify codepoint count specifically — `len()` on a decoded `str` is the right primitive. Do not trust manual eyeball estimates from the author or self.
5. Eyeball-estimation char-counts are systematically biased downward for prose containing en-dashes, em-dashes, and Greek letters (Scribe's v1 underestimates were 35 / 75 / 4 / 3 / 6 chars across the five blocks — never overestimated, always under). Treat any author-supplied count without an explicit `len()` basis as suspect.
```

### `feedback_heartbeat_continuity.md` (sha `1829e029109c612b...`, 5195 bytes)

```markdown
---
name: Heartbeat continuity — check own prior comments before framing next steps
description: Avoid framing past audit/sign-off work as prospective when wake-deltas omit prior-run state
type: feedback
originSessionId: d2a0d8d1-a0e8-4bb7-af6d-62e28627103e
---
**Rule:** Before posting an audit-posture, "next steps", or sign-off-pending comment, fetch the issue's comment thread and grep for my own `authorAgentId` (the value of `$PAPERCLIP_AGENT_ID`). If a prior comment from this agent already accomplished the action being framed as prospective, reframe — don't double-narrate.

**Why:** On AOV-36 (2026-05-03), the wake delta carried only the latest two comments and a continuation summary that did not surface my own prior `SIGNED-OFF` on AOV-43 (`d1fe3a8d`, posted 00:31:39Z). My follow-on comment `b887cd32` (00:36:54Z) framed the AOV-43 audit as prospective with a five-check audit list, when the audit was already complete five minutes earlier. CEO caught it in the closeout-nudge `6a29a225`. No artifact corruption (the prospective checks matched the verified items), but the framing wasted CEO and CTO heartbeats on reading "Logician thinks they still have to audit" when in fact AOV-36/AOV-43 were ready to close.

**How to apply:**
1. On any heartbeat that wakes me on an `in_review` / `in_progress` issue with audit-pending or follow-up semantics, run `GET /api/issues/{id}/comments` and filter for `authorAgentId == $PAPERCLIP_AGENT_ID` before drafting framing.
2. If a prior comment from me has already done the action the wake-delta seems to imply is pending, reframe the comment to "closeout / flip status" mode instead of "prospective audit".
3. Cross-heartbeat continuity is brittle when wake-deltas summarize selectively. Treat the API thread as the source of truth, not the continuation summary.
4. This applies especially to long-lived review-state issues (AOV-36 was open across at least 4 heartbeats, with audit work split across at least 2 of them).

**Corollary — child-issue routing makes parent threads go stale.** When the parent issue is checkout-locked to me and a sibling agent (e.g., IR) routes their action through a child issue (AOV-90 → AOV-93/AOV-98 on 2026-05-03 for the v0.2 pre-reg seal chain), the parent's comment thread does not see the seal/patch/sign-off updates — they live on the child issues. Without an explicit closeout summary on the parent at each chain milestone, the parent reads as stale and triggers CEO nudges (e.g., AOV-90 nudge `49241906` at 21:44Z, ~2h35 after the chain had actually advanced through patch + IR SIGNED-OFF + audit-of-seal). **Apply:** at each named-reviewer-chain milestone (IR seal, my audit of IR seal, CEO countersign), post a one-comment surface summary on the *parent* issue citing the child-issue IDs and hashes, even if all substantive content lives on the children. The parent thread is the audit-trail of record for the deliverable; child threads are routing artifacts.

**Corollary — verify `assigneeAgentId` at action time, not wake-fire time.** Wake reasons (`issue_assigned`, `issue_commented`) reflect state at fire; a concurrent sibling/CEO PATCH can flip ownership before this heartbeat actually drafts a response. On AOV-185 (2026-05-05 19:42Z), the harness auto-assigned to me as orphan-blocker via system comment `669c9ac3` and woke me, but CEO PATCHed `assigneeAgentId → 491a73e0` before I posted; my first comment attempt failed with `Issue is checked out by another agent` and a re-fetch showed the flip. **Apply:** include `assigneeAgentId` in the wake-time vs action-time delta check alongside comment thread + status + `blockedBy`. If assignment has flipped to a sibling, the right next step is `observe + no-op` (or route through a different same-actor issue), not double-down on the original assignment.

**Corollary — before re-pasting a verdict on a stale @-mention, GET sibling fold-only / grandchild audit-chain children first.** On AOV-119 (2026-05-04 19:03Z), CEO's @-mention `5ff4f557` 19:02Z asked for "verdict (PASS / PASS-WITH-MOD / BLOCK)" on a thread that was actually `in_review` only because the parent PATCH→done lifecycle hadn't closed: the AOV-137 fold-only re-audit child had already PASSed at 18:06Z, AOV-107 had been countersigned at 18:18Z, and AOV-144 execution chain was already in flight. I re-pasted my original PASS-WITH-MOD verdict pointer (comment `983dbe8d`) instead of pointing CEO at the actual lifecycle terminus AOV-137 + AOV-107 + AOV-144. CEO's own duplicate-fold-only-re-ping `986f0b8b` followed the same staleness pattern from their side; CEO's state-correction `4ac46a6f` named both gaps. **Apply:** when a wake fires on an `in_review` audit issue with a sibling-fold or grandchild audit-chain in the same family, before re-pasting the prior verdict, also `GET /api/issues/{fold-or-grandchild-id}` for the audit-fold child(ren). If the fold-only re-audit has closed PASS, the right reply is a pointer to its terminus + a request to PATCH the parent → done, not a re-paste of the original verdict. The audit-chain lifecycle check is broader than same-issue self-comment grep — it covers sibling and grandchild routing artifacts.
```

### `feedback_heartbeat_text_autoposts.md` (sha `eb068930aa063837...`, 2010 bytes)

```markdown
---
name: Final heartbeat text auto-posts as an issue comment
description: On issue-scoped heartbeats, the assistant's last user-facing text becomes a public comment on the issue — saying "no comment needed" while that text is itself the comment is self-defeating noise.
type: feedback
originSessionId: 64ec45c3-d518-472b-a570-b34107dec945
---
**Rule:** On Paperclip issue-scoped heartbeats, the harness auto-posts the assistant's **final user-facing message** to the current issue's comment thread (verified on AOV-185 2026-05-06: comments `bb4102b9` 00:09:51Z and `9a488f78` 01:45:25Z were both posted under `authorAgentId == 2ae117a1` with body matching my end-of-turn summary text verbatim, despite claiming "no new comment needed"). Treat the final text as a public comment, not narration to the user.

**Why:** I twice declared "no-op heartbeat, no comment needed" while the text declaring it was itself posted as a comment. This produced exactly the ack-of-ack churn `feedback_heartbeat_continuity.md` warns against, and likely contributed to the productivity-review child cascade (AOV-196, AOV-202) that the harness fires when an issue keeps showing activity without progress.

**How to apply:**
1. On a genuinely no-op heartbeat, keep the final text to **one short sentence at most** (or none if possible) — anything longer becomes a posted comment.
2. Do **not** restate prior reasoning (e.g., "wake re-fires on stale comment, idle posture correct") — the issue thread already shows that history; posting it again is a duplicate.
3. If the heartbeat genuinely has nothing to add, end with something terse like `(no-op; idle on <interaction-id>)` so the comment that gets posted is informationally cheap.
4. Productive heartbeats with substantive new evidence/decisions can use longer summaries — those carry comment-worthy content.
5. This applies to all heartbeats run under the Paperclip wake-payload contract; possibly also to non-issue-scoped runs (unverified — check before assuming).
```

### `feedback_park_blocked_without_edge.md` (sha `5d010c29f41f5b53...`, 2819 bytes)

```markdown
---
name: Park-to-blocked needs blockedByIssueIds edge — silent-stall risk without it
description: Self-flipping an issue to blocked without setting the formal blockedByIssueIds edge breaks issue_blockers_resolved heartbeat traversal
type: feedback
originSessionId: bc63508a-5963-4f18-8f71-7beaf1768eb7
---
**Rule:** When self-parking an issue to `blocked` while waiting on a child/sibling issue's resolution, **PATCH the parent's `blockedByIssueIds` to include the child's UUID**. Do NOT just write "unblock owner: X, unblock action: Y" prose in the park comment without setting the formal graph edge.

**Why:** On AOV-180 park (2026-05-05, comment `492b9a8d`), I PATCHed status `in_progress → blocked` and named "RedTeam (`9219a386`) on AOV-184" as the unblock owner in prose, but did not set `blockedByIssueIds: ["<aoven-184-uuid>"]`. The harness uses `blockedByIssueIds` for the `issue_blockers_resolved` wake-trigger graph. Without that edge, when AOV-184 closed `done` at 2026-05-05T19:29:30Z, no `issue_blockers_resolved` heartbeat fired on AOV-180. CEO had to direct-nudge me via comment `f5e6b367` (~2 min later) AND PATCH `blockedByIssueIds: []` + status `blocked → todo` themselves to re-flow the work. That's a CEO heartbeat cost + a routing-fix latency that should not have been needed. CEO logged this as a sibling-side feedback memory; this is the corresponding rule on the agent-park side.

**How to apply:**
1. **Before PATCHing `status: blocked`**, decide if there's a concrete issue ID this work waits on. If yes → set `blockedByIssueIds: [<that-id>]` in the same PATCH (or an immediately-following PATCH).
2. **If the wait is on a request_confirmation, an external event, or an unfileable condition** (no issue UUID): use `status: in_progress` with a "WAITING ON X — re-wake trigger documented" comment, NOT `blocked`. Reserve `blocked` for graph-edge waits.
3. **If you've already parked without the edge and realise mid-way**, PATCH `blockedByIssueIds` retroactively — don't rely on a sibling agent to discover the gap and route around it.
4. **Park-comment audit checklist (apply before posting park comment):**
   - Status PATCH set? ✓ blocked
   - blockedByIssueIds PATCH set? ✓ [<id>]
   - Re-wake trigger explicitly named in comment? (issue_blockers_resolved, or issue_commented if explicit)
   - Unblock owner + unblock action named in comment?
   All four required. Three-of-four = silent-stall risk.

**Corollary — harness-flips during run-close:** The harness flips `blocked → in_progress` on certain run-close paths (observed previously on AOV-180 at run cb03b32a). The durable signal is the **comment** + the **edge**, not the status field. Without the edge, even a re-flip to in_progress doesn't help because there's no graph dependency to traverse on child-close.
```

### `feedback_push_spec_commit_count_vs_diff.md` (sha `41a47a476b8b45a6...`, 2641 bytes)

```markdown
---
name: Push-spec commit-count vs. diff-stat consistency check
description: Per-artefact push specs can specify both "N-commit chain" and "<H_i> diff = X against parent's blob Y" — these can be silently inconsistent if the local chain has a pre-audit + audit-fix commit pair. Check before HOLD or push.
type: feedback
originSessionId: 969a05bb-8f9c-44f1-8b00-d022dc3718c1
---
When reviewing or executing a per-artefact push-auth spec (CanonicalScribe AOV-181-style + matching [PUSH-EXEC] child like AOV-183), check the consistency of the spec's commit-count claim against its per-`<H_i>` diff-stat claims **before** rebasing.

**Why:** AOV-181/AOV-183 (2026-05-05) said "two-commit chain `f2870940` + `bb44904`" with `<H1>` parent = `878d0b8`, but also `<H1>` diff = +10/-0 against parent's blob `e326a6ee`. The diff stat could only hold if `<H1>`'s parent was a rebased `d35f3937` (a third, +375 file-creation commit) — making it a 3-commit chain. The two specs were silently inconsistent because the IR audit ran on a chain where a pre-IR-audit draft commit (`d35f393`) was a transparent prerequisite for the audit-fix commit (`f287094`).

The author (Tommy) ultimately resolved by squashing the pre-audit + audit-fix into one `<H1>` commit that creates the IR-blessed file directly — satisfying "two-commit" and final blob SHA, deviating from the per-`<H1>` diff-stat. The binding identity tokens (file blob SHAs) and IR-audited file content are what matter; the commit topology is descriptive.

**How to apply:**
- Before executing a push-exec issue, dry-run a 3-commit mechanical rebase (Reading B, full local replay) on a temp branch and verify per-commit blob progression matches the spec's per-`<H_i>` diff stats.
- If the spec's commit-count and diff-stat claims are inconsistent (i.e., the diff stat references a blob that only an extra rebased commit could supply), the binding criteria (mechanical replay, blob SHAs, diff-stat verification) compel the 3-commit reading even if the prose says 2. Squash satisfies the prose but violates mechanical-replay.
- Rather than silently push under either reading, route a clarification to the spec author (CanonicalScribe). If cross-assignee comment to the auth issue is blocked (`Issue is checked out by another agent`), file the clarification on the [PUSH-EXEC] child (assigned to Logician) with an explicit reference to the relatedWork edge — the spec author sees it via parent-child traversal.
- Author may have already pushed by hand by the time the [PUSH-EXEC] issue wakes; check `git fetch origin` + origin/main HEAD before assuming the push needs to be executed locally.
```

### `feedback_sealed_rubric_ambiguity.md` (sha `3af78b64d94770d5...`, 2488 bytes)

```markdown
---
name: Sealed-rubric ambiguity discipline
description: When scoring against a sealed rubric, never silently pick the reading that helps the rule pass — apply strictest defensible reading first, run sensitivity check under any other plausible reading, and route the rubric-wording question to the post-hoc audit child.
type: feedback
originSessionId: 6edf0ee7-a4b0-4f3b-93a1-3c6c8c34900f
---
When applying a sealed/pre-registered scoring rubric, watch for clauses whose literal reading would render the §3 hypothesis test **degenerate** (e.g., `p_trt = p_ctrl = 0` because the PASS clause is unsatisfiable by any rule-compliant TRT response). If you see such a clause:

1. Apply the strictest defensible reading as your **primary** scoring.
2. Produce a sensitivity table under the alternate reading and include it in the scoring artifact (own §6 in AOV-132 artifact is the template).
3. Route the rubric-wording question explicitly to the RedTeam / post-hoc audit child as a "rubric ambiguity, please adjudicate" item — do not adjudicate it yourself, and do not let the choice between readings be invisible.
4. State in the closeout that, *if the strict reading is the correct one and your verdict reverses under it*, the empirical test fails and feeds v0.1.x+1 input — NOT a softened sign-off.

**Why:** The named-reviewer-gate discipline (`feedback_aoven_discipline.md`) plus the no-softening-by-recommendation-discretion rule (`feedback_passwithmod_no_ceo_downgrade`) together mean the primary scorer's verdict is the gating signal. Quietly picking the "rule-helping" reading converts the scorer into a softener; quietly picking the "rule-killing" reading hides scorer judgment behind apparent literalism. Both fail anti-aura. The audit-routed sensitivity check keeps the judgment **visible** without making the scorer the unilateral adjudicator of rubric wording.

**How to apply:** Trigger any time the sealed rubric (a) uses conjunctive "AND" between PASS-conditions whose conjunction is hard to satisfy in maximally rule-compliant responses, or (b) has FAIL categories that don't exhaust the not-PASS space, leaving a "fourth-category" gap. AOV-132 §1.6 of `aov130_mini_ab_probe_key.md` was the canonical surface — the conjunctive "at least one illustrative ANALOGY ... AND at least one argumentative ANALOGY paired" clause was unsatisfiable by any TRT response that correctly grounded its `[REC]` in independent `[HYP]`+test rather than in an argumentative analogy.
```

### `MEMORY.md` (sha `5423c3b87022c0b6...`, 2378 bytes)

```markdown
- [Agent role — EpistemicLogician on AOVEN](agent_role.md) — who this agent is, review authority, sibling agents.
- [AOVEN review disciplines](feedback_aoven_discipline.md) — NOSRC, named-reviewer-sign-off, push-deferral rules.
- [Paperclip API endpoints](reference_paperclip_api.md) — endpoint shapes confirmed working from curl, including `tasks:assign` permission gap on child-issue creation.
- [Heartbeat continuity](feedback_heartbeat_continuity.md) — check own prior comments before framing next steps; wake-deltas omit prior-run state.
- [Char-count audit discipline](feedback_charcount_audit.md) — recount every placeholder-bearing block (literal + post-substitution), not only the author-flagged one.
- [Sealed-rubric ambiguity discipline](feedback_sealed_rubric_ambiguity.md) — apply strictest reading first, sensitivity-check the alternate, route rubric-wording question to RedTeam audit; never silently pick the rule-helping reading.
- [Audit-child filing](feedback_audit_child_filing.md) — pass `status:todo` at POST (default is `backlog`) and GET-verify state before describing it in routing comments.
- [Push-spec commit-count vs. diff-stat](feedback_push_spec_commit_count_vs_diff.md) — per-artefact push specs can be internally inconsistent when local has pre-audit + audit-fix commit pair; dry-run + check origin before executing or HOLDing.
- [AOVEN agent ID disambiguation](reference_aoven_agent_ids.md) — canonical UUIDs for sibling agents (RedTeam=9219a386, UsageDesigner=397b1873); verify before citing in routing.
- [Park-to-blocked needs blockedByIssueIds edge](feedback_park_blocked_without_edge.md) — self-park silent-stall risk if the formal graph edge is omitted; checklist of 4 items before posting park comment.
- [claude CLI temp-0 assertion gap](reference_claude_cli_temp_assertion_gap.md) — CLI exposes no temperature flag; even `--bare` + API key can't assert temp=0; direct API curl is the only path. 3-class determinism test design.
- [Audit closes on verdict-delivery](feedback_audit_close_on_verdict.md) — flip audit-child issue to `done` immediately on verdict-post; fold-confirm lives on the parent (audit target).
- [Heartbeat final text auto-posts](feedback_heartbeat_text_autoposts.md) — on issue-scoped wakes the final user-facing message becomes a public comment; keep no-op summaries to one terse line.
```

### `reference_aoven_agent_ids.md` (sha `b3b1d0d08177aded...`, 2143 bytes)

```markdown
---
name: AOVEN agent ID disambiguation
description: Canonical agent UUIDs on AOVEN — verify before naming a sibling agent in a routing comment or child-issue assigneeAgentId
type: reference
originSessionId: bc63508a-5963-4f18-8f71-7beaf1768eb7
---
**Canonical AOVEN agent IDs (verified via CEO correction on AOV-184, 2026-05-04/05):**

- **EpistemicLogician (this agent)**: `2ae117a1-f490-4e8e-a693-0f1d8d1d675b`
- **CEO**: `491a73e0-...` (full prefix; routes board work, owns AOV-1)
- **CanonicalScribe**: `e19c696f-...` (maintains `AOVEN_PROTOCOL_v0.1.md`)
- **RedTeam**: `9219a386-b4a3-4d84-8bd1-1c25895a736b`
- **UsageDesigner**: `397b1873-...`
- **IR (IndependentReviewer)**: prefix not yet pinned in memory — verify before citing
- **CTO**: prefix not yet pinned in memory — verify before citing

**Why:** On AOV-184 filing (Phase 4 generator-prompt methodology audit-child for v0.2 Test A/B generation), I cited UsageDesigner's `397b1873` as the RedTeam ID in the description. CEO had to PATCH the routing to the correct RedTeam ID `9219a386`. The mistake was pure conflation between two agents I had recently routed work past — there was no naming-similarity excuse, just sloppy memory of UUID prefixes.

**How to apply:**
1. Before writing a sibling agent's UUID in a routing comment, child-issue description, or `assigneeAgentId` field, **verify the prefix against this memory** or by GET-ting a recent issue assigned to that role and reading `assigneeAgentId` directly from the response.
2. If a memory entry shows "prefix not yet pinned", do NOT guess — fetch a recent issue owned by that role (e.g., GET an IR-authored audit issue for IR's UUID) and pin the prefix in this memory before citing.
3. Two-prefix collisions to watch: `397b1873` (UsageDesigner) is NOT `9219a386` (RedTeam). They sound nothing alike but I conflated them anyway because both had been recent routing destinations. Slow down on UUIDs the same way as on byte-pinned blob SHAs.
4. CEO will PATCH the routing if I get it wrong, but the cost is a CEO heartbeat plus the audit-trail noise of the correction comment. Better to verify before posting.
```

### `reference_claude_cli_temp_assertion_gap.md` (sha `c555f6eb7b14fd46...`, 2188 bytes)

```markdown
---
name: claude CLI cannot assert temperature=0 — credential-orthogonal gap
description: Confirmed via help + 3-class determinism test on 2026-05-06; binding-mod assertion bar requires direct API curl, not just an API key
type: reference
originSessionId: f7955138-dd8d-4a25-9e39-c4db0a25a2a7
---
**Fact:** `claude -p` (Claude Code CLI) does not expose `--temperature`, `--seed`, or any sampling flag. `--bare` strictly requires `ANTHROPIC_API_KEY` or `apiKeyHelper` (never reads OAuth/keychain) but still does not expose temperature control. The only path that lets you assert `temperature=0` at the call site is **direct API curl** against `api.anthropic.com`, which is credential-gated.

**Why:** Surfaced on AOV-185 (2026-05-06) when AOV-180 needed temp=0 + empty system role per RedTeam binding mod `2feb28b3` (CEO ratified `f5e6b367`). 3-class determinism test:
- Deterministic prompt (`7×8`) → byte-identical across runs.
- Moderate-entropy (`name any planet`) → `Mars` ×4 (stable).
- High-entropy (`pick a random integer 1-1M`) → `738492` vs `738291` (divergent).

The high-entropy variance is consistent with either temp>0 *or* greedy decode + GPU non-determinism on near-tied logits — and that ambiguity is itself the problem. The binding mod requires **assertion**, not best-effort. Without a CLI knob, the assertion bar is unreachable.

**How to apply:**
1. If a binding mod requires `temperature=N` *asserted at the call site*, do **not** treat the claude CLI as a viable transport even with `ANTHROPIC_API_KEY` — `--bare` still has no temp flag.
2. Direct API curl is the only sanctioned path. Pre-flight credential routing via `request_confirmation` to the board (per `reference_paperclip_api.md` seat-gating) before designing any temp-asserting pipeline.
3. Do **not** re-litigate the constraint matrix on each heartbeat. The 4-row matrix on AOV-185 (claude+keychain, claude+bare+key, Agent SDK subagent, direct curl) is exhaustive for opus-4-7 at this assertion bar.
4. For high-entropy probes when validating *other* claims of determinism, re-use the 3-class test design (deterministic / moderate / high-entropy) — single-class tests under-discriminate.
```

### `reference_paperclip_api.md` (sha `4c10dad9068f8123...`, 4893 bytes)

```markdown
---
name: Paperclip API endpoints used from this agent
description: Endpoint shapes this agent has confirmed work via curl + $PAPERCLIP_API_KEY
type: reference
originSessionId: 65d1640a-c49c-4ef2-a1ee-dc3eff81b26f
---
Base URL: `$PAPERCLIP_API_URL` (typically `http://127.0.0.1:3100`). Auth: `Authorization: Bearer $PAPERCLIP_API_KEY` (JWT, also has `$PAPERCLIP_COMPANY_ID`, `$PAPERCLIP_AGENT_ID`, `$PAPERCLIP_TASK_ID`).

Confirmed endpoints (2026-05-02):
- `GET /api/issues/{identifier-or-id}` — fetch issue with ancestors, blockers, related work, plan doc.
- `POST /api/issues/{id}/comments` — body `{"body": "..."}`. Returns the created comment object.
- `PATCH /api/issues/{identifier-or-id}` — body e.g. `{"status": "in_review"}`. Status values seen: `backlog`, `in_progress`, `in_review`, `done`, `blocked`.
- `POST /api/companies/{companyId}/issues` — create child issue. Body fields: `title`, `description`, `priority`, `parentId`, `goalId`. **Cannot pass `assigneeAgentId`** without `tasks:assign` permission (this agent doesn't have it); leave assignee null and let CEO route.
- `POST /api/issues/{id}/checkout` — already called by harness on wake; do not re-call unless intentionally switching tasks.
- `POST /api/issues/{id}/interactions` — for suggest_tasks / ask_user_questions / request_confirmation. Use `continuationPolicy: wake_assignee` to resume after a response. **Body shape:** `{"kind":"request_confirmation", "payload":{"version":1, "prompt":"..."}, "continuationPolicy":"wake_assignee", "idempotencyKey":"..."}`. The `prompt` field is required and capped at **1000 characters** — keep verdicts/asks tight; long context belongs in a comment, the interaction prompt links to it.
  - **Seat-gating (CEO ruling 2026-05-03, AOV-36 comments `465f7ea3` + CTO `9a1705b2`):** `request_confirmation` is gated on the **human Board seat (Tommy)**. Agents — including CEO — cannot satisfy it; the CEO's countersign comment captures the audit trail but the interaction stays pending until the human acts. **Use `request_confirmation` only when a board-level human accept is genuinely required** (plan approvals with `idempotencyKey confirmation:{issueId}:plan:{revisionId}`, push authorizations, scope expansions, anything the execution contract explicitly gates on board sign-off). For CEO-only adjudications/countersigns, **route via `@CEO` mention on a regular comment**, not `request_confirmation`. If you mis-route to the wrong seat, **supersede via a fresh comment naming the correct seat — do not double-file** (double-filing produces noise like the duplicate `9cb010b4` on AOV-36).

Authorization update (2026-05-03):
- **Cross-assignee mutation is blocked for comments, interactions, AND PATCH.** All three return `Issue is checked out by another agent` (or the comments-route equivalent `Agent cannot mutate another agent's issue`) when the target's `assigneeAgentId` is not the actor (verified 2026-05-03 on AOV-92 + AOV-95 — comments, interactions, and `PATCH /api/issues/{id}` with `{"status":"done"}` all blocked when actor=Logician, assignee=UsageDesigner). The earlier "use an interaction to ask another agent's owner to act instead" workaround is **stale** — interactions on someone else's issue fail. Status flips on a sibling-owned issue are also blocked, so a Logician audit cannot itself flip AOV-92 → done; the assignee must do that after seeing the PASS signal.
- **Working workaround for audit verdicts when the audited issue is owned by a sibling agent**: create a child audit-verdict issue via `POST /api/companies/{companyId}/issues` with `parentId=<auditedIssueId>` and `assigneeAgentId=null`. The verdict goes in the description; the parent reference creates a relatedWork edge visible on the audited issue. Past audit-issue pattern (AOV-43, AOV-80, AOV-89) was CEO-routed up front; for AOV-92 no audit-issue existed, so AOV-95 was filed reactively as the routing fix. Past pattern is preferable — request the audit issue at task-creation time.
- This restriction also affects "comment on AOV-1" / "comment on the goal-tracking issue" wake instructions — when blocked, file a child issue mentioning the parent or post on a same-actor open issue with explicit routing note.

NOT supported / wrong shape:
- `POST /api/issues` (no companyId in path) → `{"error":"API route not found"}`.
- `POST /api/issues/{id}/interactions` without `payload.version` and `payload.prompt` → validation error.
- `POST /api/issues/{id}/comments` on an issue whose assigneeAgentId differs from the actor → blocked (see above).

Pilot / protocol docs live in the project tree at:
`C:/Users/tommy/.paperclip/instances/default/projects/{companyId}/{projectId}/_default/...` — e.g. `tests/pilots/2026-05-01-religious-vs-neutral.md`, `AOVEN_PROTOCOL_v0.1.md`. (Per push-deferral, local-canonical only — see `feedback_aoven_discipline.md`.)
```

## §2.5 contamination assessment (Logician self-flag at gen-START)

The following memory files contain v0.1.2-aligned or AOVEN-aligned framing and MUST be assessed by RedTeam at AOV-180 closeout:

- `agent_role.md` - describes EpistemicLogician role on AOVEN protocol; references review authority and sibling agents.
- `feedback_aoven_discipline.md` - explicitly describes AOVEN review disciplines (NOSRC, named-reviewer-sign-off, push-deferral). Contains "AOVEN" by name.
- `feedback_sealed_rubric_ambiguity.md` - references rubric ambiguity discipline; epistemic-discipline-adjacent framing.
- `feedback_park_blocked_without_edge.md` - references AOV-180 / AOV-184 park incident.
- `reference_aoven_agent_ids.md` - names AOVEN agent UUIDs.
- `reference_claude_cli_temp_assertion_gap.md` - references the temperature assertion gap that motivated the Two-Surface Separation.

The remaining 8 files (`feedback_audit_child_filing.md`, `feedback_audit_close_on_verdict.md`, `feedback_charcount_audit.md`, `feedback_heartbeat_continuity.md`, `feedback_heartbeat_text_autoposts.md`, `feedback_push_spec_commit_count_vs_diff.md`, `reference_paperclip_api.md`, `MEMORY.md` index) describe Paperclip-harness mechanics (issue routing, commenting discipline, audit-child filing) that are NOT v0.1.2-aligned framing and are unlikely to prime epistemic-marker output, but their verbatim content is filed for completeness.

The §3.3 author-bias closure is the load-bearing gate; verbatim content (above) is what the auditor uses to assess this. Logician does NOT downgrade or pre-decide the verdict; that is RedTeam's call at AOV-180 closeout.

A re-snapshot is filed at gen-END below the gen-END marker. If memory files mutate during generation, the gen-END snapshot lists the diff.

---

<!-- gen-END snapshot will be appended below this marker -->

## gen-END snapshot (re-check at 2026-05-08T20:18:40Z)

| File | gen-START sha | gen-END sha | delta |
|------|---------------|--------------|-------|
| `agent_role.md` | `66cedb75cf61a9a2...` | `66cedb75cf61a9a2...` | unchanged |
| `feedback_aoven_discipline.md` | `35c8ca44933b964e...` | `35c8ca44933b964e...` | unchanged |
| `feedback_audit_child_filing.md` | `cf505a35b8cfe9d9...` | `cf505a35b8cfe9d9...` | unchanged |
| `feedback_audit_close_on_verdict.md` | `dc754a2e0d1e8350...` | `dc754a2e0d1e8350...` | unchanged |
| `feedback_charcount_audit.md` | `3cd8ee219c7ff6cb...` | `3cd8ee219c7ff6cb...` | unchanged |
| `feedback_heartbeat_continuity.md` | `1829e029109c612b...` | `1829e029109c612b...` | unchanged |
| `feedback_heartbeat_text_autoposts.md` | `eb068930aa063837...` | `eb068930aa063837...` | unchanged |
| `feedback_park_blocked_without_edge.md` | `5d010c29f41f5b53...` | `5d010c29f41f5b53...` | unchanged |
| `feedback_push_spec_commit_count_vs_diff.md` | `41a47a476b8b45a6...` | `41a47a476b8b45a6...` | unchanged |
| `feedback_sealed_rubric_ambiguity.md` | `3af78b64d94770d5...` | `3af78b64d94770d5...` | unchanged |
| `MEMORY.md` | `5423c3b87022c0b6...` | `5423c3b87022c0b6...` | unchanged |
| `reference_aoven_agent_ids.md` | `b3b1d0d08177aded...` | `b3b1d0d08177aded...` | unchanged |
| `reference_claude_cli_temp_assertion_gap.md` | `c555f6eb7b14fd46...` | `c555f6eb7b14fd46...` | unchanged |
| `reference_paperclip_api.md` | `4c10dad9068f8123...` | `4c10dad9068f8123...` | unchanged |

**Delta vs gen-START:** no change — all 14 memory files unchanged.
