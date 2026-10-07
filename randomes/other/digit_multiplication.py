"""
Перемножьте соседние цифры, не разделённые символами «a» '-'или «a» '+'в строке, а затем сложите их.

Примеры
"53+5"    -->   20  # = 5 * 3 + 5
"266-66"  -->   36  # = 2 * 6 * 6 - 6 * 6
"555"     -->  125  # = 5 * 5 * 5
"""
import unittest
from typing import Any, Callable, Tuple
import re


def digit_multiplication(expression: str) -> int:
    """
    Перемножает соседние цифры, а затем вытолняет дрпугим математические операции.
    """
    return eval("".join(["*".join(x) for x in re.split(r"([\+\-])", expression)]))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(digit_multiplication, (
        ('10000345+77-2', 47),
        ('12345-11989+1231111', -522),
        ('2395', 270),
        ('3434343-12121212+4949494-122', 191788),
        ('13579+9+9+9-11', 971),
        ('6-3-3-3-4', -7),
        ('355+43', 87),
    ))
