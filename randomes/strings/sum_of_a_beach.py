"""
Пляжи заполнены песком, водой, рыбой и солнцем. Имея строку,
посчитайте, сколько раз слова "Sand", "Water", "Fish", и
"Sun"появляются без перекрытия (независимо от регистра).
Примеры

"WAtErSlIde"                    ==>  1
"GolDeNSanDyWateRyBeaChSuNN"    ==>  3
"gOfIshsunesunFiSh"             ==>  4
"cItYTowNcARShoW"               ==>  0
"""
import re
import typing
import unittest


def sum_of_a_beach(st: str) -> int:
    """
    Подсчитывает кол-во вхождений слов в строке без перекрытия.
    """
    return len(re.findall(r'sand|water|fish|sun', st.lower()))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sum_of_a_beach, (
        ("SanD", 1),
        ("sunshine", 1),
        ("sunsunsunsun", 4),
        ("123FISH321", 1),
    ))
