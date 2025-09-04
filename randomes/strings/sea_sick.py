"""
Из-за последствий Эль-Ниньо в этом году моя поездка на каникулы с аквалангом
напоминала стирку в стиральной машине... Совсем не весело.

Если дана строка, состоящая из символов «~» и «_», обозначающих волны и штиль
соответственно, ваша задача — проверить, будет ли человек страдать морской болезнью.

Переходы от спокойного состояния к волне или от волны к спокойному усилят
эффект (на самом деле, это просто волна от пика к впадине, но и этого будет достаточно).
Узнайте, сколько раз уровень звука меняется в струне, и если это число превышает 20% от
её длины, верните «Throw Up», в противном случае верните «No Problem».
"""
import typing
import unittest


def sea_sick(sea: str) -> str:
    """
    Определяет является ли число переходов состояний более 20% от длины.
    """
    return ["No Problem", "Throw Up"][sum(len(set(sea[i:i+2])) == 2 for i in range(len(sea))) > len(sea) * .2]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sea_sick, (
        ("~", "No Problem"),
        ("_~~~~~~~_~__~______~~__~~_~~", "Throw Up"),
        ("______~___~_", "Throw Up"),
        ("____", "No Problem"),
        ("_~~_~____~~~~~~~__~_~", "Throw Up"),
    ))
