"""
Напишите функцию, которая выводит позиции совпадающих пар скобок. На выходе
должен быть словарь с ключами позиций открытых скобок '(' и значениями
соответствующих позиций закрывающих скобок ')'.

Например: input = "(first)and( Second)" должен возвращать {0:6, 10:17}.

Если скобки не могут быть объединены в пары или порядок неверен
(например, ')('), верните False. В этом ката нас интересует только
положение круглых скобок «()», другие типы скобок следует игнорировать.
"""
import typing
import unittest


def bracket_pairs(s: str) -> dict | bool:
    """
    На основе переданной строки создает словарь, где
    ключем является открывающая скобка, значением закрывающая.
    Если у скобок нет пары или неварный порядок - False.
    """
    res, tmp, x = {}, {}, 0
    for i, w in enumerate(s):
        if w == '(':
            x += 1
            tmp[x] = i
        if w == ')':
            res[tmp.get(x)] = i
            x += -1
        if i == len(s) - 1 and x or x < 0:
            return False
    return res


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val)
             for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(
        type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(bracket_pairs, (
        ("len(list)", {3: 8}),
        ("string", {}),
        ("", {}),
        ("def f(x", False),
        (")(", False),
        ("(a(b)c()d)", {0: 9, 2: 4, 6: 7}),
        ("f(x[0])", {1: 6}),
    ))
