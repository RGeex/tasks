"""
При наличии строки все гласные пишутся с заглавной буквы.

Например:

Input : "Hello World!"

Output : "HEllO WOrld!"

Примечание: Y не является гласной в этой ката.

"""
import typing
import unittest


def swap(st: str) -> str:
    """
    Заменяет строчные гласные на заглавные.
    """
    return st.translate(str.maketrans('aeiou', 'AEIOU'))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(swap, (
        ("HelloWorld!", "HEllOWOrld!"),
        ("Sunday", "SUndAy"),
        ("Codewars","COdEwArs"),
        ("Monday", "MOndAy"),
        ("Friday", "FrIdAy"),
        ("abracadabra", "AbrAcAdAbrA"),
    ))
