import re
from pathlib import Path


def main(content):
    rows = process_content(content)
    lefts, rights = zip(*[re.sub(r" +", " ", r).split(" ") for r in rows])
    total = sum(abs(int(l) - int(r)) for l, r in zip(sorted(lefts), sorted(rights)))
    print(f"Total: {total}")


def process_content(content):
    return [row for row in content.split("\n") if row.strip() != ""]


if __name__ == "__main__":
    path = Path(__file__).resolve().parent / "input.txt"
    with open(path) as f:
        content = f.read()

    main(content)
