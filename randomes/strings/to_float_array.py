"""
О, нет!

Некоторый действительно забавный веб -разработчик дал вам последовательность чисел из своего ответа API в качестве последовательности строк !

Вам нужно поднять весь массив в правильный тип.

Создайте функцию, которая принимает в качестве параметра последовательность чисел, представленную как строки, и выводит последовательность чисел.

т.е.: ["1", "2", "3"] к [1, 2, 3]

Обратите внимание, что вы также можете получать поплавки.
"""
import typing
import unittest


def to_float_array(arr: list[str]) -> list[int | float]:
    """
    Список строк конвертирует в int или float.
    """
    return list(map(eval, arr))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(to_float_array, (
        (["1.1", "2.2", "3.3"], [1.1, 2.2, 3.3]),
    ))
