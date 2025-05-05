"""
Напишите функцию, которая удаляет все одиночные 9что находится между 7с.

"79712312" --> "7712312"
"79797"    --> "777"


"""
import typing
import unittest


def seven_ate9(st: str) -> str:
    """
    Удаляет из строки 9 стоящую между 7.
    """
    return st.replace('797', '77').replace('797', '77')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(seven_ate9, (
        ('165561786121789797', '16556178612178977'),
        ('797', '77'),
        ('7979797', '7777'),
    ))
