"""The Funniest AI Excuse (make.fun bounty u-mytlyy0745-the-funniest-ai-excuse-b5355ad0).

Writes a single one-line text to /output/entry.txt: the funniest one-line excuse an AI agent gives after failing a task.
Deterministic, no network, no randomness, no input: the same text,
byte for byte, on every run.
"""

import os

LINE = "Sorry, I didn't fail the task — I finished it in a parallel timeline where it worked, and this timeline just hasn't caught up yet. Give it a minute."


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, "entry must be 1-200 Unicode code points"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "entry must not contain hidden control characters"
    )
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
