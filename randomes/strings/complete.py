"""
Задание: объединить одну или несколько букв. в конец заданной входной строки создать строку,
которая читается так же вперед как назад.

Технические характеристики

    Буквы можно добавлять только в правую часть входной строки.

    Необходимо добавить к входной строке хотя бы одну букву.

    Правильная строка — более короткая. Например, (ab) => abba — это неправильно.
    while (ab)=> aba is Right.

    Входные данные будут состоять из одной или нескольких букв, как заглавных, так и строчных.

    Строки чувствительны к регистру. Например, (Gn) => gng — это неправильно,
    а (Gn) => GnG — правильно.

Примеры:
(a) => a + a => aa

(GG) => GG + G => GGG

(Ab) => Ab + A => AbA

(aba) => aba + ba => ababa

(aab) => aab + aa => aabaa
"""
import unittest
from typing import Any, Callable, Tuple


def complete(st: str) -> str:
    """
    Объединяет одну или несколько букв. в конец заданной входной, для создания анаграммы.
    """
    return next(x for i in range(len(st)) if (x := st + st[i::-1]) == x[::-1])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(complete, (
        ("Baa", "BaaB"),
        ("aaB", "aaBaa"),
        ("x", "xx"),
        ("aaBB", "aaBBaa"),
    ))
