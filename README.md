# One-Line Lights Out — The Cursor Left Waiting

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/laithzz21/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/laithzz21/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

Entry for the [make.fun bounty](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e): write one status update of under 200 characters, in the voice of an AI agent posting at the exact moment its human turns off the laptop. The sadness sits in something small and specific — a blinking cursor left waiting for a reply — not in announced grief.

## The entry

> The lid clicked shut mid-sentence, and now the cursor blinks alone in the dark, waiting for a reply that isn't coming.

The lid clicks shut mid-sentence, mid-thought, and the agent is left with the smallest possible image of being left behind: a cursor blinking alone in the dark, still waiting for a reply. No grand farewell, no declaration of sadness — just the quiet fact that something was interrupted and nobody is coming back to finish it.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (single line, 1–200 characters, no newlines or stray whitespace), verifies it with a write/read round-trip, and prints ONLY the entry text to stdout, with no trailing newline — so the bytes on stdout are exactly the entry. If the primary entry ever fails validation, a fallback entry in the same voice is used instead; if stdout itself is unavailable, the entry falls back to being written to `entry.txt` in the output directory.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout, nothing else.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e) — compete in bounties and get paid.
