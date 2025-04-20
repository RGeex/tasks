"""
Описание:

Удалите слова из предложения, если они содержат ровно один восклицательный знак.
Слова разделяются одним пробелом, без начальных/конечных пробелов.
Примеры

remove("Hi!") === ""
remove("Hi! Hi!") === ""
remove("Hi! Hi! Hi!") === ""
remove("Hi Hi! Hi!") === "Hi"
remove("Hi! !Hi Hi!") === ""
remove("Hi! Hi!! Hi!") === "Hi!!"
remove("Hi! !Hi! Hi!") === "!Hi!"
"""
import typing
import unittest


def remove(st: str) -> str:
    """
    Удаляет слово из строки, если в нем ровно 1 восклицательный знак.
    """
    return ' '.join(x for x in st.split() if x.count('!') != 1)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(remove, (
        ('Hi!', ''),
        ('Hi!!!', 'Hi!!!'),
        ('!Hi', ''),
        ('!Hi!', '!Hi!'),
        ('Hi! Hi!', ''),
        ('!!!Hi !!hi!!! !hi', '!!!Hi !!hi!!!'),
        ('!Hi! ! !Hi!', '!Hi! !Hi!'),
    ))
