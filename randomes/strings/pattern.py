"""
Задача:

Вам нужно написать функцию patternкоторый возвращает следующий шаблон
(см. шаблон и примеры) вплоть до nколичество строк.

    Примечание: Returningузор не такой как Printingузор.

Правила/Примечание:

    Если n < 1то он должен вернуть "", т.е. пустую строку.
    Есть no whitespacesв узоре.

pattern:

1
22
333
....
.....
nnnnnn

Примеры:

    pattern(5):

    1
    22
    333
    4444
    55555

    pattern(11):

    1
    22
    333
    4444
    55555
    666666
    7777777
    88888888
    999999999
    10101010101010101010
    1111111111111111111111

    Подсказка: используйте \n в строке для перехода на следующую строку.

"""
import typing
import unittest


def pattern(n: int) -> str:
    """
    Создает строку по заданному шаблону.
    """
    return '\n'.join(str(x) * x for x in range(1, n + 1))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(pattern, (
        (1, "1"),
        (2, "1\n22"),
        (5, "1\n22\n333\n4444\n55555"),
        (0, ""),
        (-25, ""),
    ))
