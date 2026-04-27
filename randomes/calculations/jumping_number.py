"""
Определение

Число-скачок — это число, у которого все соседние цифры отличаются на 1.
Задача

Если задано число, вернуть "Jumping!!"если это число, подверженное скачкам,
в противном случае вернуть. "Not!!".
Примечания

    Переданное число всегда является положительным целым числом.

    Возвращает результат в виде строки.

    Разница между цифрами 9 и 0не считается равным 1.

    Все однозначные числа считаются числами, совершающими скачки.

Примеры
н 	Ожидал 	Объяснение
9 	"Прыгаю!" 	Это однозначное число.
79 	"Нет!!" 	Соседние цифры не отличаются на 1.
23 	"Прыгаю!" 	Соседние цифры отличаются на 1.
556847 	"Нет!!" 	Соседние цифры не отличаются на 1.
4343456 	"Прыгаю!" 	Соседние цифры отличаются на 1.
89098 	"Нет!!" 	Соседние цифры не отличаются на 1.
32 	"Прыгаю!" 	Соседние цифры отличаются на 1.
"""
import unittest
from typing import Any, Callable, Tuple


def jumping_number(number):
    """
    Определяет является ли число скачковым или нет.
    """
    return next(('Not!!' for a, b in zip(str(number), str(number)[1:]) if abs(int(a) - int(b)) != 1), 'Jumping!!')


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(jumping_number, (
        (1, "Jumping!!"),
        (7, "Jumping!!"),
        (9, "Jumping!!"),
        (23, "Jumping!!"),
        (32, "Jumping!!"),
        (79, "Not!!"),
        (98, "Jumping!!"),
        (8987, "Jumping!!"),
        (4343456, "Jumping!!"),
        (98789876, "Jumping!!"),
        (987654322, "Not!!"),
    ))
