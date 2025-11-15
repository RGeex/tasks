"""
Не ставь мне пять!
В этом ката вы получаете начальный и конечный номера региона и должны вернуть
количество всех номеров, кроме номеров, содержащих цифру 5. Начальный и
конечный номера включаются в диапазон!

Примеры:

1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12
Результат может содержать пятёрки. ;-)
Начальное число всегда будет меньше конечного. Оба числа могут быть
отрицательными!

Мне очень интересно узнать ваши решения и как вы их решаете. Возможно,
кто-то из вас найдёт простое решение с точки зрения чистой математики.

Получайте удовольствие от написания кода и, пожалуйста, не забудьте
проголосовать и оценить этот ката! :-)
"""
import typing
import unittest


def dont_give_me_five(start: int, end: int) -> int:
    """
    Определяет кол-во чисел из диапазона, в которых нет цифры 5.
    """
    return len([x for x in range(start, end + 1) if '5' not in str(x)])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(dont_give_me_five, (
        ((1,9), 8),
        ((4,17), 12),
    ))
