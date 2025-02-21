"""
Учитывая строку слов (x), вам нужно вернуть массив слов, отсортированный в алфавитном порядке по конечным символам в каждом.

Если два слова имеют одинаковую последнюю букву, возвращенный массив должен показать их в том порядке, в котором они появились в данной строке.

Все входы будут действительными.
"""
import typing
import unittest


def last(st: str) -> list[str]:
    """
    Сортирует строку слов по последней букву каждого слова.
    """
    return sorted(st.split(), key=lambda x: x[-1])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(last, (
        ("man i need a taxi up to ubud", ["a", "need", "ubud", "i", "taxi", "man", "to", "up"]),
        ("what time are we climbing up the volcano", ["time", "are", "we", "the", "climbing", "volcano", "up", "what"]) ,
        ("take me to semynak", ["take", "me", "semynak", "to"]),
        ("massage yes massage yes massage", ["massage", "massage", "massage", "yes", "yes"]),
        ("take bintang and a dance please", ["a", "and", "take", "dance", "please", "bintang"]),
    ))
