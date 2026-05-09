"""
Возьмём целое число n (n >= 0)и цифра d (0 <= d <= 9)в виде целого числа.

Возведите все числа в квадрат k (0 <= k <= n)от 0 до n.

Посчитайте количество цифр dиспользуется при написании всех k**2.

Реализуйте функцию, принимающую n и dв качестве параметров и возвращаем это число.
Примеры:

n = 10, d = 1 
the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

The function, when given n = 25 and d = 1 as argument, should return 11 since
the k*k that contain the digit 1 are:
1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
So there are 11 digits 1 for the squares of numbers between 0 and 25.

Обратите внимание, что 121имеет вдвое больше цифры 1.

"""
import unittest
from typing import Any, Callable, Tuple


def nb_dig(n: int, d: int) -> int:
    """
    Подсчитывакт кол-во цифр D в диапазоне квадратов последовательных чисел до N.
    """
    return ''.join([str(x ** 2) for x in range(n + 1)]).count(str(d))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(nb_dig, (
        ((5750, 0), 4700),
        ((11011, 2), 9481),
        ((12224, 8), 7733),
        ((11549, 1), 11905),
        ((14550, 7), 8014),
        ((8304, 7), 3927),
        ((10576, 9), 7860),
        ((12526, 1), 13558),
        ((7856, 4), 7132),
        ((14956, 1), 17267),
    ))
