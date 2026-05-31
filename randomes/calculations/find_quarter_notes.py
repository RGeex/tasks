"""
Имея заданный размер (в виде строки), необходимо найти количество четвертных нот,
которые могут поместиться в один такт. Результат будет возвращен в виде беззнакового целого числа.
Если в такт помещается нецелое число четвертных нот, значение следует округлить до целого числа.
НЕ ВОЗВРАЩАЙТЕ НЕЦЕЛОЕ ЧИСЛО.

Указанный размер такта:

    Не будет иметь дефектов
    Максимальное число будет ниже 4096.
    Будет иметь нижнее число ниже 256.

Все допустимые тактовые размеры должны иметь нижний знак, являющийся степенью двойки.
Если данный размер недействителен, вернуть значение.
Noneна языке Python, nullна JavaScript и TypeScript, или -1в С.

Если в такте помещается менее одной четвертной ноты, верните 0;

Примеры:

"3/4"→ 3

"7/8"→ 3

"11/8"→ 5

"10/7"→ None/ null/ -1

"3/16"→ 0
"""
import unittest
from typing import Any, Callable, Tuple


def find_quarter_notes(time_signature: str) -> int | None:
    """
    Определяет количество четвертных нот.
    """
    t, b = map(int, time_signature.split("/"))
    return (t // (b / 4)) if b.bit_count() == 1 else None


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_quarter_notes, (
        ('4/4',   4),
        ('3/4',   3),
        ('6/8',   3),
        ('9/8',   4),
        ('1/8',   0),
        ('1/16',  0),
        ('9/0',  None),
        ('7/3',  None),
        ('6/5',  None),
        ('5/6',  None),
    ))
