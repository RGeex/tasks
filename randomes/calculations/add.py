"""
Для выполнения этого упражнения вам придётся забыть, как складывать два числа.

Лучше всего это можно объяснить с помощью следующего мема:

Дайане Ривас подсчитывает сумму, участвуя в гватемальском телевизионном шоу "Combate" в мае 2016 года.

Проще говоря, наш метод не приемлет переноса чисел и просто записывает каждое вычисленное число :-)

Можно предположить, что оба числа являются положительными.
"""
import unittest
from typing import Any, Callable, Tuple
from itertools import zip_longest as zl


def add(num1: int, num2: int) -> int:
    """
    Сложение двух положительных чисел в столбик по парно, игнорируя правила.
    """
    return int(''.join([str(sum(map(int, x))) for x in zl(*[str(x)[::-1] for x in (num1, num2)], fillvalue='0')][::-1]))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(add, (
        ((2, 11), 13),
        ((0, 1), 1),
        ((0, 0), 0),
        ((16, 18), 214),
        ((26, 39), 515),
        ((122, 81), 1103),
    ))
