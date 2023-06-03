from operator import add
from functools import reduce


def solve(board, m=0, n=0):
    """Решатель судоку, перебором допустимых значений."""

    # поиск первой пустой клетки
    for x in range(m, 9):
        for y in range(x == m and n, 9):
            if board[x][y]:
                continue

            # поиск допустимых значений для текущей пустой клетки
            row, col = map(lambda n: n - n % 3, (x, y))
            values = set(range(1, 10)) - (
                set(reduce(add, [board[row+n][col:col+3] for n in range(3)])) |
                {board[n][y] for n in range(9)} |
                set(board[x]) |
                {0}
            )

            for num in sorted(values):
                board[x][y] = num
                if solve(board, x, y + 1):
                    return board
                board[x][y] = 0
            return False
    return True


def test() -> None:
    """Тестирование работы алгоритмов."""
    problem = [
        [9, 0, 0, 0, 8, 0, 0, 0, 1],
        [0, 0, 0, 4, 0, 6, 0, 0, 0],
        [0, 0, 5, 0, 7, 0, 3, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 4, 0],
        [4, 0, 1, 0, 6, 0, 5, 0, 8],
        [0, 9, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 7, 0, 3, 0, 2, 0, 0],
        [0, 0, 0, 7, 0, 5, 0, 0, 0],
        [1, 0, 0, 0, 4, 0, 0, 0, 7]
    ]

    solution = [
        [9, 2, 6, 5, 8, 3, 4, 7, 1],
        [7, 1, 3, 4, 2, 6, 9, 8, 5],
        [8, 4, 5, 9, 7, 1, 3, 6, 2],
        [3, 6, 2, 8, 5, 7, 1, 4, 9],
        [4, 7, 1, 2, 6, 9, 5, 3, 8],
        [5, 9, 8, 3, 1, 4, 7, 2, 6],
        [6, 5, 7, 1, 3, 8, 2, 9, 4],
        [2, 8, 4, 7, 9, 5, 6, 1, 3],
        [1, 3, 9, 6, 4, 2, 8, 5, 7]
    ]

    assert solve(problem) == solution


if __name__ == '__main__':
    test()
