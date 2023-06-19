"""
Реализовать алгоритм вычисления умножения матрицы на вектор.
"""

MATRIX = list[list[int | float]]


def multx(matrix: MATRIX, vector: MATRIX) -> MATRIX:
    """Умножение матрицы на вектор."""
    vector = [v for k in vector for v in k]
    return [[a * b for a, b in zip(val, vector)] for val in matrix]


def test() -> None:
    """Тестирование работы алгоритмов."""
    data1 = [
        [16, 11, 29, 18, 29],
        [28, 23, 14, 18, 10],
        [18, 25, 17, 29, 22],
        [13, 23, 20, 19, 22],
        [18, 11, 10, 26, 28],
    ]
    data2 = [
        [16, 33, 87, 36, 87],
        [28, 69, 42, 36, 30],
        [18, 75, 51, 58, 66],
        [13, 69, 60, 38, 66],
        [18, 33, 30, 52, 84],
    ]
    vector = [
        [1], [3], [3], [2], [3],
    ]

    assert multx(data1, vector) == data2


if __name__ == '__main__':
    test()
