"""
Задача

Дана строка, верните количество содержащихся в ней одиночных букв.

Письмо чувствует себя одиноким, когда:

    Оно встречается ровно один раз во всей строке.
    В строке отсутствуют оба соседних элемента, расположенных в алфавитном порядке.

Соседними буквами в алфавите являются предыдущая и следующая буквы алфавита.

    dимеет соседей в алфавитном порядке c и e.
    aимеет только одного возможного соседа: b.
    zимеет только одного возможного соседа: y.
    Алфавит не является циклическим , поэтому zне является соседом a, и aне является соседом z.

Например:

    d не одиноко, если c или e Также встречается где-то в тексте.
    mодиноко, если mпоявляется один раз, и оба l и nотсутствуют.

Правила

    Регистр букв не имеет значения.
    Игнорировать все символы, кроме букв.
    Работайте только с английскими буквами. a-z.

Примеры

    Вход: "ad"-> Вывод: 2
    Вход: "abc"-> Вывод: 0
    Вход: "Hello, World!"-> Вывод: 3
    Вход: "A-dA"-> Вывод: 1
    Вход: "zz"-> Вывод: 0
"""
import unittest
from typing import Any, Callable, Tuple


def count_lonely_letters(text: str) -> int:
    """
    Определяет кол-во одиночных букв в строке.
    """
    lst = [0] + sorted({ord(x) for x in text.lower() if x.isalpha()}) + [0]
    return sum([b - a != 1, 1][not a] and [c - b != 1, 1][not c] for a, b, c in zip(lst, lst[1:], lst[2:]) if text.lower().count(chr(b)) == 1)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(count_lonely_letters, (
        ("ad", 2),
        ("abc", 0),
        ("Hello, World!", 3),
        ("A-dA", 1),
        ("zz", 0),
        ("", 0),
        ("123 !!!", 0),
        ("bdfhj", 5),
        ("a", 1),
        ("z", 1),
        ("iiiaii`ii", 1),
        ("iiiziii{iii", 1),
        ("iiiAiii@ii", 1),
        ("iiiZiii[iii", 1),
        ("Aa", 0),
        ("B!d", 2),
        ("C-c?e", 1),
    ))
