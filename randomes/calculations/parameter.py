"""
Давайте определим parameter числа nкак наименьшее общее кратное (НОК)
суммы его цифр и их произведения.

Вычислить параметр заданного числа n.

Для n = 1234, вывод должен быть 120.
1+2+3+4=10и 1*2*3*4=24, НОК(10,24)=120
"""

from math import lcm
from operator import mul, add
from functools import reduce


def parameter(n: int) -> int:
    """
    Поиск НОК суммы и произведения цифр заданного числа.
    """
    return lcm(*[reduce(x, map(int, str(n))) for x in (add, mul)])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (1, 1),
        (2, 2),
        (11, 2),
        (22, 4),
        (91,  90),
        (239, 378),
        (344, 528),
        (1234, 120),
    )
    for key, val in data:
        assert parameter(key) == val


if __name__ == '__main__':
    test()
