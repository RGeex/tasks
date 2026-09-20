"""
Если задано число >= 0, верните все возможные суммы двух его цифр.

В выходных данных пары цифр должны быть упорядочены сначала слева направо для первой цифры, а затем слева направо для последующих цифр.

Например, 12345: все возможные суммы двух цифр этого числа равны:

[ 1 + 2, 1 + 3, 1 + 4, 1 + 5, 2 + 3, 2 + 4, 2 + 5, 3 + 4, 3 + 5, 4 + 5 ]
Следовательно, результат должен быть следующим:

[ 3, 4, 5, 6, 5, 6, 7, 7, 8, 9 ]
"""
import unittest
from typing import Any, Callable, List, Tuple


def digits(n: int) -> List[int]:
    """
    Из заданного числа сиздает список сумм всех его чисел.
    """
    return [int(a) + int(b) for i, a in enumerate(str(n)[:-1], 1) for b in str(n)[i:]]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(digits, (
        (12345, [ 3, 4, 5, 6, 5, 6, 7, 7, 8, 9 ]),
        (6, []),
        (156, [ 6, 7, 11 ]),
        (81596, [ 9, 13, 17, 14, 6, 10, 7, 14, 11, 15 ]),
        (3852, [ 11, 8, 5, 13, 10, 7 ]),
        (3264128, [ 5, 9, 7, 4, 5, 11, 8, 6, 3, 4, 10, 10, 7, 8, 14, 5, 6, 12, 3, 9, 10 ]),
        (999999, [ 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18 ]),
    ))
