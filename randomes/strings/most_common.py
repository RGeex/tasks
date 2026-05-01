"""
Дана строка s; функция возвращает новую строку, в которой символы упорядочены по
частоте встречаемости.

Возвращаемая строка должна содержать такое же количество символов, как и исходная строка.

Сделайте преобразование стабильным, то есть символы, которые при сравнении оказываются равными,
должны оставаться в своем исходном порядке в строке s.

most_common("Hello world") => "lllooHe wrd"
most_common("Hello He worldwrd") => "lllHeo He wordwrd"

Объяснение:

В hello worldНапример, их 3. 'l'персонажей, 2 'o'персонажей, и по одному из 'H', 'e', ' ', 'w', 'r',
и 'd'персонажей. Поскольку 'He wrd'Все они связаны между собой, они расположены в том же относительном
порядке, что и в исходной строке. 'Hello world'.

Обратите внимание, что ничья возникает не только в случае, если символы встречаются в строке один раз.
См. второй пример. most_common("Hello He worldwrd")должен вернуться 'lllHeo He wordwrd',
нет 'lllHHeeoo  wwrrdd'Это ключевое свойство, если данный метод используется для преобразования
строки в несколько этапов.
"""
import unittest
from typing import Any, Callable, Tuple


def most_common(s: str) -> str:
    """
    Сортирует строку по кол-ву встречаемых в строке символов в убывающем порядке.
    """
    return ''.join(sorted(s, key=s.count, reverse=True))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(most_common, (
        ("Hello world", "lllooHe wrd"),
        ("", ""),
        ("wubz dermatoglyphics", "wubz dermatoglyphics"),
    ))
