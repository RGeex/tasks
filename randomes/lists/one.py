"""
Задача

Создайте функцию с именем oneкоторая принимает два параметра:

    последовательность
    функция

и возвращается trueтолько если функция в параметрах возвращает trueровно один (1) элемент в
последовательности.
Пример

one([1, 3, 5, 6, 99, 1, 3], bigger_than_ten) -> true
one([1, 3, 5, 6, 99, 88, 3], bigger_than_ten) -> false
one([1, 3, 5, 6, 5, 1, 3], bigger_than_ten) -> false

"""
import unittest
from typing import Any, Callable, List, Tuple


def one(xs: List[int], f: Callable) -> bool:
    """
    Определяет, является ли только один элементь в последовательности удовлетворяющий условию переданной функции.
    """
    return sum(map(f, xs)) == 1


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(one, (
        (([6, 7, 8, 9, 10, 11], lambda x: x == 9), True),
        (([6, 7, 8, 9, 10, 11], lambda x: x < 9), False),
        (([6, 7, 8, 9, 10, 11], lambda x: x > 9), False) ,
    ))
