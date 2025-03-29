"""
Вам будет предоставлен массив чисел.

Для каждого числа в массиве вам необходимо будет создать объект.

Ключом объекта будет число в виде строки. Значением будет соответствующий код символа в виде строки.

Верните массив полученных объектов.

Все входные данные будут массивами чисел. Все коды символов — допустимые строчные буквы.
Входной массив не будет пустым.
"""
import typing
import unittest


def num_obj(arr: list[int]) -> list[dict]:
    """
    Создает словари из заданных чисел.
    """
    return [{str(x): chr(x)} for x in arr]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(num_obj, (
        ([118,117,120],[{'118':'v'}, {'117':'u'}, {'120':'x'}]),
        ([101,121,110,113,113,103],[{'101':'e'}, {'121':'y'}, {'110':'n'}, {'113':'q'}, {'113':'q'}, {'103':'g'}]),
        ([118,103,110,109,104,106],[{"118":"v"},{"103":"g"},{"110":"n"},{"109":"m"},{"104":"h"},{"106":"j"}]),
        ([107,99,110,107,118,106,112,102],[{"107":"k"},{"99":"c"},{"110":"n"},{"107":"k"},{"118":"v"},{"106":"j"},{"112":"p"},{"102":"f"}]),
        ([100,100,116,105,117,121 ],[{"100":"d"},{"100":"d"},{"116":"t"},{"105":"i"},{"117":"u"},{"121":"y"}]),
    ))
