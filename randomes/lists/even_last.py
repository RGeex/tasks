"""
Дана последовательность целых чисел. Необходимо вернуть сумму всех целых чисел,
индекс которых четный (в COBOL — нечетный), умноженную на число, находящееся в
конце последовательности.

Индексы в последовательности начинаются с 0.

Если последовательность пуста, следует вернуть 0.

"""
import unittest
from typing import Any, Callable, List, Tuple


def even_last(numbers: List[int]) -> int:
    """
    Вычисляет значение из списка чисел по заданному алгоритму.
    """
    return sum(numbers[::2]) * ([0] + numbers)[-1]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(even_last, (
        ([2, 3, 4, 5], 30),
        ([], 0),
    ))
