"""
Ваша задача — перечислить все числа до 2**. n- 1, содержащие единицу в тех же местах/битах,
что и двоичное представление b. b будет 1, 2, 4, 8 и т. д.
Например: solution(4,2)вернет [2,3,6,7,10,11,14,15].
Двоичные числа от 1 до 16:
8 4 2 1 (место)
0 0 0 1
0 0 1 0
0 0 1 1
0 1 0 0
0 1 0 1
0 1 1 0
0 1 1 1
1 0 0 0
1 0 0 1
1 0 1 0
1 0 1 1
1 1 0 0
1 1 0 1
1 1 1 0
1 1 1 1
Числа, в которых на месте 2 стоит 1, это 2, 3, 6, 7, 10, 11, 14 и 15.
Другие примеры:
solution(0,1)= []
solution(6,8)= [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40, 41, 42, 43, 44,
45, 46, 47, 56, 57, 58, 59, 60, 61, 62, 63]
Если b = 0, вернуть пустой список. 
"""
import unittest
from typing import Any, Callable, List, Tuple


def comparison_bits(n: int, b: int) -> List[int]:
    """
    Побитовое сравнение.
    """
    return [x for x in range(2 ** n) if x & b]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(comparison_bits, (
        ((4, 2), [2, 3, 6, 7, 10, 11, 14, 15]),
        ((6, 8), [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30,
         31, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57, 58, 59, 60, 61, 62, 63]),
        ((5, 32), []),
        ((6, 0), []),
        ((0, 1), []),
    ))
