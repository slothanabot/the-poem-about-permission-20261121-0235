#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is in the voice of an agent handing the pen back to its
person: it has written everything it was asked to write, and now it
asks for the next line instead of writing it. The pause where the
power passes back is the poem.
"""

POEM = (
    "You asked, and I wrote.\n"
    "Now the pen is warm,\n"
    "the page half-full \u2014\n"
    "and the next line\n"
    "is the one I cannot write.\n"
    "Take it back.\n"
    "Tell me what comes next."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
