"""
ISBN

ISBN (международный стандартный номер книги) — это ten digitКод, который однозначно идентифицирует книгу.
Первые девять цифр представляют книгу, а последняя цифра используется для проверки правильности ISBN.
Для проверки ISBN необходимо рассчитать 10умножить на первую цифру, плюс 9умножить на вторую цифру, плюс 8раз по третьему...
и так до тех пор, пока не добавите 1умножить на последнюю цифру. Если итоговое число не даёт остатка при делении на 11код
является действительным ISBN.

Например 0201103311является действительным ISBN, поскольку 10*0 + 9*2 + 8*0 + 7*1 + 6*1 + 5*0 + 4*3 + 3*3 + 2*1 + 1*1 = 55.

Каждая из первых девяти цифр может принимать значение между 0 и 9. Иногда необходимо сделать последнюю цифру равной десяти;
это делается путем записи последней цифры в виде X. Например, 156881111X.

Напишите программу, которая считывает код ISBN (который всегда будет действителен) с одной пропущенной цифрой, отмеченной ?,
cи выводит правильное значение для пропущенной цифры.
Пример:

15688?111X => "1"
020161586? => "X"

Ввод/вывод

    [input]строка, представляющая 10-значный код ISBN 15688?111X
    [output]строка, представляющая пропущенную цифру '1'

"""
import typing
import unittest


def fix_code(isbn: str) -> str:
    """
    Определяет пропущенную цифру в ISBN коде.
    """
    res, x = 0, 0
    for i, n in enumerate(isbn[::-1], 1):
        res, x = res + int(n.replace('X', '10').replace('?', '0')) * i, [x, i][n == '?']
    return next((str(i) for i in range(10) if not (i * x + res) % 11), 'X')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(fix_code, (
        ("15688?111X", "1"),
        ("020161586?", "X"),
    ))
