"""
Создайте функцию, которая принимает массив имен и возвращает массив из каждого имени,
где первая буква — заглавная, а остальные — строчные.
Примеры

["jo", "nelson", "jurie"] -->  ["Jo", "Nelson", "Jurie"]
["KARLY", "DANIEL", "KELSEY"] --> ["Karly", "Daniel", "Kelsey"]


"""
import typing
import unittest


def cap_me(arr: list[str]) -> list[str]:
    """
    Преобразует список слов, в списк словк с заглавных первых букв.
    """
    return list(map(str.title, arr))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(cap_me, (
        [
            ["jo", "nelson", "jurie"],
            ["Jo", "Nelson", "Jurie"]
        ],
        [
            ["OZZA", "ARRA", "AZZA"],
            ["Ozza", "Arra", "Azza"]
        ],
        [
            ["Ror", "NOR", "xor"],
            ["Ror", "Nor", "Xor"]
        ],
        [
            [],
            []
        ],
        [
            ["", "", ""],
            ["", "", ""]
        ]
    ))
