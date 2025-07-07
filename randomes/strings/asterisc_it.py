"""
Задача

Вам дана функция, которая должна вставить звездочку ( *) между каждой парой четных цифр в
заданном вводе и вернуть его как строку. Если ввод является последовательностью, сначала
соедините элементы как строку.
Вход

Входными данными могут быть целое число, строка цифр или последовательность, содержащая
только целые числа.
Выход

Верните строку.
Примеры

5312708     -->  "531270*8"
"0000"      -->  "0*0*0*0"
[1, 4, 64]  -->  "14*6*4"

"""
import typing
import unittest


def asterisc_it(n: int | str | list[int]) -> str:
    """
    Ставит между четными цифрами знак *.
    """
    res, num, prew = '', ''.join(map(str, n) if isinstance(n, list) else str(n)), None
    for x in num:
        res, prew = res + ['*', ''][not ((curr := not int(x) % 2) and prew)] + x, curr
    return res


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(asterisc_it, (
        (5312708, '531270*8'),
        (9682135, '96*8*2135'),
        (2222, '2*2*2*2'),
        (1111, '1111'),
        (9999, '9999'),
        ('0000', '0*0*0*0'),
        (8, '8'),
        (2, '2'),
        (0, '0'),
        ([1, 4, 64, 68, 67, 23, 1], '14*6*4*6*8*67231'),
    ))
