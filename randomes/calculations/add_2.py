"""
Создайте функцию add(n)/ Add(n)которая возвращает функцию, всегда прибавляющую n к любому числу.

Примечание для Java: тип возвращаемого значения и методы не указаны, что несколько усложняет задачу.

add_one = add(1)
add_one(3)  # 4

add_three = add(3)
add_three(3) # 6

"""
import unittest
from typing import Any, Callable, Tuple


def add(n: int) -> Callable:
    """
    Увеличивает заданное число на N.
    """
    return lambda x: n + x


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(add(1), (
        (3, 4),
    ))
    test(add(0), (
        (-15, -15),
    ))
    test(add(3), (
        (5, 8),
        (5, 8),
    ))

