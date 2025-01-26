"""
Ваш друг не перестанет писать своей девушке. Это все, что он делает. Весь день. Серьезно.
Тексты тоже такие мягкие! Вся эта ситуация просто заставляет вас чувствовать себя плохо.
Будучи замечательным другом, вы вынашиваете злой заговор. Пока он спит, вы берете его
телефон и меняете параметры автозамены, чтобы каждый раз, когда он набирает «ты» или «ты»,
оно менялось на «твоя сестра».

Напишите функцию с названием autocorrect это берет строку и заменяет все экземпляры "you"
или "u" (не чувствителен к случаю) с "your sister" (всегда нижний случай).

Вернуть полученную строку.

Вот немного сложная часть: это текстовые сообщения, поэтому существуют разные формы «вы»
и «u».

Для целей этой Kata, вот что вам нужно для поддержки:

    "Youuuuuu" с любым количеством персонажей U, прикрепленных к концу
    «U» в начале, середине или конце строки, но не частью слова
    "Вы", но не как часть другого слова, такого как YouTube или Bayou
"""
import re
import typing
import unittest


def autocorrect(st: str) -> str:
    """
    Заменяет you+ или u на your sister.
    """
    return re.sub(r'(?i)\b(you+|u)\b', 'your sister', st)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(autocorrect, (
        ("u", "your sister"),
        ("you", "your sister"),
        ("Youuuuu", "your sister"),
        ("youtube", "youtube"),
    ))
