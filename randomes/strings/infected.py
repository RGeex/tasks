"""
⚠️ Мир на карантине! Новая пандемия, которая борется с человечеством.
Каждый континент изолирован друг от друга, но инфицированные люди распространились до
предупреждения.

🗺️ Вам будет предоставлена ​​карта мира в виде строки:

string s = "01000000X000X011X0X"

'0' : uninfected

'1' : infected

'X' : ocean

⚫ Вирус не может распространяться по ту сторону океана.

⚫ Если один человек заразится, все люди на этом континенте тоже заразятся.

⚫ Ваша задача — найти процент населения, которое в итоге заразилось.

☑️ Верните процент инфицированного населения от общей численности населения.

❗❗ Первый и последний континент не связаны!

💡 Пример:

 start: map1 = "01000000X000X011X0X"
 end:   map1 = "11111111X000X111X0X"
 total = 15
 infected = 11
 percentage = 100*11/15 = 73.33333333333333

➕ Для карт без океанов «X» весь мир соединен.

➕ Для карт без «0» и «1» верните 0, поскольку население отсутствует.
"""
import typing
import unittest


def infected(st: str) -> int | float:
    """
    Определяет процент зараженных.
    """
    return 100 * sum(len(x) for x in st.split('X') if '1' in x) / (len(st.replace('X', '')) or 1)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(infected, (
        ("01000000X000X011X0X",73.33333333333333),
        ("01X000X010X011XX", 72.72727272727273),
        ("XXXXX", 0),
        ("00000000X00X0000", 0),
        ("0000000010", 100),
        ("000001XXXX0010X1X00010", 100),
        ("X00X000000X10X0100",42.857142857142854),
    ))
