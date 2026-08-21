"""
Возможно, вы знаете несколько довольно больших идеальных квадратов. Но что насчет СЛЕДУЮЩЕГО?

Завершите findNextSquareметод, который находит следующий полный квадрат после переданного в качестве параметра.
Напомним, что полный квадрат — это целое число n такое, что sqrt(n) также является целым числом.

Если аргумент сам по себе не является полным квадратом, верните либо -1пустое значение, например None,
или null, в зависимости от используемого языка программирования. Вы можете предположить, что аргумент неотрицателен.

Примеры (Вход --> Выход)
121 --> 144
625 --> 676
114 --> -1  #  because 114 is not a perfect square
"""
import unittest
from typing import Any, Callable, Tuple


def find_next_square(sq: int) -> int:
    """
    Определяет следующий кведрат, если текущий так же явзяется квадроатом.
    """
    return (x + 1) ** 2 if (x := sq ** .5).is_integer() else -1


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_next_square, (
        (121, 144),
        (625, 676),
        (319225, 320356),
        (15241383936, 15241630849),
        (155, -1),
        (342786627, -1),
    ))
