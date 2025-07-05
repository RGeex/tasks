"""
Напишите функцию, которая будет брать ключ X и помещать его в середину Y,
повторяя N раз.

Дополнительное испытание (не тестировалось): Вы можете выполнить это
задание менее чем за 70 символов без использования регулярных выражений.
Испытайте себя, чтобы сделать это. Это не будет лучшим вариантом,
но это сработает.

Правила:

Если X невозможно разместить в середине, верните X.

N всегда будет > 0.

Пример:

X = 'A';

Y = '*';

N = 10;

Y repeated N times = '**********';

X in the middle of Y repeated N times = '*****A*****';


"""
import typing
import unittest


def middle_me(N: int, X: str, Y: str):
    """
    Размещает X в центре строки из символов Y длиной N, если это возможно.
    """
    return X if N % 2 else X.join([N // 2 * Y] * 2)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(middle_me, (
        ((18, 'z', '#'), '#########z#########'),
        ((19, 'z', '#'), 'z'),
    ))
