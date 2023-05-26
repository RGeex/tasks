"""
Напишите функцию, вычисляющую определитель
квадратной матрицы.

"""


def determinant(matrix: list) -> int:
    """Вычисляет определитель квадратной матрицы."""
    M = matrix

    if len(M) == 1:
        return M[0][0]
    if len(M) == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]

    res = 0
    for x in range(len(M)):
        tmp = [v[:x] + v[x+1:] for i, v in enumerate(M) if i]
        res += M[0][x] * determinant(tmp) * [1, -1][x % 2]

    return res


def test() -> None:
    """Тестирование работы алгоритмов."""
    data = [
        ([[5]], 5),
        ([[4, 6], [3, 8]], 14),
        ([[2, 4, 2], [3, 1, 1], [1, 2, 0]], 10),
    ]

    for arr, val in data:
        assert determinant(arr) == val


if __name__ == '__main__':
    test()
