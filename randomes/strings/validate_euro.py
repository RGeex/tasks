"""
ЕЦБ (Европейский центральный банк) нуждается в вашей помощи! Они заметили, что из-за мошенников
распространяются поддельные евробанкноты.

Существуют продвинутые методы определения того, была ли купюра изготовлена ​​вручную или нет.
Но для евробанкнот существует специфический алгоритм (хотя я не могу найти никаких доказательств
этому, но каждая евробанкнота, которую я видел, соответствует этому алгоритму. Для целей этого
задания мы будем считать, что этот алгоритм абсолютно верен). Ваша задача — проверить подлинность
евробанкноты по её серийному номеру. Предположим, что все остальные детали купюры либо подлинные,
либо идеально изготовлены мошенниками.

Вот алгоритм:

Серийный номер каждой евробанкноты начинается с двух заглавных латинских букв и следует за ними 10 цифр.

1. Sum every digit in a serial number.
2. Get the English Alphabetical position of the two letters. (A - 1, B - 2, C - 3 and etc.).
3. Add those numbers to the already existing sum of digits.
4. Sum the result's digits up. If the sum is not 1-digit number, keep summing the new number's digits,
until the result is 1-digit number.

Если итоговый результат равен 7, значит, у вас в руках настоящая евробанкнота. В противном случае,
банкнота поддельная. Предположим, что каждый ввод соответствует требованиям серийного номера
(2 заглавные латинские буквы и 10 цифр).

Пример действительного серийного номера:

VA0436214792
V = 22; A = 1

22 + 1 + 0 + 4 + 3 + 6 + 2 + 1 + 4 + 7 + 9 + 2 = 61 -> 6 + 1 = 7 -> True

И один недействительный:

WF9804350654
W = 23; F = 6

23 + 6 + 9 + 8 + 0 + 4 + 3 + 5 + 0 + 6 + 5 + 4 = 73 -> 10 -> 1 -> False

Удачи!
"""
import unittest
from typing import Any, Callable, Tuple


def validate_euro(serial_number: str) -> bool:
    """
    Проверяет, является ли номер купюры подлинным.
    """
    return validate_euro(str(sum(int(x) if x.isdigit() else ord(x) - 64 for x in serial_number))) if len(serial_number) > 1 else int(serial_number) == 7


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(validate_euro, (
        ("VA0436214792", True),
        ("HG2015896213", True),
        ("UB5067129430", False),
        ("YZ8630148532", False),
        ("DA8374810231", False),
    ))

