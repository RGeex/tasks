"""
Вы возвращаетесь к своей новой работе по расшифровке для секретной организации,
когда получаете новое задание. Оказывается, враг общается с помощью устройства,
которое он называет «Зеркало».
Это элементарное устройство, которое шифрует сообщение, меняя букву на ее
зеркально противоположную (A => Z), (B => Y), (C => X) и т. д.

Ваша задача — создать метод под названием «зеркало», который расшифрует
сообщения. Полученные сообщения будут написаны строчными буквами.

Чтобы повысить секретность, необходимо принять второй необязательный параметр,
сообщающий, какие буквы или символы следует переставить; если он не указан,
по умолчанию будет использоваться весь алфавит.

Чтобы сделать это немного более понятным: например, в случае «abcdefgh» в
качестве второго необязательного параметра вы заменяете «a» на «h», «b» на «g» и т. д.

Например:

mirror("Welcome home"), "dvoxlnv slnv" #whole alphabet mirrored here
mirror("hello", "abcdefgh"), "adllo" #notice only "h" and "e" get reversed


"""
import typing
import unittest


def mirror(code: str, mode: str = 'abcdefghijklmnopqrstuvwxyz') -> str:
    """
    Производит замену символов зеркально по ключу.
    """
    return code.lower().translate(str.maketrans(mode, mode[::-1]))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(mirror, (
        (("Welcome home",), "dvoxlnv slnv"),
        (("hello",), "svool"),
        (("goodbye",), "tllwybv"),
        (("ngmlsoor",), "mtnohlli"),
        (("gsrh rh z hvxivg",), "this is a secret"),
        (("Welcome home", "w"), "welcome home"),
        (("hello", "abcdefgh"), "adllo"),
        (("goodbye", ""), "goodbye"),
        (("CodeWars", "+-*/="), "codewars"),
        (("this is a secret", " *"), "this*is*a*secret"),
    ))

# print(abc[:26//2])
# print(abc[26//2:][::-1])