"""
Моя подруга хочет придумать новое название для своей группы.
Ей нравятся группы, которые используют формулу:
"The" + существительное, первая буква которого заглавная, например:

"dolphin" -> "The Dolphin"

Однако, когда существительное НАЧИНАЕТСЯ и ЗАКАНЧИВАЕТСЯ на одну и ту же букву,
она любит повторять существительное дважды и соединять их первой и последней буквами,
объединяя в одно слово (БЕЗ артикля «The» перед ним), вот так:

"alaska" -> "Alaskalaska"

Завершите функцию, которая принимает существительное в виде строки и возвращает название
предпочитаемой ею группы, записанное в виде строки.


"""
import unittest
from typing import Any, Callable, Tuple


def band_name_generator(name: str) -> str:
    """
    Генерирует название из строки по заданному условию.
    """
    return (name + name[1:] if name[0] == name[-1] else f'the {name}').title()


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(band_name_generator, (
        ("knife", "The Knife"),
        ("tart", "Tartart"),
        ("sandles", "Sandlesandles"),
        ("bed", "The Bed"),
        ("qq", "Qqq"),
    ))
