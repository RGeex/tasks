"""
Необходимо доработать функцию/метод для вычисления двух самых старших чисел.
Она должна принимать в качестве аргумента массив чисел и возвращать два самых старших числа из массива .
Возвращаемое значение должно представлять собой массив в формате [second oldest age,  oldest age].

Порядок передаваемых чисел может быть любым. Массив всегда будет содержать как минимум 2 элемента.
Если есть два или более самых старых возраста, то верните оба в формате массива.

Например (Ввод --> Вывод):

[1, 2, 10, 8] --> [8, 10]
[1, 5, 87, 45, 8, 8] --> [45, 87]
[1, 3, 10, 0]) --> [3, 10]

[ 3, 4, 5, 6, 5, 6, 7, 7, 8, 9 ]
"""
import unittest
from typing import Any, Callable, List, Tuple


def two_oldest_ages(ages: List[int]) -> List[int]:
    """
    Возвращает 2 максимальных числа сипска.
    """
    return sorted(ages)[-2:]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(two_oldest_ages, (
        ([1, 5, 87, 45, 8, 8], [45, 87]),
        ([6, 5, 83, 5, 3, 18], [18, 83]),
        ([10, 1], [1, 10]),
    ))
