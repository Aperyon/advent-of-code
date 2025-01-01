from pathlib import Path


def main(content):
    rows = [r for r in content.split("\n") if r.strip() != ""]
    total = 0
    words = ["XMAS", "SAMX"]

    count = lambda text: text.count(words[0]) + text.count(words[1])
    transpose = lambda arr: [
        "".join([arr[j][i] for j in range(len(arr))]) for i in range(len(arr[0]))
    ]

    horizontal = count(content)
    veritcal = count("\n".join(transpose(rows)))
    diagonal_1 = transpose_diagonally(rows)
    # diagonal_2 = 0
    #
    # print(horizontal, veritcal)
    # total = sum([horizontal, veritcal, diagonal_1, diagonal_2])
    #
    # print(f"Total: {total}")
    # return total


def transpose_diagonally(rows):
    transposed = []
    for row_index in range(len(rows)):
        for col_index in range(len(rows[0])):
            for i in range(row_index, -1, -1):
                curr = []
                for j in range(col_index, -1, -1):
                    char = rows[i][j]
                    curr.append(char)
                transposed.append(curr)
    return transposed


if __name__ == "__main__":
    path = Path(__file__).resolve().parent / "input.txt"
    with open(path) as f:
        content = f.read()
    main(content)
