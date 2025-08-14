"""
Дана строка, содержащая список целых чисел, разделенных запятыми.
Напишите функцию, которая принимает указанную строку и возвращает
новый массив/список, содержащий все целые числа, присутствующие в
строке, сохраняя порядок.

Обратите внимание, что может быть одна или несколько последовательных
запятых без цифр, например:

"-1,-2,,,,,,3,4,5,,6"

Например

"-1,-2,3,-4,-5"   --> [-1,-2,3,-4,-5]
"1,2,3,,,4,,5,,," --> [1,2,3,4,5]
",,,,,,,"         --> []

"""
import typing
import unittest


def string_to_int_list(st: str) -> list[int]:
    """
    Строку чисел разделенных запятыми, преобразует в список.
    """
    return list(map(int, st.replace(',', ' ').split()))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase( type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(string_to_int_list, (
        ("1,2,3,4,5", [1, 2, 3, 4, 5]),
        ("21,12,23,34,45", [21, 12, 23, 34, 45]),
        ("-1,-2,3,-4,-5", [-1, -2, 3, -4, -5]),
        ("1,2,3,,,4,,5,,,", [1, 2, 3, 4, 5]),
        (",,,,,1,2,3,,,4,,5,,,", [1, 2, 3, 4, 5]),
        ("", []),
        (",,,,,,,,", []),
    ))
