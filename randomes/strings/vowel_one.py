"""
гласный

Напишите функцию, которая принимает строку и выводит струны из 1 и 0, где гласные становятся 1, а неволс становится 0.

Все не-Vowels, включая не альфа-символы (пространства, запятые и т. Д.) Должны быть включены.

Примеры:

vowelOne "abceios" -- "1001110"

vowelOne "aeiou, abc" -- "1111100100"
"""
import typing
import unittest


def vowel_one(st: str) -> str:
    """
    Заменяет гласные на 1, остальные на 0.
    """
    return ''.join('01'[x in 'aeiou'] for x in st.lower())


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(vowel_one, (
        ("vowelOne", "01010101"),
        ("123, arou", "000001011"),
        ("Codewars", "01010100"),
        ("Python", "000010"),
    ))
