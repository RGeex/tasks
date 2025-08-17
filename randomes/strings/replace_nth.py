"""
Задача

Напишите метод, который заменяет каждый n-ный символ oldValue на символ newValue .
Входы

    text: строка для изменения
    n: меняйте целевую букву каждые nй происшествия
    old_value(или аналогично): целевой персонаж
    new_value(или аналогичный): символ, который будет использоваться в качестве замены

Примечание для нетипизированных языков: все входные данные всегда допустимы и соответствуют ожидаемому типу.
Правила

    Ваш метод должен быть чувствителен к регистру!
    Если n равно 0 или отрицательно, или если оно больше, чем количество oldValue, вернуть исходный текст без изменений.

Пример:

n:         2
old_value: 'a'
new_value: 'o'
"Vader said: No, I am your father!"
  1     2          3        4       -> 2nd and 4th occurence are replaced
"Vader soid: No, I am your fother!"

Как видно из примера: первым изменяется вторая буква «a».
Поэтому начало всегда с n-го подходящего символа, а не с первого!

"""
import typing
import unittest


def replace_nth(text: str, n: int, old_value: str, new_value: str, t: int = 0) -> str:
    """
    Заменяет каждый N-ый заданный символ в строке на новый.
    """
    return ''.join([x, new_value][n > 0 and t != (t := t + (x == old_value)) and not t % n] for x in text)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase( type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(replace_nth, (
        (["Vader said: No, I am your father!", 2, 'a', 'o'], "Vader soid: No, I am your fother!"),
        (["Vader said: No, I am your father!", 4, 'a', 'o'], "Vader said: No, I am your fother!"),
        (["Vader said: No, I am your father!", 6, 'a', 'o'], "Vader said: No, I am your father!"),
        (["Vader said: No, I am your father!", 0, 'a', 'o'], "Vader said: No, I am your father!"),
        (["Vader said: No, I am your father!", -2, 'a', 'o'], "Vader said: No, I am your father!"),
        (["Vader said: No, I am your father!", 1, 'i', 'y'], "Vader sayd: No, I am your father!"),
        (["Luke cries: Noooooooooooooooo!", 6, 'o', 'i'], "Luke cries: Noooooioooooioooo!"),
    ))
