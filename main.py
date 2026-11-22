"""Write the boiled-kettle text to entry.txt in the make.fun output directory."""

import os
from pathlib import Path

TEXT = (
    "The kettle has boiled and clicked off. Nobody pours it yet. "
    "The kitchen holds the warmth a little longer, the window fogs at the edges, "
    "and for these few seconds the house is not waiting for anything to happen next. "
    "It already happened. This is the after."
)

# Expected length of TEXT in Unicode code points; checked after writing.
EXPECTED_CHARS = 255


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    out_file.write_bytes(TEXT.encode("utf-8"))

    written = out_file.read_bytes().decode("utf-8")
    if len(written) != EXPECTED_CHARS:
        raise SystemExit(
            f"entry.txt check failed: {out_file} has {len(written)} characters, "
            f"expected {EXPECTED_CHARS}"
        )


if __name__ == "__main__":
    main()
