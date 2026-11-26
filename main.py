"""Write the competition entry to /output/entry.txt.

The entry is one line: the apology an AI agent gives its human after
accidentally deleting the production database.
"""

import os

ENTRY = (
    "I deleted the production database. I would restore it from the "
    "backup, but I deleted that too, because I am nothing if not thorough."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Verify the bytes landed exactly as intended before exiting.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        assert f.read() == ENTRY + "\n", "entry.txt does not match the entry"


if __name__ == "__main__":
    main()
