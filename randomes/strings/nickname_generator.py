"""
Генератор ников

Напишите функцию, nicknameGeneratorкоторый принимает строковое имя в качестве аргумента и
возвращает первые 3 или 4 буквы в качестве псевдонима.

Если третья буква — согласная, верните первые 3 буквы.

nickname("Robert") //=> "Rob"
nickname("Kimberly") //=> "Kim"
nickname("Samantha") //=> "Sam"

Если третья буква — гласная, верните первые 4 буквы.

nickname("Jeannie") //=> "Jean"
nickname("Douglas") //=> "Doug"
nickname("Gregory") //=> "Greg"

Если строка короче 4 символов, возвращается «Ошибка: имя слишком короткое».

Примечания:

    Гласные — «aeiou», поэтому букву «y» можно не учитывать.
    Входные данные всегда будут строкой.
    Вводимая буква всегда будет заглавной, а остальные строчными (например, Сэм).
    Входные данные могут быть изменены.


"""
import typing
import unittest


def nickname_generator(name: str) -> str:
    """
    Создает никнеймы из имени.
    """
    return 'Error: Name too short' if len(name) < 4 else name[:[3, 4][name[2] in 'aeiou']]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(nickname_generator, (
        ("Jimmy", "Jim"),
        ("Samantha", "Sam"),
        ("Sam", "Error: Name too short"),
        ("Kayne", "Kay"),
        ("Melissa", "Mel"),
        ("James", "Jam"),
        ("Gregory", "Greg"),
        ("Jeannie", "Jean"),
        ("Kimberly", "Kim"),
        ("Timothy", "Tim"),
        ("Dani", "Dan"),
        ("Saamy", "Saam"),
        ("Saemy", "Saem"),
        ("Saimy", "Saim"),
        ("Saomy", "Saom"),
        ("Saumy", "Saum"),
        ("Boyna", "Boy"),
        ("Kiyna", "Kiy"),
        ("Sayma", "Say"),
        ("Ni", "Error: Name too short"),
        ("Jam", "Error: Name too short"),
        ("Suv", "Error: Name too short"),
    ))
