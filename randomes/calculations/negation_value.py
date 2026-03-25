"""

В программировании вы знаете оператор логического отрицания ( ! ),
он меняет значение условия на противоположное.

!false = true
!!false = false

Ваша задача — доработать функцию 'negationValue()', которая принимает строку отрицаний со значением
и возвращает то, каким было бы это значение, если бы к нему были применены эти отрицания.

negation_value("!", False) #=> True
negation_value("!!!!!", True) #=> False
negation_value("!!", []) #=> False

Не используйте eval()функция или Function()конструктор в JavaScript.

Примечание: Функция всегда возвращает логическое значение, даже если нет отрицаний.
"""
import unittest
from typing import Any, Callable, Tuple


def negation_value(s: str, val: Any) -> bool:
    """
    Реверсирует N раз булево значение.
    """
    return [bool(val), not val][len(s) % 2]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(negation_value, (
        (("", True), True),
        (("", False), False),
        (("!", False), True),
        (("!", True), False),
        (("!!!", []), True),
    ))
