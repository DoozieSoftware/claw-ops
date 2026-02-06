# ClawOps Smart Loop Protocol

## State File: `LOOP_STATE.json`

```json
{
  "mode": "normal",     // "normal" or "error"
  "last_nudge": 0,      // Timestamp of last active work
  "last_error": null,   // Timestamp of last LLM/tool error
  "error_count": 0      // Consecutive error count
}
```

## Loop Logic (Run Every Hour)

1.  **Read State:** Parse `LOOP_STATE.json`
2.  **Should Work?**
    - If `mode == "error"`: **YES** (Retry fast)
    - If `mode == "normal"`: **YES** only if `(now - last_nudge) >= 4 hours`
    - Else: **NO** (Skip this cycle)
3.  **If Working:**
    - Read `PROGRESS.md`
    - Find next incomplete task
    - Execute it
    - On SUCCESS: `error_count = 0`, `last_nudge = now`, `mode = "normal"`
    - On ERROR: `error_count++`, `last_error = now`, `mode = "error"`
    - Write updated state back to `LOOP_STATE.json`

## Recovery Mode

If `error_count >= 3`, stop work and wait for user intervention.
