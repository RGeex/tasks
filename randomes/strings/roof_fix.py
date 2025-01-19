"""
Спортивный центр требует ремонта. Вандалы с такой силой забивали мячи в крышу, что некоторые
черепицы начали торчать. Крыша представлена ​​буквой r.

В качестве быстрого решения комитет решил поставить сверху еще одну старую крышу, если они смогут
найти подходящую. Это ваша работа.

«Новая» крыша (f) подойдет, если в настоящее время в ней есть дыра в том месте, где на старой крыше
торчит черепица.

Прикрепленные плитки обозначаются либо «\», либо «/». Дыры в «новой» крыше обозначены пробелами
(' '). Любой другой персонаж не может переступить через торчащую плитку.

Возвращайте true, если новая крыша подходит, и false, если нет.
"""
import typing
import unittest


def roof_fix(f: str, r: str) -> bool:
    """
    Определяет, можно ил использовать старую крышу для починки.
    """
    return not next((1 for a, b in zip(f, r) if b != '_' and a != ' '), 0)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(roof_fix, (
        (('  l   f l k djmi k', r'___\_____//_____/_'), False),
        (('    ikm il  h  llmmc   a i', r'__\_______________________'), True),
        (('   h c ', r'__/____'), True),
        (('q h', r'_/_'), True),
        ((' cg dg   em  lfh cdam', r'_______/____\_____/_/'), False),
    ))
