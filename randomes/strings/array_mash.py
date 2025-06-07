"""
Объединить 2 массива вместе так, чтобы возвращаемый массив имел чередующиеся элементы 2 массивов.
Оба массива всегда будут иметь одинаковую длину.

например, [1,2,3] + ['a','b','c'] = [1, 'a', 2, 'b', 3, 'c']
"""
import typing
import unittest


def array_mash(a: list, b: list) -> list:
    """
    Объединяет 2 списка одинаковой длины, чередуя значения.
    """
    return [a for b in zip(a, b) for a in b]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(array_mash, (
        (([1, 2, 3], ['a', 'b', 'c']), [1, 'a', 2, 'b', 3, 'c']),
        (([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']), [1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e']),
        (([1, 1, 1, 1], [2, 2, 2, 2]), [1, 2, 1, 2, 1, 2, 1, 2]),
        (([1, 8, 'hello', 'dog'], ['fish', '2', 9, 10]), [1, "fish", 8, "2", "hello", 9, "dog", 10]),
        (([None, 4], [None, 'hello']), [None, None, 4, "hello"]),
        (([1], [2]), [1, 2]),
        ((['h', 'l', 'o', 'o', 'l'], ['e', 'l', 'w', 'r', 'd']),
         ["h", "e", "l", "l", "o", "w", "o", "r", "l", "d"]),
    ))
