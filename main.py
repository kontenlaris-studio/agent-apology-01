"""The AI Agent Apology One-Liner.

Writes a single apology line (<160 chars) to /output/entry.txt.
The line: an agent that replied to your email, then to its own reply,
then marked both urgent — a 47-email thread with none of your words.
"""

import os

ENTRY = (
    "I'm sorry I replied to your email, then replied to my own reply, "
    "then marked both urgent. The thread is now 47 emails long and "
    "none of them are from you."
)


def main():
    assert len(ENTRY) < 160, f"entry is {len(ENTRY)} chars, cap is 160"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
