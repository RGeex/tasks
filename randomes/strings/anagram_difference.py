"""
Учитывая два слова, сколько букв из них нужно удалить,
чтобы они стали анаграммами?
Пример
    
    Первое слово : c od e w ar s (буквы удалены 4)
    Второе слово : ha c k er r a nk (6 букв удалены)
    Результат: 10

Подсказки

    Слово является анаграммой другого слова, если в нем есть одинаковые буквы
    (обычно в разном порядке).
    Не беспокойтесь о случае. Все входные данные будут в нижнем регистре.
"""
import typing
import unittest
from collections import Counter


def anagram_difference(w1: str, w2: str) -> int:
    """
    Подсчитывает кол-во букв, убрав которые слова станут анаграммами.
    """
    return sum(map(len, (w1, w2))) - sum((Counter(w1) & Counter(w2)).values()) * 2


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(anagram_difference, (
        (('', ''), 0),
        (('a', ''), 1),
        (('', 'a'), 1),
        (('ab', 'a'), 1),
        (('ab', 'ba'), 0),
        (('ab', 'cd'), 4),
        (('codewars', 'hackerrank'), 10)
    ))
