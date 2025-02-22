"""
Учитывая строку пространства, разделенные словами, верните самое длинное слово.
Если есть несколько самых длинных слов, верните самое правое самое длинное слово.
Примеры

"red white blue"  =>  "white"
"red blue gold"   =>  "gold"
"""
import typing
import unittest


def longest_word(st: str) -> str:
    """
    Поиск в строке самого длинного слова с конца строки.
    """
    return max(enumerate(st.split()), key=lambda x: (len(x[1]), x[0]))[1]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(longest_word, (
        ('a b c d each', "each" ),
        ('each step', "step" ),
        ('forward each step going', "forward" ),
        ('brings each step going', "brings" ),
        ('each step forward brings opportunity', "opportunity" ),
    ))
