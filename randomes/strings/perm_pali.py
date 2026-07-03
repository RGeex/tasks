"""
Рассмотрим строку "adfa"и следующие правила:

а) каждый символ ДОЛЖЕН быть заменен либо на предыдущий, либо на следующий в алфавите.
б) «а» можно заменить только на "b" and "z" to "y".

Из нашей строки получаем:

"adfa" -> ["begb","beeb","bcgb","bceb"]

Here is another example: 
"bd" -> ["ae","ac","ce","cc"]

--We see that in each example, one of the outcomes is a palindrome. That is, "beeb" and "cc".

Вам будет предоставлена ​​строка в нижнем регистре, и ваша задача — вернуть её.
True если хотя бы один из результатов является палиндромом или False в противном случае.

Больше примеров в тестовых заданиях. Удачи!

"""
import unittest
from typing import Any, Callable, Tuple


def perm_pali(st: str) -> bool:
    """
    Определяет может ли слово после перестановки букв быть палиндромом.
    """
    lst = [{chr((lst := ord(s)) + [1, -1][lst > 97]), chr((lst := ord(s)) + [-1, 1][lst < 122])} for s in st]
    return all([a & b for a, b in zip(lst, lst[::-1])])


def perm_pali_2(st: str) -> bool:
    """
    Определяет может ли слово после перестановки букв быть палиндромом.
    """
    return all([abs(ord(a) - ord(b)) in [0, 2] for a, b in zip(st, st[::-1])])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(perm_pali, (
        ("abba", True),
        ("abaazaba", False),
        ("abccba", True),
        ("adfa", True),
        ("ae", False),
        ("abzy", False),
        ("ababbaba", True),
        ("sq", True),
        ("kxbkwgyydkcbtjcosgikfdyhuuprubpwthgflucpyylbofvqxkkvqthmdnywpaunfihvupbwpruwfybdmgeuocltdaidyyewmbzm", True),
    ))
    test(perm_pali_2, (
        ("abba", True),
        ("abaazaba", False),
        ("abccba", True),
        ("adfa", True),
        ("ae", False),
        ("abzy", False),
        ("ababbaba", True),
        ("sq", True),
        ("kxbkwgyydkcbtjcosgikfdyhuuprubpwthgflucpyylbofvqxkkvqthmdnywpaunfihvupbwpruwfybdmgeuocltdaidyyewmbzm", True),
    ))
