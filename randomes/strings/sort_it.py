"""
Напишите функцию, принимающую два параметра: i) строку (содержащую список слов)
и ii) целое число (n). Функция должна упорядочить список по алфавиту, начиная
с n-й буквы каждого слова.

Буквы следует сравнивать без учёта регистра. Если обе буквы одинаковые,
расположите их в обычном (лексикографическом) порядке, также без учёта регистра.

Пример:

sort_it('bid, zag', 2) #=> 'zag, bid'

Длина всех слов в списке будет >= n. Формат будет "x, x, x". В Haskell вы
получите список Strings вместо этого.
"""
import typing
import unittest


def sort_it(words: str, n: int) -> str:
    """
    Сортирует слова по алфавиту начиная с N буквы каждого слова.
    """
    return ', '.join(sorted(words.split(', '), key=lambda x: x[n - 1]))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_it, (
        (('bill, bell, ball, bull', 2),'ball, bell, bill, bull'),
        (('words, wordz, wordy, wording', 5), 'wording, words, wordy, wordz'),
        (('he, hi, ha, ho', 2), 'ha, he, hi, ho'),
        (('zephyr, yellow, wax, a, ba, cat', 1), 'a, ba, cat, wax, yellow, zephyr'),
        (('hello, how, are, you, doing, today', 3), 'today, are, doing, hello, you, how'),
    ))
