"""
В этом задании вам будет дана строка, которая может содержать как заглавные,
так и строчные буквы, и ваша задача — преобразовать эту строку либо в текст
только в строчные буквы, либо только в заглавные буквы в зависимости от:

    Вносите как можно меньше изменений.
    Если строка содержит одинаковое количество заглавных и строчных букв,
    преобразуйте строку в строчные.

Например:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

Больше примеров в тестовых заданиях. Удачи! 
"""
import unittest
from typing import Any, Callable, Tuple


def one_register(s: str) -> str:
    """
    Делает строку одного регистра.
    """
    return s.lower() if sum(x.islower() for x in s) >= len(s) / 2 else s.upper()


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(one_register, (
        ("code", "code"),
        ("CODe", "CODE"),
        ("COde", "code"),
        ("Code", "code"),
    ))
