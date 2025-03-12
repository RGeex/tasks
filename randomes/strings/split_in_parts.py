"""
Цель этого ката — разбить заданную строку на разные строки одинакового размера (обратите внимание, что размер строк передается методу).

Пример:

Split the below string into other strings of size #3

'supercalifragilisticexpialidocious'

Will return a new string
'sup erc ali fra gil ist ice xpi ali doc iou s'
Предположения:

String length is always greater than 0
String has no spaces
Size is always positive
"""
import typing
import unittest


def split_in_parts(st: str, part_length: int) -> str:
    """
    Делит строку по заданному числу символов через пробел.
    """
    return ' '.join([st[i:i + part_length] for i in range(0, len(st), part_length)])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(split_in_parts, (
        (("supercalifragilisticexpialidocious", 3), "sup erc ali fra gil ist ice xpi ali doc iou s"),
        (("HelloKata", 1), "H e l l o K a t a"),
        (("HelloKata", 9), "HelloKata"),
    ))
