"""
Дезоксирибонуклеиновая кислота (ДНК) — химическое вещество, содержащееся в ядре клеток и несущее
«инструкции» по развитию и функционированию живых организмов.

Если вы хотите узнать больше: http://en.wikipedia.org/wiki/DNA

В цепочках ДНК символы «A» и «T» являются дополнениями друг друга, как «C» и «G». Ваша функция
получает одну сторону ДНК (строку, за исключением Haskell); вам нужно вернуть другую,
комплементарную сторону. Цепь ДНК никогда не бывает пустой или ДНК вообще нет
(опять же, за исключением Haskell).

Больше подобных упражнений можно найти здесь: http://rosalind.info/problems/list-view/ (источник)

Пример: ( вход -> выход )

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
"""
import typing
import unittest


def DNA_strand(st: str) -> str:
    """
    Из заданной строки ДНК, возвращает комплементарную сторону.
    """
    return st.translate(str.maketrans('ATCG', 'TAGC'))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(DNA_strand, (
        ("AAAA", "TTTT"),
        ("ATTGC", "TAACG"),
        ("GTAT", "CATA"),
    ))
