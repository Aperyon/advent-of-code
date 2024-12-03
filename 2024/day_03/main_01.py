import re
from pathlib import Path
from operator import mul


def main(content):
    pattern = r"mul\((?P<n1>\d{1,3})\,(?P<n2>\d{1,3})\)"
    total = sum(mul(*map(int, m)) for m in re.findall(pattern, content))

    print(f"Total: {total}")
    return total


if __name__ == "__main__":
    path = Path(__file__).resolve().parent / "input.txt"
    with open(path) as f:
        content = f.read()
    main(content)
