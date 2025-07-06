"""
Вы, наверное, знаете, что некоторые символы, написанные на листе бумаги,
после поворота этого листа на 180 градусов, можно прочитать, хотя иногда
и по-другому. Так, заглавные буквы «H», «I», «N», «O», «S», «X», «Z» после
поворота не меняются, буква «M» становится «W», и наоборот, буква «W»
становится «M».

Мы назовем слово «шифтером», если оно состоит только из букв «H», «I», «N», «O»,
«S», «X», «Z», «M» и «W». Перевернув лист, это слово тоже можно прочитать,
хотя и по-другому. Так, слово «WOW» превращается в слово «MAM». С другой стороны,
слово «HOME» не является шифтером.

Найти количество уникальных слов-шифтеров во входной строке (без дубликатов).
Все слова-шифтеры должны быть подсчитаны, даже если они парные
(например, "MOM" и "WOW"). Строка содержит только заглавные буквы.
Примеры

shifter("SOS IN THE HOME") == 2 # shifter words are "SOS" and "IN"
shifter("WHO IS SHIFTER AND WHO IS NO") == 3 # shifter words are "WHO", "IS", "NO"
shifter("TASK") == 0 # no shifter words
shifter("") == 0 # no shifter words in empty string
"""
import typing
import unittest


def shifter(st: str) -> int:
    """
    Поиск кол-ва уникальных слов шифтеров в строке.
    """
    return len({x for x in st.split() if not set(x) - set("HINOSXZMW")})


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(shifter, (
        ("ON", 1),
        ("OS IS UPDATED", 2),
        ("WHO IS WHO", 2),
        ("JS", 0),
        ("I III I III", 2),
        ("", 0),
    ))
