"""
Задача
Дамп шестнадцатеричного формата должен содержать только допустимые шестнадцатеричные байты.

Действительный байт:

состоит ровно из двух символов.
содержит только шестнадцатеричные цифры ( 0-9, A-F).
Использует только заглавные буквы.
Возвращает индекс первого поврежденного байта.

Если каждый байт действителен, вернуть -1.

Примеры
find_corrupted_byte(["48", "65", "6C", "6C", "6F"])

-1
find_corrupted_byte(["48", "65", "6G", "6C", "6F"])

2
find_corrupted_byte(["48", "6", "6C"])

1
find_corrupted_byte(["48", "6c", "6F"])

1
Примечания
Входные данные представляют собой список строк.
Пустой список считается допустимым.


"""
import unittest
from typing import Any, Callable, List, Tuple


HEX = set("0123456789ABCDEF")


def find_corrupted_byte(dump: List[str]) -> int:
    """
    Поиск ближайшего поврежденного байта.
    """
    return next((i for i, x in enumerate(dump) if len(x) != 2 or set(x) - HEX), -1)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_corrupted_byte, (
        (["48", "65", "6C", "6C", "6F"], -1),
        (["48", "65", "6G", "6C", "6F"], 2),
        (["48", "6", "6C"], 1),
        (["48", "6c", "6F"], 1),
        (["FF", "00", "123"], 2),
    ))
