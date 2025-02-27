"""
Боб ленивый человек.

Ему нужно, чтобы вы создали метод, который может определить, сколько letters , и в нижней части, (как буквы ASCII и digits в данной строке.

Пример:

"hel2! LO" -> 6

"!? .. A" -> 1
"""
import typing
import unittest


def count_letters_and_digits(st: str) -> int:
    """
    Определяет кол-во цифр и букв в строке.
    """
    return sum(1 for x in st if x.isdigit() or x.isalpha())


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(count_letters_and_digits, (
        ('n!!ice!!123', 7),
        ('de?=?=tttes!!t', 8),
        ('', 0),
        ('!@#$%^&`~.', 0),
        ('u_n_d_e_r__S_C_O_R_E', 10),
    ))
