"""One-Line Laugh-Off -- entry program.

Writes one funny line (1 to 200 characters, UTF-8, no trailing newline)
to /output/entry.txt. Standard library only, no network, deterministic.
"""
import os

MAX_CHARS = 200

JOKE = (
    "My Roomba filed a noise complaint \u2014 against me, "
    "for vacuuming while it vacuums."
)


def checked(line: str) -> str:
    """Refuse to write anything the gate would reject."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip() or not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry must be 1 to %d characters" % MAX_CHARS)
    return line


def main() -> None:
    line = checked(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
