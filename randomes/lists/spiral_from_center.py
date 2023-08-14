"""
Создать матрицу закрученную по спирали из центра вправо и по часовой стрелке.
"""


def spiral_from_center(size: int) -> list:
    """
    Создает квадратную матрицу, нечетной длины, заполняя по спирали
    из центра значениями от 1 до n**2.
    """
    size -= not size % 2
    matrix = [[0] * size for _ in range(size)]
    dx, dy, x, y = 0, 1, size // 2, size // 2
    for value in range(size**2):
        matrix[x][y] = value + 1
        if not matrix[x+dy][y-dx]:
            dx, dy = dy, -dx
        x += dx
        y += dy
    return list(map(list, list(zip(*matrix))[::-1]))


def display(size: int) -> None:
    """
    Печатает матрицу построчно, дополняя числа 0-ми, если необходимо.
    """
    for line in spiral_from_center(size):
        print(*[str(x).zfill(len(str(size**2))) for x in line])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (3, [
            [7, 8, 9],
            [6, 1, 2],
            [5, 4, 3],
        ]),
        (5, [
            [21, 22, 23, 24, 25],
            [20, 7, 8, 9, 10],
            [19, 6, 1, 2, 11],
            [18, 5, 4, 3, 12],
            [17, 16, 15, 14, 13],
        ]),
    )

    for key, val in data:
        assert spiral_from_center(key) == val


if __name__ == '__main__':
    test()
