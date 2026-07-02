"""
Макси — наибольшее число, которое можно получить, поменяв местами две цифры целого числа,
Минни — наименьшее число. Создайте функцию, которая принимает целое число и возвращает Макси и Минни.
Начальные нули не допускаются. Все тестовые случаи — положительные целые числа, состоящие из трех и более цифр.
Иногда перестановка цифр не требуется.
Примеры:

    swap(12340) → (42310,10342)
    swap(98761) → (98761,18769)>>Для Макси замена не требуется.
    swap(9000) → (9000,9000)>>Обмены не допускаются.
    swap(90888) → (98880,80889)



"""
import unittest
from typing import Any, Callable, Tuple


def swap(number: int) -> Tuple[int, int]:
    """
    Определяет максимальное и минимальное число получаемое при переставноки 2-х цифр числа.
    """
    nums = [list(str(number)) for _ in range(2)]
    for x in range(2):
        for i in range(len(nums[x])):
            m = min([n for n in nums[x][i:] if i or n != '0']) if x else max(nums[x][i:])
            if x and nums[x][i] > m or nums[x][i] < m:
                n = len(nums[x]) - 1 - nums[x][::-1].index(m)
                nums[x][i], nums[x][n] = nums[x][n], nums[x][i]
                break
    return tuple([int(''.join(x)) for x in nums])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(swap, (
        (231, (321, 132)),
        (11321, (31121, 11123)),
        (10000, (10000, 10000)),
        (98761, (98761, 18769)),
        (597202395684464, (997202355684464, 297205395684464)),
        (111090753368874, (911010753368874, 101091753368874)),
    ))
