"""
Задание 4 первой недели ASC (средний уровень #1)

Напишите функцию, которая преобразует любое предложение в предложение типа VAPORWAVE.
Предложение типа VAPORWAVE преобразует все буквы в верхний регистр и добавляет 2
пробела между каждой буквой (или специальным символом), чтобы создать этот эффект VAPORWAVE.

Обратите внимание, что в данном случае пробелы следует игнорировать.
Примеры

"Lets go to the movies"       -->  "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
"Why isn't my code working?"  -->  "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"
"""
import unittest
from typing import Any, Callable, Tuple


def vaporcode(s: str) -> str:
    """
    Преобразование строки в вапрокод.
    """
    return '  '.join(s.upper().replace(' ', ''))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(vaporcode, (
        ("Lets go to the movies","L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"),
        ("Why isn't my code working?","W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"),
    ))
