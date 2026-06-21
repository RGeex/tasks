"""
Представьте себе круг. Чтобы закодировать слово. codewars,
мы могли бы разделить круг на 8 частей (как codewarsсодержит 8 букв):
Затем добавьте буквы по часовой стрелке: Затем удалите кружок:

Если читать результат слева направо, то получим csordaew.

Декодирование — это тот же процесс, но в обратном порядке.
Если мы декодируем csordaew, мы получаем codewars.
Примеры:

    encode "codewars" -> "csordaew"
    decode "csordaew" -> "codewars"

    encode "white" -> "wehti"
    decode "wehti" -> "white"

"""
import unittest
from typing import Any, Callable, Tuple


def encode(s: str) -> str:
    """
    Шифрует строку.
    """
    return ''.join(a + b for a, b in zip(s, s[-1::-1]))[:len(s)]


def decode(s: str) -> str:
    """
    Расшифровывает строку.
    """
    return s[::2] + s[-(len(s) % 2 + 1)::-2]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(encode, (
        ("codewars", "csordaew"),
        ("white", "wehti"),
        ("Assert", "Atsrse"),
        ("Hello world!", "H!edlllroo w"),
        ("You have chosen to translate this kata.", "Y.oaut ahka vsei hcth oesteanl stnoa rt"),
    ))
    test(decode, (
        ("csordaew", "codewars"),
        ("wehti", "white"),
        ("Atsrse", "Assert"),
        ("H!edlllroo w", "Hello world!"),
        ("Y.oaut ahka vsei hcth oesteanl stnoa rt", "You have chosen to translate this kata."),
    ))
