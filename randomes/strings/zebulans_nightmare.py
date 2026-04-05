"""
Зебулан усердно трудился, чтобы написать весь свой код на Python в строгом соответствии с
правилами PEP8. В этом задании вы — озорной хакер, который решил саботировать весь его хороший код.

Ваша задача — взять имена функций, совместимые с PEP8, и преобразовать их в формат camelCase.
Например:

"camel_case" --> "camelCase"
"zebulans_nightmare" --> "zebulansNightmare"
"get_string" --> "getString"
"convert_to_uppercase" --> "convertToUppercase"
"main" --> "main"

"""
import unittest
from typing import Any, Callable, Tuple


def zebulans_nightmare(function: str) -> str:
    """
    Преобразование строки в CamelCase.
    """
    return ('x' + function).replace('_', ' ').title().replace(' ', '')[1:]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(zebulans_nightmare, (
        ('camel_case', 'camelCase'),
        ('zebulans_nightmare', 'zebulansNightmare'),
        ('get_string', 'getString'),
        ('convert_to_uppercase', 'convertToUppercase'),
    ))
