"""
Учитывают 2 струны, a и b, вернуть строку формы: shorter+reverse(longer)+shorter.

Другими словами, самая короткая строка должна быть помещена в качестве префикса и в
качестве суффикса самого длинного.

Строки a и b Может быть пустым, но не нулевым (в струнах C# также может быть нулевым.
Обращаться с ними так, как будто они пусты.).
Если a и b иметь такую ​​же лечение длиной a Как более длительное произведение b+reverse(a)+b
"""
import typing
import unittest


def shorter_reverse_longer(a: str, b: str) -> str:
    """
    Создание строки по заданному шаблону из двух строк.
    """
    a, b = sorted((b, a), key=len)
    return a + b[::-1] + a


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(shorter_reverse_longer, (
        (("first", "abcde"), "abcdetsrifabcde"),
        (("hello", "bau"), "bauollehbau"),
        (("abcde", "fghi"), "fghiedcbafghi"),
    ))
