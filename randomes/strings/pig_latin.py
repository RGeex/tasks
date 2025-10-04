"""
Задача:

Создайте функцию, которая преобразует слово в «свинью латынь». Правила «свиной латыни» следующие:
Если слово состоит более чем из 3 букв:
  1. Возьмите первую букву слова и переместите ее в конец.
  2. Добавьте -ay к слову.
В противном случае оставьте слово в покое.
Пример: hello= ellohay
"""
import typing
import unittest


def pig_latin(word):
    """
    Изменяет слово в свинолатынь.
    """
    return f'{word[1:]}{word[0]}ay' if len(word) > 3 else word


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(pig_latin, (
        ('hello', 'ellohay'),
        ('hi', 'hi'),
    ))
