"""
На заводе принтер печатает этикетки для коробок. Для одного вида коробок.
Принтер должен использовать цвета, которые, для простоты, названы буквами из a to m.

Цвета, используемые принтером: записано в управляющей строке. Например,
"хорошая" управляющая строка будет выглядеть так: aaabbbbhaijjjmЭто означает,
что принтер использовал три раза цвет А, четыре раза цвет b, затем один раз цвет h,
затем один раз цвет a...

Иногда возникают проблемы: нехватка цветов, технические неполадки и "плохое качество".
генерируется управляющая строка, например: aaaxbbbbyyhwawiwjjjwwmс письмами не от a to m.

Вам нужно написать функцию. printer_errorкоторый, получив строку,
вернет Показатель ошибок принтера в виде строки, представляющей рациональное число,
числитель которого — это количество ошибок, а знаменатель — длина управляющей строки.
Не упрощайте эту дробь до более простого выражения.

Строка имеет длину, большую или равную единице, и содержит только буквы. от aк z.
Примеры:

s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"

"""
import unittest
from typing import Any, Callable, Tuple


def printer_error(s: str) -> str:
    """
    Определяет кол-во ошибок в управляющей строке.
    """
    return f"{len(s.translate(str.maketrans('', '', 'abcdefghijklm')))}/{len(s)}"


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(printer_error, (
        ("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz", "3/56"),
        ("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz", "6/60"),
        ("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu" , "11/65"),
    ))
