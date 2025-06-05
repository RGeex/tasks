"""
У вас есть сборник прекрасных стихотворений. К сожалению, они не очень хорошо отформатированы.
Они все в одну строку, вот так:

Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.
Complex is better than complicated.

Вам нужно представить каждое предложение на новой строке, чтобы это выглядело следующим образом:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

Напишите функцию, которая принимает строку (как в примере с одной строкой) в качестве аргумента и
возвращает новую строку, отформатированную в несколько строк, причем каждое новое предложение при
выводе на печать начинается с новой строки.

Попробуйте решить эту задачу с помощью str.split() и str.join() . строковых методов

Каждое предложение будет заканчиваться точкой, и каждое новое предложение будет иметь один пробел
перед предыдущей точкой. Будьте осторожны с конечными пробелами в вашем решении.
"""
import typing
import unittest


def format_poem(poem: str) -> str:
    """
    Разделяет строку на строки по предложениям.
    """
    return poem.replace('. ', '.\n')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(format_poem, (
        ('Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.',
         'Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.'),
        ("Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules.",
         "Flat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules."),
        ("Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess.",
         "Although practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess."),
    ))
