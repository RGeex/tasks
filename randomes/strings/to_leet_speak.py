"""
Ваша задача — написать функцию, которая преобразует обычное английское предложение в язык Leetspeak .

Изменять следует только заглавные буквы; строчные буквы, цифры и пробелы изменять не нужно.

Например:
"LEET" --> "1337"
"aA8 " --> "a@8 "
В этом ката мы используем простой диалект LeetSpeak. Используйте следующий алфавит:
"""
import unittest
from typing import Any, Callable, Tuple

abc = {
    "A": "@",
    "B": "8",
    "C": "(",
    "D": "D",
    "E": "3",
    "F": "F",
    "G": "6",
    "H": "#",
    "I": "!",
    "J": "J",
    "K": "K",
    "L": "1",
    "M": "M",
    "N": "N",
    "O": "0",
    "P": "P",
    "Q": "Q",
    "R": "R",
    "S": "$",
    "T": "7",
    "U": "U",
    "V": "V",
    "W": "W",
    "X": "X",
    "Y": "Y",
    "Z": "2"
}


def to_leet_speak(s: str) -> str:
    """
    Заменяет указанные буквы на заданные символы в строке.
    """
    return s.translate(str.maketrans("".join(abc.keys()), "".join(abc.values())))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(to_leet_speak, (
        ("LEET", "1337"),
        ("CODEWARS", "(0D3W@R$"),
        ("HELLO WORLD", "#3110 W0R1D"),
        ("LOREM IPSUM DOLOR SIT AMET", "10R3M !P$UM D010R $!7 @M37"),
        ("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", "7#3 QU!(K 8R0WN F0X JUMP$ 0V3R 7#3 1@2Y D06"),
    ))
