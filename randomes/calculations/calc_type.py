"""
Вам необходимо создать функцию, которая принимает 3 числовых аргумента и 2 операнда.
a и bи результат неизвестной операции, выполненной над ними.

На основе этих трех значений необходимо вернуть строку, описывающую,
какая операция была использована для получения заданного результата.

Возможные возвращаемые строки: "addition", "subtraction", "multiplication", "division".
Примеры:

(a = 1, b = 2, result = 3)   --> 1 ? 2 = 3   --> "addition"
(a = 5, b = 2, result = 2.5) --> 5 ? 2 = 2.5 --> "division"

Примечания

    Он /Оператор выполняет простое деление без округления.
    Можно предположить, что всегда будет существовать единственный допустимый ответ
    (без неоднозначных случаев, например, таких как...).
    1 ? 0 = 0что может быть либо - или +, или 3 ? 1 = 3что может быть либо * или /).
    Можно предположить, что деления на не будет. 0

"""
import unittest
from typing import Any, Callable, Tuple


def calc_type(a: int, b: int, res: int | float) -> str:
    """
    Определяет, какая операция была произведена для получения заданного результата.
    """
    return {a + b == res: "addition", a - b == res: "subtraction", a * b == res: "multiplication", a / b == res: "division"}.get(1, '')


def calc_type_2(a: int, b: int, res: int | float) -> str:
    """
    Определяет, какая операция была произведена для получения заданного результата.
    """
    return {a + b: "addition", a - b: "subtraction", a * b: "multiplication", a / b: "division"}.get(res, '')


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(calc_type, (
        ((1, 2, 3), "addition"),
        ((10, 5, 5), "subtraction"),
        ((10, 4, 40), "multiplication"),
        ((9, 5, 1.8), "division"),
    ))
    test(calc_type_2, (
        ((1, 2, 3), "addition"),
        ((10, 5, 5), "subtraction"),
        ((10, 4, 40), "multiplication"),
        ((9, 5, 1.8), "division"),
    ))
