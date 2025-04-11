"""
Напишите метод, который будет искать в массиве строк все строки,
содержащие другую строку, игнорируя регистр. Затем вернет массив найденных строк.

Метод принимает два параметра: строку запроса и массив строк для поиска,
и возвращает массив.

Если строка не содержится ни в одной из строк массива, метод возвращает массив,
содержащий одну строку: «Пусто» (или Nothingв Haskell или «None» в Python и C)
Примеры

Если строка для поиска — «me», а массив для поиска —
[«home», «milk», «Mercury», «fish»], метод должен вернуть [«home», «Mercury»].

"""
import typing
import unittest


def word_search(query: str, seq: list[str]) -> list[str]:
    """
    Поиск в массиве слов, содержащих искомую подстроку.
    """
    return [word for word in seq if query.lower() in word.lower()] or ['None']
    

def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(word_search, (
        (("ab", ["za", "ab", "abc", "zab", "zbc"]), ["ab", "abc", "zab"]),
        (("aB", ["za", "ab", "abc", "zab", "zbc"]), ["ab", "abc", "zab"]),
        (("ab", ["za", "aB", "Abc", "zAB", "zbc"]), ["aB", "Abc", "zAB"]),
        (("abcd", ["za", "aB", "Abc", "zAB", "zbc"]), ["None"]),
    ))
