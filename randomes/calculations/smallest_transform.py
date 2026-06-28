"""
Задача

Вам дано положительное целое число. nВаша задача — преобразовать это число в другое число,
у которого все цифры идентичны , минимизируя при этом количество изменений .
Каждый шаг преобразования включает в себя увеличение или уменьшение цифры на единицу.

Например, если заданное число равно 399 , его можно преобразовать в 999 за 6 шагов,
увеличив первую цифру на 6. Преобразование в любое другое число с теми же цифрами займет более 6 шагов.

Если nЕсли элемент уже состоит из одинаковых цифр, функция должна вернуть 0
Поскольку никаких изменений не требуется. Обертывание,
то есть перемещение из 9 to 0 или 0 to 9За один шаг это недопустимо.
Примеры

399 ➞ 6
# 399 transformed to 999 in 6 steps.

1234 ➞ 4
# there are two possible transformations with identical digits: 2222 and 3333. 
# The function should return 4 as it takes 4 steps to transform 1234 into either 2222 or 3333. 
# The steps involved could be either incrementing or decrementing a digit by one at a time until all digits become the same.

900 ➞ 9
# 900 can be transformed to 000 after decrementing first digit 9 times to `0`.

7777 ➞ 0

"""
import unittest
from typing import Any, Callable, Tuple


def smallest_transform(num: int) -> int:
    """
    Определяет мин кол-во изменений для приведения числа к единым цифрам.
    """
    nums = sorted(map(int, str(num)))
    return sum(abs(n - nums[len(nums) // 2]) for n in nums)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(smallest_transform, (
        (399, 6),
        (1234, 4),
        (153, 4),
        (33338, 5),
        (7777, 0),
        (977, 2),
        (589, 4),
        (900, 9),
        (8005, 13),
        (65251, 8),
        (635299, 14),
    ))
