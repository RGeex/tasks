"""
Ваша задача — написать программу, которая принимает предложение и возвращает строку,
показывающую уникальное положение каждого слова в предложении. Если слово встречается
в предложении более одного раза, строка должна вернуть позицию первого вхождения слова.

Уникальная позиция в данном случае означает позицию слова без учета повторяющихся слов.
Необходимо учитывать написание слов с заглавной буквы: «ПЧЕЛА» следует считать тем же,
что и «пчела». В предложениях знаки препинания отсутствуют.
Пример

"man hello man"

становится

"010"
Пример

"THE ONE BUMBLE BEE one bumble the bee"

становится

"01231203"
Пример

"Ask not what your COUNTRY can do for you ASK WHAT YOU CAN DO FOR YOUR country"

становится

"01234567802856734"
"""
import unittest
from typing import Any, Callable, Tuple


def compress(sentence: str) -> str:
    """
    Определяет индекс слов в строке, не учитывая повоторяющиеся и регистр.
    """
    lst = sentence.lower().split()
    return ''.join([str(sorted(set(lst), key=lst.index).index(x)) for x in lst])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(compress, (
        ("The bumble bee", "012"),
        ("SILLY LITTLE BOYS silly little boys", "012012"),
        ("Ask not what your COUNTRY can do for you ASK WHAT YOU CAN DO FOR YOUR country", "01234567802856734"),
        ("The number 0 is such a strange number Strangely it has zero meaning", "012345617891011"),
    ))

