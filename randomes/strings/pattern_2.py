"""
Задача:

Вам необходимо написать функцию, которая создает следующий шаблон (см. примеры)
до желаемого количества строк.

Если аргумент заключается в следующем: 0или отрицательное целое число, тогда оно
должно вернуть ""то есть пустая строка.

Примеры:

Argument: 9

123456789
234567891
345678912
456789123
567891234
678912345
789123456
891234567
912345678

Argument: 11

1234567891011
2345678910111
3456789101112
4567891011123
5678910111234
6789101112345
7891011123456
8910111234567
9101112345678
1011123456789
1112345678910

Примечание: В шаблоне нет пробелов.

Подсказка: Используйте \nв строке для перехода на следующую строку


"""
import unittest
from typing import Any, Callable, Tuple


def pattern(n: int) -> str:
    """
    Создает строки по шаблоную
    """
    return '\n'.join(''.join(list(map(str, range(x, n + 1))) + list(map(str, range(1, x))))  for x in range(1, n + 1)) if n > 0 else ''


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(pattern, (
        (7, "1234567\n2345671\n3456712\n4567123\n5671234\n6712345\n7123456"),
        (1, "1"),
        (4, "1234\n2341\n3412\n4123"),
        (0, ""),
        (-25, ""),
        (11,
            "1234567891011\n"
            "2345678910111\n"
            "3456789101112\n"
            "4567891011123\n"
            "5678910111234\n"
            "6789101112345\n"
            "7891011123456\n"
            "8910111234567\n"
            "9101112345678\n"
            "1011123456789\n"
            "1112345678910"
         ),
    ))
