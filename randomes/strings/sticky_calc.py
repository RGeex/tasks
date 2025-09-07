"""
Фрэнк только что купил новый калькулятор. Но это не обычный калькулятор. Это «липкий калькулятор» .

Всякий раз, когда вы складываете, вычитаете, умножаете или делите два числа, два числа сначала соединяются:

Например:

50 + 12 becomes 5012

и далее операция проводится как обычно:

(5012) + 12 = 5024

Задача

Ваша задача — создать функцию, которая принимает 3 параметра:

stickyCalc(operation, val1, val2)

который работает так же, как липкий калькулятор Фрэнка
Некоторые примеры

stickyCalc('+', 50, 12)     // Output: (5012 + 12) = 5024
stickyCalc('-', 7, 5)       // Output: (75 - 5) = 70
stickyCalc('*', 13, 20)     // Output: (1320 * 20 ) = 26400
stickyCalc('/', 10, 10)     // Output: (1010 / 10) = 101

Примечание

    Калькулятор работает только с положительными целыми числами.
    Калькулятор округляет любое нецелое число перед выполнением операции.
    Калькулятор округляет любой вывод до ближайшего целого числа.

Например:

stickyCalc('/', 12.1, 6.8), 18);   

12,1 и 6,8 округляются до 12 и 7 соответственно и «склеиваются», образуя 127.

Хотя 127 / 7 = 18,1428 , вместо этого выводится 18.

"""
import typing
import unittest


def sticky_calc(operation: str, val1: int | float, val2: int | float) -> int:
    """
    Производит вычисления в строке.
    """
    return round(eval(operation.join((str(round(val1)) + (x := str(round(val2))), x))))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sticky_calc, (
        (('+', 4, 7), 54),
        (('-', 15, 10), 1500),
        (('*', 5, 5), 275),
        (('/', 10, 7), 15),
        (('+', 4.2, 7), 54),
        (('+', 4.7, 7.2), 64),
        (('/', 10, 7), 15),
        (('/', 51, 63), 82),
    ))
