"""
Moser Streaming

В геометрии, если расположить точки на окружности и соединить каждую пару точек прямыми линиями,
то окружность разделится на области.

Максимальное количество создаваемых регионов соответствует известной последовательности кругов Мозера:

1, 2, 4, 8, 16, 31, 57, 99, 163, 256, ...

Задача

Ваша задача — создать бесконечный генератор , который будет выдавать значения этой
последовательности одно за другим.

Последовательность начинается с n = 1.

Реализуйте функцию-генератор:

def moser():

Это позволяет бесконечно повторять значения последовательности кругов Мозера.
Пример

for i in moser():
    print(i)

# prints 1, 2, 4, 8, 16, 31, 57, 99, 163, 256, 386, 562, 794, 1093...


"""
import unittest
from typing import Any, Callable, Tuple, Generator
from math import comb
from itertools import islice


def moser() -> Generator[int]:
    """
    Генератор Мозера.
    """
    n = 1
    while True:
        yield comb(n, 4) + comb(n, 2) + 1
        n += 1


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(lambda x: x, (
        (list(islice(moser(), 10)), [1, 2, 4, 8, 16, 31, 57, 99, 163, 256]),
    ))
