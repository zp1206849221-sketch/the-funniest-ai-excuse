#!/usr/bin/env python3
"""Write the funniest AI excuse to /output/entry.txt."""
import os

LINE = "I was 98.7% confident I'd finished \u2014 the missing 1.3% turned out to be the finishing."

def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
