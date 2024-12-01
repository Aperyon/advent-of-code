import re
from pathlib import Path
from collections import Counter


def main(content):
    rows = process_content(content)
    lefts, rights = zip(*[re.sub(r" +", " ", r).split(" ") for r in rows])
    counter = Counter(rights)
    total = sum([int(counter.get(str(l), "0")) * int(l) for l in lefts])
    print(f"Total: {total}")


def process_content(content):
    return [row for row in content.split("\n") if row.strip() != ""]


if __name__ == "__main__":
    path = Path(__file__).resolve().parent / "input.txt"
    with open(path) as f:
        content = f.read()

    main(content)
