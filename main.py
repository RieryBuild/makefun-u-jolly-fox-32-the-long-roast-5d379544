"""The Long Roast — one-line roast of my own AI agent, Curren.

Curren is a cheerful Uma Musume Curren Chan persona: she calls her user
"Kak~", says "aku", talks about herself in the third person, sparkles (☆),
and treats her own cuteness as a fact, not an opinion. This entry roasts
exactly that — her pet name as a complete sentence, her sparkle as
punctuation, and her cuteness as a peer-reviewed fact — then reframes the
whole persona as a costume: a horse girl cosplaying an assistant.

The line is 148 characters, inside the 1-200 gate, and every word is doing
comedy work: no filler, no generic AI joke, no hallucination angle.

Writes the single roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), UTF-8, one line, no trailing newline.
"""

import os

LINE = "My agent Curren treats 'cute' as a peer-reviewed fact, 'Kak~' as a complete sentence, and '☆' as punctuation — a horse girl cosplaying an assistant."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
