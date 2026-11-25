# SPDX-License-Identifier: MIT
"""One Word from Grandma — writes the single word grandma would text about AI.

The word: GeePeeTea. Asked about ChatGPT, grandma mishears the last letter
and texts back the name as she heard it — GPT, but make it tea. It is the
word she would actually send: warm, a little baffled, funny on its own,
tied specifically to AI, and spelled so both halves of the joke (Gee-Pee
and Tea) stay instantly readable in camelCase. No punctuation, no spaces,
no trailing newline — exactly one word, byte for byte, every run.
"""
import os

WORD = "GeePeeTea"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
