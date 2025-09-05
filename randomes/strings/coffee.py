"""
Описание: Джон очень любит кофе. Ранее он написал несколько сообщений, но переживает,
что они не передали его энтузиазма, поэтому решил отправить их ещё раз, написав слово
«кофе» заглавными буквами:

КОФЕ

Задача: Напишите функцию «кофе», которая принимает строку в качестве параметра и
возвращает эту строку с каждым вхождением слова «кофе» заглавными буквами.

Ввод: строка. Слово «кофе» может встречаться несколько раз. Оно может содержать
заглавные буквы или быть полностью заглавным. В строке также могут присутствовать
знаки препинания. Оно не будет частью другого слова, например, «Кофебургер»,
которое и так не является словом.

Вывод: строка со всеми вхождениями слова «кофе» заглавными буквами:

Примеры:

Ввод: «Я выпил сегодня утром всего две чашки кофе? Мне нужно больше». Вывод:
«Я выпил сегодня утром всего две чашки КОФЕ? Мне нужно больше».

Ввод: «Кофе! Купи мне КОФЕ!» Вывод: «КОФЕ! Купи мне КОФЕ!»

Удачи!
"""
import typing
import unittest
import re


def coffee(sentence: str) -> str:
    """
    Изменяет слово coffee на капс.
    """
    return re.sub(r'(?i)coffee', 'COFFEE', sentence)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(coffee, (
        ("I'm having trouble staying focussed.  Let's get some coffee.", "I'm having trouble staying focussed.  Let's get some COFFEE."),
    ))
