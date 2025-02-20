"""
Учитывая два слова и букву, верните одно слово, которое представляет собой комбинацию обоих слов, объединенных в точке, где данная буква сначала появляется в каждом словом. Возвращенное слово должно иметь начало первого слова и окончания второго, с разделительной буквой посередине. Вы можете предположить, что оба слова будут содержать разделительную букву.
Примеры

("hello", "world", "l")       ==>  "held"
("coding", "anywhere", "n")   ==>  "codinywhere"
("jason", "samson", "s")      ==>  "jasamson"
("wonderful", "people", "e")  ==>  "wondeople"
"""
import typing
import unittest


def string_merge(st1: str, st2: str, letter: str) -> str:
    """
    Объединяет 2 заданных слова через указанную букву в этих словах.
    """
    return st1[:st1.find(letter)] + st2[st2.find(letter):]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(string_merge, (
        (("hello", "world", "l"), "held"),
        (("coding", "anywhere", "n"), "codinywhere"),
        (("jason", "samson", "s"), "jasamson"),
        (("wonderful", "people", "e"), "wondeople"),
        (("person","here", "e"), "pere"),
        (("apowiejfoiajsf","iwahfeijouh", "j"), "apowiejouh"),
        (("abcdefxxxyzz","abcxxxyyyxyzz", "x"), "abcdefxxxyyyxyzz"),
    ))
