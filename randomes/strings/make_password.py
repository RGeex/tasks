"""
Один из вариантов создания удовлетворительного пароля — начать с запоминающейся фразы или предложения и создать пароль, извлекая первые буквы каждого слова.

Еще лучше заменить некоторые из этих букв цифрами (например, букву Oможно заменить на число 0):

    вместо того, чтобы включить i или Iпоставьте номер 1в пароле;
    вместо того, чтобы включить o или Oпоставьте номер 0в пароле;
    вместо того, чтобы включить s или Sпоставьте номер 5в пароле.

Примеры:

"Give me liberty or give me death"  --> "Gml0gmd"
"Keep Calm and Carry On"            --> "KCaC0"
"""
import typing
import unittest


def make_password(st: str) -> str:
    """
    Создание пароля из заданной строки.
    """
    return ''.join([{'o': '0', 'i': '1', 's': '5'}.get(x[0].lower(), x[0]) for x in st.split()])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(make_password, (
        ("Give me liberty or give me death", "Gml0gmd"),
        ("Keep Calm and Carry On", "KCaC0"),
    ))
