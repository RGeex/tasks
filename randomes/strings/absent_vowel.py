"""
Ваша задача — выяснить индекс гласной, отсутствующей в данной строке:

    Aимеет индекс 0,
    Eимеет индекс 1,
    Iимеет индекс 2,
    Oимеет индекс 3,
    Uимеет индекс 4.

Примечания: Нет необходимости в проверке строки, и каждое данное предложение будет содержать все гласные,
кроме одной. Также вам не нужно будет беспокоиться о заглавных буквах.
Примеры

"John Doe hs seven red pples under his bsket"          =>  0  ; missing: "a"
"Bb Smith sent us six neatly arranged range bicycles"  =>  3  ; missing: "o"
"""
import typing
import unittest


def absent_vowel(st: str) -> int:
    """
    Поиск индекса отсутствующей гласной в слове.
    """
    return 'aeiou'.index((set('aeiou') - {x for x in st.lower() if x in 'aeiou'}).pop())


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(absent_vowel, (
        ("John Doe hs seven red pples under his bsket", 0),
        ("Bb Smith sent us six neatly arranged range bicycles", 3),
    ))
