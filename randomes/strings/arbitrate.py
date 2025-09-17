"""
Когда к одной шине подключено несколько ведущих устройств ( https://en.wikipedia.org/wiki/System_bus ),
необходимо провести арбитраж, чтобы выбрать, какое из них может иметь доступ к шине
(и «общаться» с ведомым устройством).

Мы реализуем здесь очень простую модель управления шиной. n, число,
представляющее количество ведущих устройств, подключенных к шине, и
фиксированный порядок приоритетов (первый ведущий имеет больший приоритет
доступа, чем второй и т. д.), задача состоит в том, чтобы выбрать выбранное ведущее устройство.
На практике вам дана строка inpдлины nпредставляющий nзапросы ведущих устройств на получение доступа к шине,
и вы должны вернуть строку, представляющую ведущих устройств, показывающую, какому (только одному) из них был
предоставлен доступ:

The string 1101 means that master 0, master 1 and master 3 have requested
access to the bus. 
Knowing that master 0 has the greatest priority, the output of the function
should be: 1000

Примеры

* arbitrate("001000101", 9) -> "001000000"

* arbitrate("000000101", 9) -> "000000100"

Примечания

    Полученная строка ( char* ) следует выделить в arbitrateфункция, и будет освобождена в тестах.

    nвсегда больше или равно 1.


"""
import typing
import unittest


def arbitrate(s: str, n: int) -> str:
    """
    Выводит заданное устройство, подключенное к шине.
    """
    return s[::-1].replace('1', '*', min(n, s.count('1')))[::-1].replace('*', '1', 1).replace('*', '0')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(arbitrate, (
        (("001000101", 9), "001000000"),
        (("000000101", 9), "000000100"),
        (("0000", 4), "0000"),
    ))
