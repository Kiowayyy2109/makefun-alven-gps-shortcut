"""The GPS Swears It Was a Shortcut — one-line excuse entry.

Writes the GPS's single excuse line to /output/entry.txt.
"""

import os

LINE = (
    "I stand by the shortcut: the highway was jammed, the goat path was "
    "empty, and nobody told me the bridge retired in 1987."
)


def main() -> None:
    # The grader reads /output/entry.txt; the line must be a single
    # non-empty line of at most 200 characters, so guard it here.
    assert LINE.strip() and "\n" not in LINE and len(LINE) <= 200
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
