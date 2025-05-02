"""
Сделайте свои строки более занудными: замените все «a»/«A» на 4, «e»/«E» на 3 и «l» на 1
например  "Fundamentals" --> "Fund4m3nt41s"
"""
import typing
import unittest


def nerdify(st: str) -> str:
    """
    Заменяет символы в строке по шаблону.
    """
    return st.translate(str.maketrans('aAeEl', '44331'))



def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(nerdify, (
        ("Fundamentals", "Fund4m3nt41s"),
        ("Seven", "S3v3n"),
        ("Los Angeles", "Los 4ng313s"),
        ("Seoijselawuue", "S3oijs314wuu3"),

    ))
