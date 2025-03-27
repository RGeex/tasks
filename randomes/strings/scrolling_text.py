"""
Давайте создадим бегущую строку текста!

Ваша задача — завершить функцию, которая принимает строку и возвращает массив со всеми
возможными поворотами заданной строки в верхнем регистре .
Пример

scrollingText("codewars")должен вернуть:

[ "CODEWARS",
  "ODEWARSC",
  "DEWARSCO",
  "EWARSCOD",
  "WARSCODE",
  "ARSCODEW"
  "RSCODEWA",
  "SCODEWAR" ]

"""
import typing
import unittest


def scrolling_text(st: str) -> list[str]:
    """
    Возвращает все вращения из заданной строки.
    """
    return [st.upper()[i:] + st.upper()[:i] for i in range(len(st))]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(scrolling_text, (
        ("abc", ["ABC","BCA","CAB"]),
    ))
