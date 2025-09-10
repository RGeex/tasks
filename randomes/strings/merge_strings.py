"""
В этом задании вам нужно написать функцию, которая объединяет две строки.
Это происходит путём объединения конца первой строки с началом второй,
если они полностью совпадают.

"abcde" + "cdefgh" => "abcdefgh"
"abaab" + "aabab" => "abaabab"
"abc" + "def" => "abcdef"
"abc" + "abc" => "abc"

ПРИМЕЧАНИЕ: Алгоритм всегда должен использовать максимально возможное
перекрытие.

"abaabaab" + "aabaabab" would be "abaabaabab" and not "abaabaabaabab"
"""
import typing
import unittest


def merge_strings(first: str, second: str) -> str:
    """
    Слияние строк с максимально возможным перекрытием.
    """
    return first[:next((i for i in range(len(first)) if second.startswith(first[i:])), len(first))] + second


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(merge_strings, (
        (('abcde', 'cdefgh'), 'abcdefgh'),
        (('abaab', 'aabab'), 'abaabab'),
    ))
