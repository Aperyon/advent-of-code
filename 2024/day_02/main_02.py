from itertools import pairwise, product
from pathlib import Path


def main(content):
    processed_rows = process_content(content)
    count_safe_reports(processed_rows)


def count_safe_reports(reports):
    safe_reports = sum(validate_report(report) for report in reports)
    print(f"Safe reports: {safe_reports}")
    return safe_reports


def validate_report(report):
    consistent = lambda x, y: sorted([x, y])[report[0] > report[1]] == x
    bound = lambda x, y: 1 <= abs(x - y) <= 3
    results = all([c(*v) for v, c in product(pairwise(report), [consistent, bound])])
    if results:
        return results
    second = any(second_try(report))
    if second:
        print(report)

    return second


def second_try(report):
    bound = lambda x, y: 1 <= abs(x - y) <= 3
    results = []
    for i in range(0, len(report)):
        new_report = [*report]
        new_report.pop(i)
        consistent = False
        consistent = new_report == sorted(new_report) or new_report == sorted(
            new_report, reverse=True
        )
        current = (
            all([c(*v) for v, c in product(pairwise(new_report), [bound])])
            and consistent
        )
        results.append(current)
    return results


def process_content(content):
    return [
        [int(l) for l in r.split(" ")] for r in content.split("\n") if r.strip() != ""
    ]


if __name__ == "__main__":
    path = Path(__file__).resolve().parent / "input.txt"
    with open(path) as f:
        content = f.read()

    main(content)
