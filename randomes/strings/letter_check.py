"""
Напишите функцию, которая проверяет, присутствуют ли все буквы во второй строке хотя бы один раз в
первой, независимо от того, сколько раз они появляются:

["ab", "aaa"]    =>  true
["trances", "nectar"]    =>  true
["compadres", "DRAPES"]  =>  true
["parses", "parsecs"]    =>  false

Функция не должна быть чувствительна к регистру, как указано в примере № 2. Примечание: обе строки
представлены как один аргумент в виде массива.
"""
import typing
import unittest
from operator import sub


def letter_check(arr: list[str]) -> bool:
    """
    Проверяет встречаются ли все буквы второй строки в первой.
    """
    return not sub(*[set(x.lower()) for x in arr[::-1]])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(letter_check, (
        (["abcd", "aaa"], True),
        (["trances", "nectar"], True),
        (["THE EYES", "they see"], True),
        (["assert", "staring"], False),
        (["arches", "later"], False),
        (["dale", "caller"], False),
        (["parses", "parsecs"], False),
        (["replays", "adam"], False),
        (["mastering", "streaming"], True),
        (["drapes", "compadres"], False),
        (["deltas", "slated"], True),
        (["deltas", ""], True),
        (["", "slated"], False),
    ))
