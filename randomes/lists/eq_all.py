"""
Задача

Создать функцию eq_all ли все элементы любой итерации это определяет, равны;
итерация может быть бесконечной. Возвращаемое значение — это bool.

Примеры

eq_all('aaa')   : True
eq_all('abc')   : False
eq_all('')      : True

eq_all([0,0,0]) : True
eq_all([0,1,2]) : False
eq_all([])      : True

Примечания

Чтобы результат функции был True, iterableдолжно быть конечным; False, однако,
может быть результатом элемента, конечно удаленного от левого конца.
Не будет тестов с бесконечными сериями одинаковых элементов.
Элементы будут примитивными значениями.
"""

from typing import Iterable


def eq_all(iterable: Iterable) -> bool:
    """
    Проверяет являются ли все элементы последовательности одинаковыми.
    Исключение:
        - True == 1
        - False == 0
    """
    return not next((1 for i, x in enumerate(iterable) if (n := [i and n, x][not i]) != x), 0)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('', True),
        ([], True),
        ((), True),
        ({}, True),
        ({2}, True),
        (set(), True),
        ('aaa', True),
        ('abc', False),
        ({2, 3}, False),
        ([0, 0, 0], True),
        ({'a': 32}, True),
        ([0, 1, 2], False),
        (('A', 'A', 'A'), True),
        (('A', 'A', 'a'), False),
        ({'a': 32, 'A': 32}, False),
    )
    for key, val in data:
        assert eq_all(key) == val


if __name__ == '__main__':
    test()
