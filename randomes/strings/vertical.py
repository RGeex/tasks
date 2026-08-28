"""
Слова внизу страницы
Обычно мы читаем список слов слева направо :

hi world yo
Ваша задача — распечатать их сверху вниз .

Каждое слово образует столбец шириной ровно в один символ, идущий вниз по странице.
Столбцы сохраняют свой первоначальный порядок, располагаются рядом друг с другом и разделены одним пробелом.

Пример
vertical(["hi", "world", "yo"])
возвращает строку

h w y
i o o
  r
  l
  d
hiи yoзаканчиваются после двух символов, поэтому их столбцы просто становятся пустыми — но world
процесс продолжается, и они должны оставаться в том же столбце, с которого начали.

Правила
Возвращает одну строку . Строки объединяются с помощью оператора ` .`"\n" .
В конце строки нет символа новой строки.
Количество строк равно длине самого длинного слова.
Если в слове закончились символы, соответствующая ячейка становится пустой.
Столбцы справа должны оставаться выровненными.
Все строки обрезаны по правому краю.
Пустое слово ""по-прежнему владеет колонкой.
Возвращается пустой список "".
Гарантии
Входные данные представляют собой список строк.
Ни одно слово не содержит пробела.
Слова состоят из букв (в любом регистре) и цифр.
"""
import unittest
from typing import Any, Callable, List, Tuple
from itertools import zip_longest as zl


def vertical(words: List[str]) -> str:
    """
    Переводит предложение из горизонтального в вертикальное.
    """
    return "\n".join([" ".join(x).rstrip() for x in zl(*words, fillvalue=" ")])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(vertical, (
        (["cat", "dog"], "c d\na o\nt g"),
        (["hi", "world", "yo"], "h w y\ni o o\n  r\n  l\n  d",),
        (["solo"], "s\no\nl\no"),
        (["a", "b", "c"], "a b c"),
        (["", "abc"], "  a\n  b\n  c"),
        ([], ""),
    ))
