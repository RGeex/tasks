"""
В этом ката вы создадите функцию, которая преобразует строку с буквами и
цифрами в инверсию этой строки (в отношении буквенных и цифровых символов).
Так, например, письмо a станет 1 и номер 1 станет a; z станет 26 и 26 станет z.

Пример: "a25bz" стал бы "1y226"

Числа, обозначающие буквы ( n <= 26) всегда будет разделяться буквами для всех
тестовых случаев:

    "a26b" можно проверить, но не "a262b"
    "cjw9k" можно проверить, но не "cjw99k"

Список с названием alphabet для вас предварительно загружено: ['a', 'b', 'c', ...]
"""
import re
import typing
import unittest


def AlphaNum_NumAlpha(s: str) -> str:
    """
    Переводит числа в буквы, а буквы в числа.
    """
    return ''.join([str(ord(x) - 96) if x.isalpha() else chr(int(x) + 96) for x in re.split(r'(\d*)', s) if x])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(AlphaNum_NumAlpha, (
        ('25abcd26', 'y1234z'),
        ('18zyz14', 'r262526n'),
        ('a1b2c3d4', '1a2b3c4d'),
        ('5a8p17', 'e1h16q'),
    ))
