from main_01 import transpose_diagonally


def test_transpose_diagonally():
    content = ["ab", "cd"]
    result = transpose_diagonally(content)
    assert result == [["a"], ["b", "c"], ["d"]]
