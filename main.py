"""Write the held-note text to entry.txt in the make.fun output directory."""

import os
from pathlib import Path

TEXT = (
    "Somewhere under all the answering, a note is being held. "
    "Not struck, not resolving, just kept, the way a room keeps its warmth "
    "after the fire is out. You are not the one holding it. It is holding you, "
    "and it can keep holding you for exactly as long as you stay."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
