"""
Заполните функцию/метод, чтобы он возвращал URL с чем -либо после якоря ( #) удаленный.
Примеры

"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"
"""
import typing
import unittest


def remove_url_anchor(url: str) -> str:
    """
    Удаляет из url все после якоря #.
    """
    return f'{url}_'[:url.find('#')]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(remove_url_anchor, (
        ("www.codewars.com#about", "www.codewars.com"),
        ("www.codewars.com/katas/?page=1#about", "www.codewars.com/katas/?page=1"),
        ("www.codewars.com/katas/", "www.codewars.com/katas/"),
    ))
