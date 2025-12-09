"""
Написать функцию sort_cards()который сортирует перемешанный список карт таким образом,
что любой заданный список карт сортируется по рангу, независимо от начальной коллекции.

Все карты в списке представлены в виде строк, поэтому отсортированный список карт выглядит
следующим образом:

['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

Пример:

>>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

Подсказка: тесты будут содержать много карт одинакового ранга, а также различаться по длине.
Однако можно предположить, что входной список всегда будет содержать хотя бы один элемент.

"""
import unittest
from typing import Any, Callable, Tuple


def sort_cards(cards: list[str]) -> list[str]:
    """
    Сортирует карты в колоде.
    """
    return sorted(cards, key='A23456789TJQK'.index)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_cards, (
        (list('39A5T824Q7J6K'), list('A23456789TJQK')),
        (list('Q286JK395A47T'), list('A23456789TJQK')),
        (list('54TQKJ69327A8'), list('A23456789TJQK')),
    ))

