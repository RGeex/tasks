"""
Дан массив целых чисел. a и целые числа t и x посчитайте, сколько элементов в массиве можно
приравнять к определенному значению. t путем увеличения / уменьшения его x(или ничего не делать).

# ex 1

a = [11, 5, 3]
t = 7
x = 2

count(a, t, x) # => 3

    Число 11 можно сделать равным 7, вычтя 2 дважды.
    5 можно сделать равным 7, добавив 2.
    Число 3 можно сделать равным 7, прибавив 2 дважды.

# ex 2

a = [-4,6,8]
t = -7
x = -3

count(a, t, x) # => 2

Ограничения

-10 18 <= a[i],t,x <= 10 18

3 <= |a| <= 10 4

"""
import unittest
from typing import Any, Callable, List, Tuple


def count(a: List[int], t: int, x: int) -> int:
    """
    Подсчитывает кол-во элементов в списке, которые при увеличении / уменьшении на x могут быть равны t.
    """
    return sum(not ((n - t) % x if x else n != t) for n in a)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(count, (
        (([11, 5, 3], 7, 2), 3),
        (([11, 5, 7], 7, 0), 1),
        (([-4, 6, 8], -7, -3), 2),
    ))
