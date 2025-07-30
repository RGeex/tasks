"""
Ваша задача — написать обновление для лотерейного автомата.
Текущая версия выдаёт последовательность случайных букв и
целых чисел (передаваемых в функцию как строка).
Ваш код должен отфильтровывать все буквы и возвращать
уникальные целые числа в виде строки, в порядке их
появления. Если в строке нет целых чисел, верните "One more run!"
Примеры

"hPrBKWDH8yc6Lt5NQZWQ"  -->  "865"
"ynMAisVpHEqpqHBqTrwH"  -->  "One more run!"
"555"                   -->  "5"


"""
import typing
import unittest


def lottery(st: str) -> str:
    """
    Выбирает уникальные цифры из строки в порядке их появления.
    """
    return ''.join({x: x for x in st if x.isdigit()}) or 'One more run!'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(lottery, (
        ("wQ8Hy0y5m5oshQPeRCkG", "805"),
        ("ffaQtaRFKeGIIBIcSJtg", "One more run!"),
        ("555", "5"),
        ("HappyNewYear2020", "20"),
        ("20191224isXmas", "20194"),
        ("", "One more run!"),
    ))
