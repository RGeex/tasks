"""
Твой отец не очень разбирается в пунктуации и постоянно ставит лишние
запятые в своих постах. Ты можешь стерпеть эти лишние предложения,
ведь он действительно так говорит, но эти лишние запятые нужно убрать!

Напишите функцию, которая принимает строку в качестве аргумента и
возвращает строку, удалив лишние запятые. Возвращаемая строка не
должна заканчиваться запятой или иметь пробелы в конце.

"""
import typing
import unittest
import re


def dad_filter(string: str) -> str:
    """
    Убирает лишние запятые.
    """
    return re.sub(r',+', ',', string).strip(', ')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(dad_filter, (
        ("all this,,,, used to be trees,,,,,,", "all this, used to be trees"),
        ("Listen,,,, kid,,,,,,", "Listen, kid"),
        ("Luke,,,,,,,,, I am your father,,,,,,,,,  ", "Luke, I am your father"),
        ("i,, don't believe this round earth,,, show me evadence!!", "i, don't believe this round earth, show me evadence!!"),
        ("Dead or alive,,,, you're coming with me,,,   ", "Dead or alive, you're coming with me"),
    ))
