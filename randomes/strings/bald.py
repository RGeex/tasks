"""
Будучи сам лысым, я знаю это чувство, когда нужно держать его чисто выбритым.
Нет ничего хуже, чем развевающиеся на ветру торчащие волосы.

Вам будет предоставлена ​​строка(x). Чисто выбритая голова отображается как "-",
а лишние волосы отображаются как "/". Ваша задача - проверить голову на наличие
лишние волосы и избавиться от них.

Вам следует вернуть исходную строку, но с удаленными лишними волосками. Однако
продолжайте считать их, так как есть второй элемент, который вам нужно вернуть:

0 hairs --> "Clean!"
1 hair --> "Unicorn!"
2 hairs --> "Homer!"
3-5 hairs --> "Careless!"
>5 hairs --> "Hobo!"

Итак, для этого заголовка: "------/------" вы должны вернуть:

["-------------", "Unicorn"]
"""
import typing
import unittest


def bald(st: str) -> list[str]:
    """
    Подсчитывает кол-во волосков на голове и сбривает их.
    """
    return [st.replace('/', '-'), {0: "Clean!", 1: "Unicorn!", 2: "Homer!", 3: "Careless!", 4: "Careless!", 5: "Careless!"}.get(st.count('/'), "Hobo!")]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(bald, (
        ("/---------", ["----------", "Unicorn!"]),
        ("/-----/-", ["--------", "Homer!"]),
        ("--/--/---/-/---", ["---------------", "Careless!"]),
    ))
