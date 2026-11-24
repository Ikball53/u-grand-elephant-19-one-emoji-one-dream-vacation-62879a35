"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt: Mount Fuji (U+1F5FB).

Why this emoji: a snow-capped Fuji at sunrise is a postcard in a
single glyph. It plainly names a dream vacation (a mountain, a
faraway place), it is vivid at a glance, and it is specific — one
particular dream trip, Japan, not just any holiday. It is a fresher
pick than the beach cliche, yet it reads instantly across cultures
and screens, even at small size.

Deterministic, stdlib only, no network, no input.
The output is one character, four UTF-8 bytes, no trailing newline.
"""

import os

ENTRY = "\U0001F5FB"  # 🗻 MOUNT FUJI


def main() -> None:
    # Gate check, done before writing anything: the brief requires
    # 1 to 8 characters, and this entry is exactly one emoji.
    assert len(ENTRY) == 1, "entry must be exactly one emoji"
    assert ENTRY.strip() != "", "entry must not be only whitespace"
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # Write exact bytes: UTF-8, no trailing newline, no extra content.
    with open(output_path, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
