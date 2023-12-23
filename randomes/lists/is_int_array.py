"""
Напишите функцию с сигнатурой, показанной ниже:

def is_int_array(arr):
    return True

    возвращает true  / Trueесли каждый элемент массива является целым числом или числом с плавающей запятой без десятичных знаков.
    возвращает true  / Trueесли массив пуст.
    возвращает false / Falseдля каждого другого входа
"""

from typing import Any


def is_int_array(arr: Any) -> bool:
    """
    Проверяет, что передан список и содержит только целые числа типа int или float.
    """
    return not next((1 for x in [' ', arr][isinstance(arr, list)] if not isinstance(x, (int, float)) or x % 1), 0)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([], True),
        ([1, 2, 3, 4], True),
        ([-11, -12, -13, -14], True),
        ([1.0, 2.0, 3.0], True),
        ([1, 2, None], False),
        (None, False),
        ("", False),
        ([None], False),
        ([1.0, 2.0, 3.0001], False),
        (["-1"], False),
        ([1.2, 1.8, 3], False),
    )
    for key, val in data:
        assert is_int_array(key) == val


if __name__ == '__main__':
    test()
