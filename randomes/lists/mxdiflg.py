"""
Вам даны два массива. a1 и a2из строк. Каждая строка состоит из букв из a к z.
Позволять xпусть будет любая строка из первого массива и yпусть будет любой строкой из второго массива.

Find max(abs(length(x) − length(y)))

Если a1и/или a2пустые возвраты -1на каждом языке за исключением Haskell (F#), где вы вернёте Nothing (Никто).
Пример:

a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13

Примечание Bash:

    Входные данные: 2 строки с подстроками, разделёнными символом ,
    Вывод: число в виде строки
"""
import unittest
from typing import Any, Callable, List, Tuple


def mxdiflg(a1: List[str], a2: List[str]) -> int:
    """
    Определяет максимальную разницу между длиной строк списков.
    """
    return max([abs(len(x) - len(y)) for x in a1 for y in a2], default=-1)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(mxdiflg, (
        ((["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"], ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]), 13),
        ((["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], ["bbbaaayddqbbrrrv"]), 10),
        (([], ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]), -1) ,
    ))

