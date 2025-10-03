"""
Удобное слово — это слово, которое вы можете набирать, всегда чередуя руку,
которой печатаете (при условии, что вы печатаете с помощью клавиатуры QWERTY
и используете пальцы, как показано на рисунке ниже).

При этом завершите функцию, которая получает слово и возвращает trueесли это
удобное слово и false в противном случае.

Слово всегда будет строкой, состоящей только из букв ASCII из a к z.

Чтобы избежать проблем с доступностью изображений, вот списки букв для каждой
руки:

    Левый: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
    Верно: y, u, i, o, p, h, j, k, l, n, m

Примеры

"yams"  -->  true
"test"  -->  false
"""
import typing
import unittest


def comfortable_word(word: str) -> bool:
    """
    Проверяет, является ли слово удобным для написания.
    """
    return not next((1 for i, w in enumerate(word) if w in (x := ['qwertasdfgzxcvb', 'yuiophjklnm'])[::word[0] in x[1] or -1][i % 2]), 0)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(comfortable_word, (
        ('yams', True),
        ('test', False),
    ))
