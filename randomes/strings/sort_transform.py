"""
Дан массив чисел, вернуть строку, состоящую из четырех частей:

    «слово» из четырех символов, составленное из символов, полученных из
    первых двух и последних двух чисел в массиве. Порядок должен быть таким,
    как читаемый слева направо (первый, второй, предпоследний, последний),

    то же, что и выше, после сортировки массива в порядке возрастания,

    то же самое, что и выше, после сортировки массива в порядке убывания,

    то же самое, что и выше, после преобразования массива в символы ASCII и сортировки по алфавиту.

Четыре части должны образовывать одну строку, каждая часть должна быть разделена дефисом ( -).

Пример формата решения: "asdf-tyui-ujng-wedg"
Примеры

[111, 112, 113, 114, 115, 113, 114, 110]  -->  "oprn-nors-sron-nors"
[66, 101, 55, 111, 113]                   -->  "Beoq-7Boq-qoB7-7Boq"
[99, 98, 97, 96, 81, 82, 82]              -->  "cbRR-QRbc-cbRQ-QRbc"
"""
import typing
import unittest


def sort_transform(arr: list[int]) -> str:
    """
    Создает строку из заданного списка чисел.
    """
    return '-'.join([''.join(map(chr, x[:2] + x[-2:])) for x in (arr, sorted(arr), sorted(arr, reverse=True), sorted(arr, key=chr))])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_transform, (
        ([111, 112, 113, 114, 115, 113, 114, 110], "oprn-nors-sron-nors"),
        ([51, 62, 73, 84, 95, 100, 99, 126], "3>c~-3>d~-~d>3-3>d~"),
        ([66, 101, 55, 111, 113], "Beoq-7Boq-qoB7-7Boq"),
        ([78, 117, 110, 99, 104, 117, 107, 115, 120, 121, 125], "Nuy}-Ncy}-}ycN-Ncy}"),
        ([101, 48, 75, 105, 99, 107, 121, 122, 124], "e0z|-0Kz|-|zK0-0Kz|"),
        ([80, 117, 115, 104, 65, 85, 112, 115, 66, 76, 62], "PuL>->Asu-usA>->Asu"),
        ([91, 100, 111, 121, 51, 62, 81, 92, 63], "[d\\?-3>oy-yo>3-3>oy"),
        ([78, 93, 92, 98, 108, 119, 116, 100, 85, 80], "N]UP-NPtw-wtPN-NPtw"),
        ([111, 121, 122, 124, 125, 126, 117, 118, 119, 121, 122, 73], "oyzI-Io}~-~}oI-Io}~"),
        ([82, 98, 72, 71, 71, 72, 62, 67, 68, 115, 117, 112, 122, 121, 93], "Rby]->Cyz-zyC>->Cyz"),
        ([99, 98, 97, 96, 81, 82, 82], "cbRR-QRbc-cbRQ-QRbc"),
        ([66, 99, 88, 122, 123, 110], "Bc{n-BXz{-{zXB-BXz{"),
        ([66, 87, 98, 59, 57, 50, 51, 52], "BW34-23Wb-bW32-23Wb"),
    ))
