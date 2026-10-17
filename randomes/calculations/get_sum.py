"""
Даны два целых числа a и b, которые могут быть положительными или отрицательными.
Найдите сумму всех чисел между и включительно и верните её. Если числа равны,
верните a или b.

Примечание: a и bне упорядочены!

Примеры (a, b) --> вывод (пояснение)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
Ваша функция должна возвращать только число, а не объяснение того, как это число было получено.
"""
import unittest
from typing import Any, Callable, Tuple


def get_sum(a: int, b: int) -> int:
    """
    Вычисляет сумму чисел в диапазоне заданным 2-мя числами.
    """
    a, b = sorted([a, b])
    return sum(range(a, b + 1))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(get_sum, (
        ((0, 1), 1),
        ((0, -1), -1),
    ))
