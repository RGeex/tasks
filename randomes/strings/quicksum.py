"""
Контрольная сумма — это алгоритм, который сканирует пакет данных и возвращает одно число.
Идея заключается в том, что если пакет изменяется, контрольная сумма также изменится,
поэтому контрольные суммы часто используются для обнаружения изменений. ошибки передачи,
проверка содержимого документов и во многих других ситуациях, когда необходимо обнаружить
нежелательные изменения в данных.

В этой задаче вам предстоит реализовать алгоритм контрольной суммы, называемый Quicksum.
Пакет Quicksum допускает только заглавные буквы и пробелы. Он всегда начинается и заканчивается заглавной буквой.

В остальном, пробелы и заглавные буквы могут встречаться в любом сочетании,
включая последовательные пробелы.

Квиксумма — это сумма произведений позиции каждого символа в пакете на значение этого символа.
Пробел имеет значение ноль, а буквы — значение, равное их позиции в алфавите.

Так, A = 1, B = 2и т. д., через Z = 26Вот примеры вычислений Quicksum для пакетов. "ACM" и "A C M":

ACM
1 × 1 + 2 × 3 + 3 × 13 = 46 

A C M
1 x 1 + 3 x 3 + 5 * 13 = 75

Если пакет содержит не только заглавные буквы и пробелы или только пробелы,
результат функции quicksum должен быть равен нулю (0).

AbqTH #5 = 0
"""
import unittest
from typing import Any, Callable, Tuple
from string import ascii_uppercase as abc


def quicksum(packet: str) -> int:
    """
    Вычисляет квиксумму строки.
    """
    return sum(i * (abc.find(x) + 1) for i, x in enumerate(set(packet) <= set(f' {abc}') and packet or '', 1))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(quicksum, (
        ("ACM", 46),
        ("MID CENTRAL", 650),
        ("BBC", 15),
        ("???", 0),
        ("axg ", 0),
        ("234 234 WEF ASDF AAA 554211 ???? ", 0),
        ("A C M", 75),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 6201),
        ("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z", 12051),
        ("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ", 848640),
        ("Z     A", 33),
        ("12312 123 123 asd asd 123 $$$$/()=", 0),
        ("As ", 0),
        ("         ", 0),
    ))
