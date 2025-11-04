"""
Наступила пятница 13-е, и Джейсон готов к своей первой серии убийств!

Создайте функцию killcount, которая принимает два аргумента: массив пар массивов (имя и интеллект консультанта - ["Chad", 2]) и целое число, представляющее интеллект Джейсона.

Рубин, Питон, Кристалл:

counselors = [["Chad", 2], ["Tommy", 9]]
jason = 7

Ваша функция должна возвращать массив имен всех советников, которых Джейсон может перехитрить и убить.

Счастливой пятницы 13-го!
"""
import typing
import unittest


def kill_count(counselors: list[list[str, int]], jason: int) -> list[str]:
    """
    Определяет список имен не умнее Джейсона.
    """
    return [name for name, iq in counselors if iq < jason]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(kill_count, (
        (([["Tiffany", 4],["Jack", 6],["Megan", 7],["Tyler", 3]], 6), ["Tiffany", "Tyler"]),
        (([["Tiffany", 4],["Jack", 6],["Megan", 7],["Tyler", 3]], 8), ["Tiffany", "Jack", "Megan", "Tyler"]),
        (([["Tiffany", 4],["Jack", 6],["Megan", 7],["Tyler", 3]], 3), []),
    ))
