"""
Представьте себе игру, в которой игрок должен угадать загаданное слово. Игроку известна только его длина.

Чтобы помочь детям в достижении их цели, игра будет принимать догадки и показывать количество букв, которые находятся на правильной позиции.

Напишите метод, который, учитывая правильное слово и предположение игрока, возвращает это число.

Например, вот возможный ход мыслей человека, пытающегося угадать слово «собака»:

count_correct_characters("dog", "car"); #0 (No letters are in the correct position)
count_correct_characters("dog", "god"); #1 ("o")
count_correct_characters("dog", "cog"); #2 ("o" and "g")
count_correct_characters("dog", "cod"); #1 ("o")
count_correct_characters("dog", "bog"); #2 ("o" and "g")
count_correct_characters("dog", "dog"); #3 (Correct!)

Вызывающий должен убедиться, что угадываемое слово всегда имеет ту же длину, что и
правильное слово, но поскольку в противном случае могут возникнуть проблемы, вам необходимо проверить такую ​​возможность:

#Raise an exception if the two parameters are of different lengths.

Однако вы можете предположить, что оба параметра всегда будут в одном и том же регистре.

"""
import typing
import unittest


def count_correct_characters(correct: str, guess: str) -> int:
    """
    Проверяет, сколько букв оказались на своих местах.
    """
    if len(correct) == len(guess):
        return sum(a == b for a, b in zip(correct, guess))
    raise ValueError('Raise an exception if the two parameters are of different lengths')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(count_correct_characters, (
        (("dog", "car"), 0),
        (("dog", "god"), 1),
        (("dog", "cog"), 2),
        (("dog", "cod"), 1),
        (("dog", "bog"), 2),
        (("dog", "dog"), 3),
    ))
