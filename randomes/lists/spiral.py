"""
Заполнение матрицы по списрали.

На вход подаются 2 числа, являющихся размером матрицы.
Необходимо вернуть матрицу заполненную числами от 1 до m * n
располагающимися по спирали с началом в точке 0, 0.
"""


def spiral(m: int, n: int) -> list[int]:
    """Располагает числа от 1 до m * n, в матрице по списрали."""
    matrix = [[0] * m for _ in range(n)]

    dx, dy, x, y = 0, 1, 0, 0

    for val in range(1, m * n + 1):
        matrix[x][y] = val
        if matrix[(x + dx) % n][(y + dy) % m]:
            dx, dy = dy, -dx
        x += dx
        y += dy

    return matrix


def test() -> None:
    """Тестирование работы алгоритмов."""
    data = [
        ([
            [1, 2],
            [6, 3],
            [5, 4],
        ], (2, 3)),
        ([
            [1, 2, 3],
            [6, 5, 4],
        ], (3, 2)),
        ([
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5],
        ], (3, 3)),
    ]

    for matrix, args in data:
        assert spiral(*args) == matrix


if __name__ == '__main__':
    test()
