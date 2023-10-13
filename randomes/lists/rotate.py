"""
Напишите функцию, которая поворачивает двумерный массив (матрицу) по или
против часовой стрелки на 90 градусов и возвращает повернутый массив.

Функция принимает два параметра: матрицу и строку, задающую направление
или поворот. Направление будет либо "clockwise"или "counter-clockwise". 
"""


def rotate(matrix: list, direction: str) -> list:
    """
    Поворачивает матрицу в зависимости от direction.
    """
    if direction == 'clockwise':
        return list(map(list, zip(*matrix[::-1])))
    return list(map(list, zip(*matrix)))[::-1]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    data = (
        ((matrix, 'counter-clockwise'), [[3, 6, 9], [2, 5, 8], [1, 4, 7]]),
        ((matrix, 'clockwise'), [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    )
    for key, val in data:
        assert rotate(*key) == val


if __name__ == '__main__':
    test()
