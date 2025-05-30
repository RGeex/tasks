"""
Дженни 9 лет. Она самый молодой детектив в Северной Америке. Дженни учится в 3 классе,
поэтому, когда появляется новая миссия, она получает код для расшифровки в виде наклейки
(с числами) в своей тетради по математике и комментарий (предложение) в своей тетради для
письма. Все, что ей нужно сделать, это придумать одно слово, а дальше она уже знает,
что делать. И вот тут наступает ваша очередь — вы можете помочь Дженни узнать, что это за слово!

Чтобы узнать, что это за слово, вам следует использовать наклейку (массив из 3 чисел),
чтобы извлечь 3 буквы из комментария (строки), которые составляют это слово.

    Каждое из чисел в массиве относится к положению буквы в строке в порядке возрастания.
    Пробелы — это не места, вам нужны сами буквы. Никаких пробелов.
    Возвращаемое слово должно состоять только из строчных букв.
    если вы не можете найти одну из букв, используя индексные номера, верните "Нет миссии сегодня".
    Дженни была бы очень расстроена, но такова жизнь... :(

Example: input: [5, 0, 3], "I Love You" output: "ivy" (0 = "i", 3 = "v", 5 = "y")
"""
import typing
import unittest


def missing(nums: list[str], st: str) -> str:
    """
    Расшифровывает послание.
    """
    result = ''.join([x for i, x in enumerate(st.lower().replace(' ', '')) if i in nums])
    return result if len(result) == len(nums) else "No mission today"


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(missing, (
        (([0, 3, 5], "I love you"), "ivy"),
        (([29, 31, 8], "The quick brown fox jumps over the lazy dog"), "bay"),
        (([12, 4, 6], "Good Morning"), "No mission today"),
    ))
