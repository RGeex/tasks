"""
Завершите функцию, которая принимает в качестве аргумента ненулевое целое число.

Если целое число делится на 3, вернуть строку "Java".

Если целое число делится на 3 и делится на 4, вернуть строку "Coffee"

Если одно из приведенных выше условий верно и целое число четное, добавьте "Script"до конца строки.

Если ни одно из условий не выполняется, вернуть строку "mocha_missing!"
Примеры

1   -->  "mocha_missing!"
3   -->  "Java"
6   -->  "JavaScript"
12  -->  "CoffeeScript"


"""
import typing
import unittest


def caffeine_buzz(num: int) -> str:
    """
    Обрабатывает входящее число и в зависимости от результатта выдает строку.
    """
    return {3: 'Java', 6: 'JavaScript', 12: 'CoffeeScript'}.get(next((n for n in (12, 6, 3) if not num % n), 0), 'mocha_missing!')
    


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(caffeine_buzz, (
        (1, "mocha_missing!"),
        (2, "mocha_missing!"),
        (3, "Java"),
        (4, "mocha_missing!"),
        (5, "mocha_missing!"),
        (6, "JavaScript"),
        (7, "mocha_missing!"),
        (8, "mocha_missing!"),
        (9, "Java"),
        (10, "mocha_missing!"),
        (11, "mocha_missing!"),
        (12, "CoffeeScript"),
    ))
