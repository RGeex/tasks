"""
Создайте функцию, которая принимает входную строку и возвращает строку,
где все заглавные слова входной строки находятся в начале, а все строчные
слова — в конце. Порядок заглавных и строчных букв в словах должен
соответствовать порядку их появления.

Если слово начинается с цифры или специального символа, пропустите слово и
исключите его из результата.

Входная строка не будет пустой.

Для входной строки: "hey You, Sort me Already!"  функция должна вернуть: "You, Sort Already! hey me"

"""
import typing
import unittest


def capitals_first(text: str) -> str:
    """
    Упорядочивает слова в строке, исключая слова не начинающиеся с буквы.
    """
    return ' '.join([b for a in zip(*[[x, ''][::x[0].isupper() or -1] for x in text.split() if x[0].isalpha()]) for b in a if b])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(capitals_first, (
        ("sense Does to That Make you?", "Does That Make sense to you?"),
        ("hey You, Sort me Already", "You, Sort Already hey me"),
        ("sense Does to That Make you?", "Does That Make sense to you?"),
        ("i First need Thing In coffee The Morning", "First Thing In The Morning i need coffee"),
        ("123 baby You and Me", "You Me baby and"),
        ("Life gets Sometimes pretty !Hard", "Life Sometimes gets pretty"),
    ))
