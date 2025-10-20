"""
Выведите отладку на совершенно новый уровень:

Дана строка, удалите все ошибки .

Это означает, что вам необходимо удалить все вхождения слова «bug» из данной строки, если только слово не стоит во множественном числе («bugs»).

Например, если ввести «obugobugobuoobugsoo», следует вернуть «ooobuoobugsoo».

Другой пример: если задано «obbugugo», нужно вернуть «obugo».

Обратите внимание, что все символы будут строчными.

Приятного хлюпанья!

"""
import typing
import unittest
import re


def debug(s: str) -> str:
    """
    Устраняет ошибки в строке.
    """
    return re.sub(r'bugs?', lambda x: x.group(0).rstrip('bug'), s)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(debug, (
        ('obugobugobuoobugsoo', 'ooobuoobugsoo'),
        ('obbugugo', 'obugo'),
        ('bugs bunny', 'bugs bunny'),
        ('bugs buggy', 'bugs gy'),
    ))
