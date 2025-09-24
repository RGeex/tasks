"""
Дан массив строк. Отсортируйте массив в порядке веса от легкого к тяжелому.

Единицами веса являются граммы (Г), килограммы (КГ) и тонны (Т).

Массивы всегда будут содержать правильные и положительные значения, а также заглавные буквы.

"""
import typing
import unittest
import re


def arrange(arr: list[str]) -> list[str]:
    """
    Сортирует список весов.
    """
    return sorted(arr, key=lambda x: int(re.sub(r'([A-Z]+)', lambda m: dict(zip(['KG', 'T'], ['000', '000000'])).get(m.group(), ''), x)))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(arrange, (
        (["200G","300G","150G","100KG"], ["150G","200G","300G","100KG"]),
        (["400G","100T","150KG","100G"], ["100G","400G","150KG","100T"]),
        (["4T","300G","450G","900KG"], ["300G","450G","900KG","4T"]),
        (["400T","100T","1T","100G"], ["100G","1T","100T","400T"]),
        (["1G","2KG","3T","100KG"], ["1G","2KG","100KG","3T"]),
        (["100KG","100G","150T","150KG"], ["100G","100KG","150KG","150T"]),
        (["3T","2900000G","2950KG"], ["2900000G","2950KG","3T"]),
        (["3T","3000001G","2950KG"], ["2950KG","3T","3000001G"]),
        (["1T"], ["1T"]),
        ([], []),
    ))
