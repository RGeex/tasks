"""
Числа ложбана

Счет на ложбане , искусственном языке, разработанном за последние сорок лет,
проще, чем на большинстве Языки. Цифры из zero к nine являются:

1 pa 4 vo 7 ze
2 re 5 mu 8 bi 0 no
3 ci 6 xa 9 so

Более крупные числа получаются путём склеивания цифр. Например,
123 является pareci.

Напишите программу, которая считывает строку на ложбане
(представляющую число, меньшее или равное 1,000,000) и выводит его в числах.
Пример:

renonore  # Lojban string
2002  # Number

Ввод/вывод

    [input]строка, представляющая число в ложбане pareci
    Ограничения: число ложбанов ≤ 1 000 000
    [output]целое число, представляющее число Ложбана 123

Источник: Британская олимпиада по информатике 2002 г.

"""
import typing
import unittest


def convert_lojban(st: str) -> int:
    """
    Переводист с языка lojbon в число.
    """
    return int(''.join(str('no pa re ci vo mu xa ze bi so'.split().index(st[i * 2: i * 2 + 2])) for i in range(len(st) // 2)))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(convert_lojban, (
        ("pareci", 123),
        ("renonore", 2002),
    ))
