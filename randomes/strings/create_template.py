"""
Реализовать функцию createTemplateкоторый принимает строку с тегами,
завернутыми в {{brackets}}в качестве входных данных и возвращает замыкание,
которое может заполнять строку данными (плоский объект, где ключами являются имена тегов).

template = create_template("{{name}} likes {{animalType}}")
template(name="John", animalType="dogs") # John likes dogs

Если ключа нет в карте, поместите туда пустую строку.с
"""
import typing
import unittest
import re
from typing import Callable


def create_template(template: str) -> Callable:
    """
    Создает ункцию за замены слов в тексте по шаблону.
    """
    return lambda **x: re.sub(r'{{(.*?)}}', lambda m: x.get(m.group(1), ''), template)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    template = create_template("{{firstName}} {{lastName}} likes {{interests}}")
    test(lambda x: x, (
        (template(firstName="John", lastName="Smith", interests="sport"), "John Smith likes sport"),
        (template(firstName="Albert", lastName="Einstein", occuptation="physicist"), "Albert Einstein likes "),
    ))
    template = create_template("{{foo}} bar {{baz}}")
    test(lambda x: x, (
        (template(), " bar "),
    ))
