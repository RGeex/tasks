"""
Учитывая строку, переверните каждый символ в код символа ASCII и объедините их, чтобы создать номер - давайте назовем этот номер total1:

'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667

Затем замените любую частоту числа 7 с номером 1и назовите этот номер «Total2»:

total1 = 656667
              ^
total2 = 656661
              ^

Затем верните разницу между суммой цифр в total1 и total2:

  (6 + 5 + 6 + 6 + 6 + 7)
- (6 + 5 + 6 + 6 + 6 + 1)
-------------------------
                       6
"""
import typing
import unittest


def calc(st: str) -> int:
    """
    Поиск разницы суммы цифр с произведенной заменой от оригинала.
    """
    return 6 * sum(str(ord(x)).count('7') for x in st)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(calc, (
        ('abcdef', 6),
        ('ifkhchlhfd', 6) ,
        ('aaaaaddddr', 30) ,
        ('jfmgklf8hglbe', 6),
        ('jaam', 12),
    ))
