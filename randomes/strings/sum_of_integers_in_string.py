"""
Ваша задача в этом задании — реализовать функцию, которая вычисляет сумму целых чисел внутри строки.
Например, в строке "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"
сумма целых чисел равна 3635.

Примечание: будут проверяться только положительные целые числа.
"""
import unittest
from typing import Any, Callable, Tuple
import re


def sum_of_integers_in_string(s: str) -> int:
    """
    Вычисляет сумму чисел из строки.
    """
    return sum(int(x) for x in re.split(r"[^\d]", s) if x)


def sum_of_integers_in_string_2(s: str) -> int:
    """
    Вычисляет сумму чисел из строки.
    """
    return sum(int(x) for x in re.findall(r"(\d+)", s))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sum_of_integers_in_string, (
        ("12.4", 16),
        ("h3ll0w0rld", 3),
        ("2 + 3 = ", 5),
        ("Our company made approximately 1 million in gross revenue last quarter.", 1),
        ("The Great Depression lasted from 1929 to 1939.", 3868),
        ("Dogs are our best friends.", 0),
        ("C4t5 are 4m4z1ng.", 18),
        ("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", 3635)
    ))
    test(sum_of_integers_in_string_2, (
        ("12.4", 16),
        ("h3ll0w0rld", 3),
        ("2 + 3 = ", 5),
        ("Our company made approximately 1 million in gross revenue last quarter.", 1),
        ("The Great Depression lasted from 1929 to 1939.", 3868),
        ("Dogs are our best friends.", 0),
        ("C4t5 are 4m4z1ng.", 18),
        ("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", 3635)
    ))
