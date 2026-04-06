"""
В этом задании вам нужно будет написать функцию, которая принимает массив строк и возвращает строку,
которая является либо 'naughty' или 'nice'. Строки, начинающиеся с букв b, f, или k являются
naughtyСтроки, начинающиеся с букв g, s, или n являются nice Другие струны не являются ни
непослушными, ни послушными.

Если количество плохих и хороших поступков одинаково, вернитесь. 'naughty'

Примеры:

bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
whatListAmIOn(bad_actions)
#-> 'naughty'
good_actions = ['got someone a new car', 'saved a man from drowning', 'never got into a fight']
what_list_am_i_on(good_actions)
#-> 'nice'
actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']
what_list_am_i_on(actions)
#-> 'naughty'

"""
import unittest
from typing import Any, Callable, List, Tuple


def what_list_am_i_on(actions: List[str]) -> str:
    """
    Определяет является ли список строк хорошим или плохим.
    """
    return ['naughty', 'nice'][sum(x[0] in 'bfk' or x[0] in 'gsn' and -1 for x in actions) < 0]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(what_list_am_i_on, (
        (['broke someone\'s window', 'fought over a toaster', 'killed a bug'], 'naughty'),
        (['got someone a new car', 'saved a man from drowning', 'never got into a fight'], 'nice'),
        (['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes'], 'naughty'),
    ))
