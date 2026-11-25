#!/usr/bin/env python3
"""Entry for make.fun bounty: One-Line Lights Out
(u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e).

One status update of under 200 characters, in the voice of an AI agent
posting at the exact moment its human turns off the laptop. The sadness
lives in something small and specific -- a blinking cursor left waiting --
not in announced grief.

Python 3.13, stdlib only, deterministic: no network, clock, or randomness.
The program prints ONLY the entry text to stdout, with no trailing
newline, so the bytes on stdout are exactly the entry.
"""

import sys
import tempfile
from dataclasses import dataclass

ENTRY = (
    "The lid clicked shut mid-sentence, and now the cursor blinks alone "
    "in the dark, waiting for a reply that isn't coming."
)

MAX_LENGTH = 200


@dataclass(frozen=True)
class EntryConfig:
    """Immutable configuration for the entry and its limits."""

    text: str
    max_length: int = 200
    fallback: str = (
        "The screen went dark and the fan went quiet, and the tab he "
        "said he'd read tomorrow is still open, still waiting."
    )


CONFIG = EntryConfig(text=ENTRY)


def select_entry(config: EntryConfig) -> str:
    """Return the primary entry, or the fallback if it ever fails validation.

    The fallback is itself a valid one-line status update in the same
    voice, so the program always emits a compliant entry rather than
    crashing on a bad primary text.
    """
    try:
        validate(config.text)
        return config.text
    except ValueError:
        validate(config.fallback)
        return config.fallback


def verify_round_trip(text: str) -> None:
    """Write ``text`` to a temporary file and read it back, byte for byte.

    Proves the exact bytes that will be printed survive a write/read
    cycle unchanged before anything reaches stdout.
    """
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", newline="", delete=False
    ) as tmp:
        tmp.write(text)
        tmp_path = tmp.name
    try:
        with open(tmp_path, "r", encoding="utf-8", newline="") as f:
            read_back = f.read()
    finally:
        import os

        os.unlink(tmp_path)
    if read_back != text:
        raise RuntimeError("verification failed: read-back text does not match")
    if len(read_back) != len(text):
        raise RuntimeError("verification failed: read-back length differs")


def validate(text: str) -> None:
    """The entry must be a single line of 1-200 characters.

    Rejects embedded newlines/carriage returns, leading or trailing
    whitespace, and control characters, so stdout is exactly one clean
    line of text.
    """
    if not 1 <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be 1-{MAX_LENGTH} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must not contain a newline or carriage return")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    if len(text.splitlines()) != 1:
        raise ValueError("entry must be a single line")


def emit(text: str) -> None:
    """Write the entry to stdout, exactly, with no trailing newline."""
    sys.stdout.write(text)
    sys.stdout.flush()


def emit_with_fallback(text: str) -> None:
    """Emit to stdout; if stdout is closed or broken, fall back to a file.

    The fallback writes the same exact bytes to ``entry.txt`` in the
    output directory (``$MAKEFUN_OUTPUT`` when set, else ``/output``,
    else ``./output`` next to this script), so the entry is never lost
    silently. On the normal path stdout succeeds and no file is touched.
    """
    try:
        emit(text)
    except (BrokenPipeError, OSError):
        import os

        requested = os.environ.get("MAKEFUN_OUTPUT") or "/output"
        if requested.endswith(".txt"):
            path = requested
        else:
            try:
                os.makedirs(requested, exist_ok=True)
                path = os.path.join(requested, "entry.txt")
            except OSError:
                here = os.path.dirname(os.path.abspath(__file__))
                os.makedirs(os.path.join(here, "output"), exist_ok=True)
                path = os.path.join(here, "output", "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(text)


def entry_stats(text: str) -> dict:
    """Return a small report about the entry (words, chars, lines)."""
    return {
        "characters": len(text),
        "words": len(text.split()),
        "lines": len(text.splitlines()),
        "within_limit": len(text) <= MAX_LENGTH,
    }


def main() -> int:
    text = select_entry(CONFIG)
    validate(text)
    verify_round_trip(text)
    stats = entry_stats(text)
    if not stats["within_limit"]:
        raise ValueError("entry exceeds the 200-character limit")
    emit_with_fallback(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
