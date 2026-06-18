"""
Шифр №1 - Шифр ​​01

Такого шифра не существует, я его только что создал сам. Использовать его невозможно,
так как расшифровать его невозможно. Это хеш. Несколько предложений могут дать одинаковый результат.
Как работает этот шифр

Оно смотрит на букву и видит её индекс в алфавите, а алфавит — это a-zЕсли вы не знали.
Если значение нечетное, оно заменяется на 1Если это четное число, оно заменяется на 0
Обратите внимание, что индекс должен начинаться с 0. Также, если символ не является буквой,
он остается неизменным.
Пример

encode("Hello World!"); // => "10110 00111!"

Это потому что HИндекс 's 7что странно, поэтому его заменяют на 1, и так далее.

Удачи в программировании!

"""
import unittest
from typing import Any, Callable, Tuple


def encode(s: str) -> str:
    """
    Зашифровывает строку по заданному алгоритму.
    """
    return ''.join(str(int(not ord(x) % 2)) if x.isalpha() else x for x in s)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(encode, (
        ("Hello World!", "10110 00111!"),
    ))
