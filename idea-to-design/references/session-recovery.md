# Session Recovery

Use this reference to keep `idea-to-design` resilient across crashes, restarts, or new sessions.

Main rule:
- a new session must be able to continue from files, not from memory

---

## Recovery Source Order

When resuming work, use this order:

1. `state.json`
2. `resume_packet`
3. `handoff_notes`
4. `Design-Spec.md`
5. latest checkpoint snapshot
6. asset directory

Do not start by replaying full chat history unless files are clearly stale or inconsistent.

---

## What Must Always Be Recoverable

At any stop point, a new agent should be able to answer:

- what project this is
- what phase it is in
- what was last completed
- what page or flow is in focus
- what the next recommended step is
- what files must be read
- what must not be redone
- what quality bar must be preserved

If these are missing, the state is not recovery-safe.

---

## Required State Updates

Update `state.json` whenever any of these changes:

- current phase
- approved stage
- current focus
- core flow set
- core page set
- selected design direction
- accepted image asset
- next recommended step
- blocking question list

Do not postpone these updates until the very end of the session.

---

## Required Stop Packet

Before pausing, ending, or switching sessions, write:

### `resume_packet.summary`
Short summary of current state.

### `resume_packet.last_completed_step`
Last meaningful completed action.

### `resume_packet.next_recommended_step`
Single best next step.

### `resume_packet.next_prompt_for_agent`
A direct instruction another Codex session can execute immediately.

Recommended content:
- files to read first
- current phase
- current focus
- work that must not be redone
- single next step only

Recommended pattern:

```text
Read state.json, Design-Spec.md, and [other file if needed]. Continue from [phase] with focus on [page/flow/task]. Do not redo [accepted work]. Complete only [next step]. Then update state.json, handoff_notes, and checkpoint if a boundary is crossed.
```

### `handoff_notes.for_next_session`
Short human-readable continuation note.

### `handoff_notes.must_read_files`
Files that must be opened first.

### `handoff_notes.do_not_redo`
Work already accepted or locked.

---

## Checkpoint Strategy

Use checkpoints at meaningful boundaries, not every tiny edit.

Recommended checkpoint moments:
- scope approved
- structure approved
- design direction chosen
- first accepted wireframe set
- first accepted mid-fi set
- first accepted hi-fi set
- final design doc generated

Each checkpoint should record:
- checkpoint id
- phase
- short summary
- timestamp
- related assets
- path to copied `state.json`
- path to copied `Design-Spec.md` if available

---

## Checkpoint File Convention

Recommended directory:

```text
checkpoints/
  2026-05-05T1600-scope-state.json
  2026-05-05T1730-structure-state.json
  2026-05-05T1730-structure-spec.md
```

Recommended naming:
- timestamp first
- phase second
- artifact type last

This keeps newest recovery points easy to find.

---

## Recovery Procedure For New Session

When a new session takes over:

1. read `state.json`
2. inspect `resume_packet`
3. inspect `handoff_notes`
4. open listed must-read files
5. confirm current phase and focus
6. continue from `next_recommended_step`

If `next_prompt_for_agent` is present and valid:
7. follow it directly as the starting instruction

Only if state is stale or contradictory:
- compare latest checkpoint
- inspect latest asset refs
- repair `state.json`

---

## Anti-Patterns

Avoid:
- relying on remembered chat context
- storing only broad summaries with no next step
- leaving page fidelity outdated after image acceptance
- updating `Design-Spec.md` but not `state.json`
- updating `state.json` but not `handoff_notes`

These create false recovery confidence.

---

## Minimal Recovery Quality Bar

A recovery-safe project must let a fresh session continue within a few minutes by reading files only.

Recommended higher bar:
- a fresh session can continue by executing `next_prompt_for_agent` with little or no extra interpretation
