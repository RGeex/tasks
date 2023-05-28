"""
Дана квадратная матрица. Сформировать новую матрицу,
полученную из исходной путем поворота относительно
центра на 90 по часовой стрелке
"""


def create_matrix(N: int, M: int | None = None) -> list:
    """Создание матрицы N x M, где N - строки, M - столбцы."""
    M = M or N  # если не задан M, то матрица квадратная

    # Создание матрицы N x M, заполненной 0-ми
    matrix = [[0] * M for _ in range(N)]

    # Заполнение матрицы порядковыми номерами
    for i in range(N * M):
        matrix[i // M][i % M] = i + 1

    return matrix


def turn_matrix(lst: list) -> list:
    """Поворачивает матрицу по часовой стрелке."""
    return list(map(list, zip(*lst[::-1])))


def test() -> None:
    """Тестирование работы алгоритмов."""
    matrix1 = create_matrix(3)
    matrix2 = turn_matrix(matrix1)
    matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix4 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    assert matrix1 == matrix3
    assert matrix2 == matrix4


if __name__ == '__main__':
    test()
