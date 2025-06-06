"""
Почему мы должны остановиться только на 50 оттенках серого? Давайте посмотрим,
до скольких мы сможем дойти.

Напишите функцию, которая принимает число n в качестве параметра и возвращает массив,
содержащий n оттенков серого в шестнадцатеричном коде ( #aaaaaaнапример).
Массив должен быть отсортирован в порядке возрастания, начиная с '#010101', '#020202'и т. д.
(используя строчные буквы).

Примеры:

n =  1:    ["#010101"]
n = 10:    ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606", "#070707", "#080808", "#090909", "#0a0a0a"]

Напоминаем, что серый цвет состоит из одинакового количества красного, зеленого и синего:
#010101, #aeaeae, или #555555.

Черный: #000000и белый: #ffffffне являются принятыми значениями.

Когда nотрицательно, просто верните пустой массив. Если nбольше 254,
просто верните массив из 254 элементов.

Веселиться!

"""
import typing
import unittest


def shades_of_grey(num: int) -> list[str]:
    """
    Возвращает оттенки серого по заданному кол-ву. не > 255.
    """
    return ['#' + f'{x + 1:0>2x}' * 3 for x in range(min(254, num))]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(shades_of_grey, (
        (-2, []),
        (-1, []),
        (0, []),
        (1, ["#010101"]),
        (2, ["#010101", "#020202"]),
        (3, ["#010101","#020202", "#030303"]),
        (4, ["#010101", "#020202", "#030303", "#040404"]),
        (5, ["#010101", "#020202", "#030303", "#040404", "#050505"]),
        (6, ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606"]),
        (7, ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606", "#070707"]),
        (8, ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606", "#070707", "#080808"]),
        (9, ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606", "#070707", "#080808", "#090909"]),
    ))
