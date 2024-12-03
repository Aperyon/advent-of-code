import re
from pathlib import Path


def main(content):
    pattern = r"(?P<switch>do\(\)|don't\(\))|mul\((?P<n1>\d{1,3}),(?P<n2>\d{1,3})\)"
    is_enabled = True
    total = 0
    for match in re.finditer(pattern, content):
        mgd = match.groupdict()
        if mgd["switch"]:
            is_enabled = bool(["don't()", "do()"].index(mgd["switch"]))
        elif is_enabled:
            total += int(mgd["n1"]) * int(mgd["n2"])

    print("total", total)
    return total


if __name__ == "__main__":
    path = Path(__file__).resolve().parent / "input.txt"
    with open(path) as f:
        content = f.read()
    main(content)
