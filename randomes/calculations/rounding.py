"""
Задача

Округлите заданное число. nдо ближайшего кратного m.

Если nнаходится точно посередине между двумя кратными m, вернуть n вместо.
Пример

Для n = 20, m = 3Результат должен быть следующим: 21.

Для n = 19, m = 3Результат должен быть следующим: 18.

Для n = 50, m = 100Результат должен быть следующим: 50.
Ввод/вывод

    [input]целое число n

1 ≤ n < 10^9.

    [input]целое число m

3 ≤ m < 109.

    [output]целое число

"""
import unittest
from typing import Any, Callable, Tuple


def rounding_1(n: int, m: int) -> int:
    """
    Округляет n до ближайшего кратнорго m.
    """
    return [min(x := [(n // m + i) * m for i in range(2)], key=lambda k: abs(n - k)), n][len({abs(k - n) for k in x}) == 1]


def rounding_2(n: int, m: int) -> int:
    """
    Округляет n до ближайшего кратнорго m.
    """
    return n if n % m == m / 2 else m * round(n / m)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(rounding_1, (
        ((20, 3), 21),
        ((19, 3), 18),
        ((1, 10), 0),
        ((50, 100), 50),
        ((123, 456), 0),
        ((300873066, 4), 300873066),
    ))
    test(rounding_2, (
        ((20, 3), 21),
        ((19, 3), 18),
        ((1, 10), 0),
        ((50, 100), 50),
        ((123, 456), 0),
        ((300873066, 4), 300873066),
    ))
