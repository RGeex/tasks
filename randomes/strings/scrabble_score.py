"""
Напишите программу, которая по заданному слову вычисляет счет в игре «Скрабл» для этого слова.
Значения букв

Вам понадобится следующее:

Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10

Будет предустановленный словарь. dict_scoresсо всеми этими значениями: dict_scores["E"] == 1
Примеры

"cabbage" --> 14

«капуста» должна быть оценена в 14 баллов:

    3 балла за C
    1 балл за А, дважды
    3 очка за B, дважды
    2 балла за G
    1 балл за E

Итого:

3 + 2*1 + 2*3 + 2 + 1= 3 + 2 + 6 + 3= 14

Должна вернуться пустая строка 0. Строка может содержать пробелы и буквы (заглавные и строчные),
вам следует подсчитывать очки скрэббла только для букв в этой строке.

""           --> 0
"STREET"    --> 6
"st re et"    --> 6
"ca bba g  e" --> 14
"""
import typing
import unittest


dict_scores = {
    'E': 1,
    'A': 1,
    'I': 1,
    'O': 1,
    'N': 1,
    'R': 1,
    'T': 1,
    'L': 1,
    'S': 1,
    'U': 1,
    'D': 2,
    'G': 2,
    'B': 3,
    'C': 3,
    'M': 3,
    'P': 3,
    'F': 4,
    'H': 4,
    'V': 4,
    'W': 4,
    'Y': 4,
    'K': 5,
    'J': 8,
    'X': 8,
    'Q': 10,
    'Z': 10,
}


def scrabble_score(st: str) -> int:
    """
    По дсчитывает счет для заданного слова.
    """
    return sum(dict_scores.get(x, 0) for x in st.upper())


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(scrabble_score, (
        ("", 0),
        ('a', 1),
        ("street", 6),
        ("STREET", 6),
        (' a', 1),
        ("st re et", 6),
        ('f', 4),
        ("quirky", 22),
        ("MULTIBILLIONAIRE", 20),
        ("alacrity", 13),
    ))
