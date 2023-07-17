"""
Имея строку, содержащую только буквы, вы должны найти количество уникальных
строк (включая саму строку), которые могут быть получены путем перестановки
букв в строке.  Строки нечувствительны к регистру.

ПОДСКАЗКА: Генерация всех уникальных строк и длины вызовов не является отличным
решением этой проблемы. Это можно сделать намного быстрее...
"""

from collections import Counter
from operator import floordiv
from functools import reduce
from math import factorial


def uniq_count(s: str) -> int:
    """Поиск ко-ва уникальных строк, путем перестановки символов."""
    return reduce(floordiv, map(factorial, (len(s), *Counter(s.lower()).values())))


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        ("", 1),
        ("AB", 2),
        ("AAA", 1),
        ("ABC", 6),
        ("AbA", 3),
        ("ABBb", 4),
        ("AbcD", 24),
        ("BEST", 24),
        ("ASTON", 120),
    )

    for key, val in data:
        assert uniq_count(key) == val


if __name__ == '__main__':
    test()
