"""
Проверьте, является ли это гласной буквой (a, e, i, o, u,) на n
Позиция в строке (первый аргумент). Не забывайте о заглавных буквах.

Несколько случаев:

{
checkVowel('cat', 1)  ->   true // 'a' is a vowel
checkVowel('cat', 0)  ->   false // 'c' is not a vowel
checkVowel('cat', 4)  ->   false // this position doesn't exist
}

P.S. Если n < 0, вернуть false

"""
import typing
import unittest


def check_vowel(strng: str, position: int) -> bool:
    """
    Проверяет, является ли указанная буква в слове гласной.
    """
    return position in range(len(strng)) and strng.lower()[position] in 'aeiou'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(check_vowel, (
        (('cat', 1), True),
        (('cat', 0), False),
        (('cat', 4), False)  ,
        (('Amanda', -2), False),
        (('Amanda', 0), True),
        (('Amanda', 2), True),
    ))
