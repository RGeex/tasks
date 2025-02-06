"""
Королевская домохозяйство открывает новую вакансию микроволновой печи, которая нагревает посуду для
королевы Елизаветы II. Все кандидаты должны пройти несколько очень сложных испытаний и обучения в
учебном лагере. Удачи, наберетель!
Тест на сенсорную панель.

На микроволновке максимальное число, в которое вы можете войти в течение нескольких минут или
секунд, это 99Полем Следовательно, время может быть представлено двумя способами:

    Используя стандартный метод, где секунды поднимаются до 59 только,
    Используя альтернативный метод, где секунды могут подняться до 99 Так же, как минуты.

Хорошая микроволновая горничная не может тратить свое время на то, что она без необходимости
перемещать пальцем от одной кнопки к другой, чтобы установить таймер.

Учитывая время, необходимое для того, чтобы нагреть пищу за считанные секунды, вы должны вернуть
цепочку цифр, которые горничная должна вводить, используя один из вышеупомянутых методов, так что
количество различных последовательных цифр было минимальным. Если количество различий одинаково,
выберите более короткую строку. Если обе строки тоже имеют одинаковую длину, используйте стандартный
метод.
Пример 1:

input = 71
method 1: "111" (1 minute and 11 seconds)
method 2: "71" (0 minutes and 71 seconds)
return "111" since it has fewer different consecutive digits

Пример 2:

input = 72
method 1: "112" (1 minute and 12 seconds)
method 2: "72" (0 minutes and 72 seconds)
return "72" since the number of different consecutive digits is the same but "72" has fewer digits
than "112"

Пример 3:

input = 3690
method 1: "6130" (61 minutes and 30 seconds)
method 2: "6090" (60 minutes and 90 seconds)
return "6130" (the standard way) since both the number of different consecutive digits and the
number of digits are the same
"""
import typing
import unittest
from itertools import groupby


def get_best_combination(n: int) -> str:
    """
    Поиск минимального кол-ва цифр для программирования продолжительности использования СВЧ.
    """
    x = divmod(n, 60)
    x = [''.join([f'{x:0>2}' for x in x]).lstrip('0') for x in (x, [x, (x[0] - 1, x[1] + 60)][x[1] + 40 < 100])]
    return x[min([([x for x, _ in groupby(x)], x, i) for i, x in enumerate(x)], key=lambda x: (len(x[0]), len(x[1])))[2]]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(get_best_combination, (
        (6, "6"),
        (33, "33"),
        (60, "60"),
        (71, "111"),
        (72, "72"),
        (90, "90"),
        (99, "99"),
        (115, "155"),
        (121, "201"),
        (180, "300"),
        (273, "433"),
        (279, "399"),
        (3690, "6130"),
        (4697, "7777"),
        (5255, "8735"),
    ))
