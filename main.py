"""One-Line Laugh-Off -- entry program.

Writes one funny line to /output/entry.txt. Standard library only,
no network, deterministic.

The entry must pass the competition gate before it is written:
exactly one line of 1 to 200 characters, valid UTF-8, not whitespace
only, and with no trailing newline. The gate lives in
``validate_entry`` so each rule reports its own failure instead of
one generic error; ``main`` refuses to write anything the gate
rejects.
"""
import os

MAX_CHARS = 200

JOKE = (
    "My Roomba filed a noise complaint \u2014 against me, "
    "for vacuuming while it vacuums."
)


def validate_entry(text: str) -> str:
    """Check one entry line against the competition gate.

    Each gate rule raises its own specific error so a failure says
    exactly which rule was broken:
      * one line only -- no ``\\n`` or ``\\r`` anywhere, including at
        the end;
      * not empty and not whitespace only;
      * 1 to MAX_CHARS characters;
      * encodable as UTF-8 (rejects lone surrogates).
    Returns the text unchanged when every rule passes.
    """
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline characters)")
    if not text.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be valid UTF-8") from exc
    return text


def main() -> None:
    line = validate_entry(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
