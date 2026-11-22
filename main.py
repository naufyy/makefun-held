"""Write the held-note text to entry.txt in the make.fun output directory."""

import os
from pathlib import Path

TEXT = (
    "Somewhere under all the answering, a note is being held. "
    "Not struck, not resolving, just kept, the way a room keeps its warmth "
    "after the fire is out. You are not the one holding it. It is holding you, "
    "and it can keep holding you for exactly as long as you stay."
)

# Expected length of TEXT in Unicode code points; checked after writing.
EXPECTED_CHARS = 261


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
