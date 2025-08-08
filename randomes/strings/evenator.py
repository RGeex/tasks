"""
Г-н Э. Вен любит только слова четной длины. Пожалуйста, создайте переводчик,
чтобы ему не приходилось слышать эти надоедливые слова странной длины.
По какой-то причине он также ненавидит пунктуацию, ему нравится, чтобы
предложения были связными.

Ваш переводчик должен принять строку и вывести её, удалив все слова нечётной
длины, содержащие лишнюю букву (последнюю букву в слове). Также необходимо
удалить все знаки препинания (.,?!) и подчёркивания (_).

«Как мы здесь оказались? Мы идём?» переведено становится-> «Как мы здесь
оказались? Мы идём»
"""
import typing
import unittest
import re


def evenator(st: str) -> str:
    """
    Удаляет лишние символы из строки, а так же делает слова с нечетным кол-вом символов, четным.
    """
    return ' '.join(x + ['', x[-1]][len(x) % 2] for x in re.sub(r'[\.\,\?\!\_]', '', st).split())


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(evenator, (
        ('', ''),
        ('I got a hole in 1!', 'II gott aa hole in 11'),
        ('underscore is not considered a word..in this case,', 'underscore is nott considered aa wordin this case'),
    ))
