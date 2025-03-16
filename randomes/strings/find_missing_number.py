"""
Вы получаете несколько случайных элементов в виде строки, разделенной пробелом. Проверьте, являются ли элементы частью возрастающей последовательности целых чисел, начиная с 1, с шагом 1 (например, 1, 2, 3, 4).

Возвращаться:

    0если элементы могут образовать такую ​​последовательность, и ни одно число не пропущено («не нарушено», например) "1 2 4 3")
    1если во входных данных есть какие-либо нечисловые элементы («недопустимые», например "1 2 a")
    nесли элементы являются частью такой последовательности, но некоторые числа отсутствуют, и nявляется самым низким из них («сломанный», например) "1 2 4" или "1 5")

Примеры

"1 2 3 4"  ==>  return 0, because the sequence is complete

"1 2 4 3"  ==>  return 0, because the sequence is complete (order doesn't matter)

"2 1 3 a"  ==>  return 1, because it contains a non numerical character

"1 3 2 5"  ==>  return 4, because 4 is missing from the sequence

"1 5"      ==>  return 2, because the sequence is missing 2, 3, 4 and 2 is the lowest


"""
import re
import typing
import unittest


def find_missing_number(sequence: str) -> int:
    """
    Проверяет упущения в последовательности.
    """
    return 1 if re.search(r'[^\d ]', sequence) else next((i for i, n in enumerate(sorted(map(int, sequence.split())), 1) if i != n), 0)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_missing_number, (
        ("1 2 3 5", 4),
        ("1 5", 2),
        ("", 0),
        ("1 2 3 4 5", 0),
        ("2 3 4 5", 1),
        ("2 6 4 5 3", 1),
        ("_______", 1),
        ("2 1 4 3 a", 1),
    ))
