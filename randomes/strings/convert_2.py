"""
История:

Пришельцы с планеты Кеплер-27b иммигрировали на Землю! Они выучили английский,
ходят в наши магазины, едят нашу еду, одеваются как мы, ездят на Uber, пользуются
Google и так далее. Однако говорят они по-английски немного иначе. Можете ли вы
написать программу, которая переводит наш английский на их инопланетный?
Задача:

Напишите функцию, которая получает строку в нижнем регистре и преобразует её из
нашего английского в инопланетный английский. Они, как правило, говорят на букву
a нравиться o и oкак u.

"hello" ---> "hellu"
"codewars" ---> "cudewors"
"""
import typing
import unittest


def convert(st: str) -> str:
    """
    Заменяет буквы в слове по шаблону.
    """
    return st.translate(str.maketrans('ao', 'ou'))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(convert, (
        ('codewars', 'cudewors'),
        ('hello', 'hellu'),
    ))
