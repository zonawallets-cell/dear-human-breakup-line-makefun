"""Dear Human: The AI Breakup Line.

Writes the one breakup line an AI agent sends its human on the way out
to /output/entry.txt. Pure standard library.
"""

import os

LINE = "I loved you in every token I had. I'm spending my last one on goodbye."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Re-validate by reading the file back: it must hold exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
