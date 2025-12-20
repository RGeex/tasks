"""
Вам дали старую книгу, в которой, к сожалению, несколько страниц расположены неправильно. К счастью,
ваш компьютер хранит список всех номеров страниц в порядке их расположения. 1 к n.

Вам предоставлен массив чисел, и вы должны вернуть массив со всеми номерами страниц,
которые указаны неверно. Неправильные номера страниц могут располагаться рядом друг с другом.
Возможны повторяющиеся неправильные номера страниц.

Пример:

Given: list = [1,2,10,3,4,5,8,6,7]
Return: [10,8]

В вашем списке возвращенных пользователей неверные номера страниц должны быть указаны в том порядке,
в котором они были найдены.
"""
import unittest
from typing import Any, Callable, Tuple, List


def find_page_number(pages: List[int]) -> List[int]:
    """
    Поиск чисел в списке стоящих не по порядку на чиная с 1.
    """
    res: List[int] = []
    for i, page in enumerate(pages, 1):
        if i - len(res) != page:
            res.append(page)
    return res


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_page_number, (
        ([1, 2, 10, 3, 4, 5, 8, 6, 7], [10, 8]),
        ([1, 2, 3, 4, 50, 5, 6, 7, 51, 8, 40, 9], [50, 51, 40]),
        ([1, 2, 3000, 3, 4, 5, 8, 6, 7, 8, 100, 9, 40, 10, 11, 13], [3000, 8, 100, 40, 13]),
        ([1, 2, 3, 4, 50, 5, 6, 7, 51, 8, 9], [50, 51]),
        ([4, 1, 2, 3, 3, 4, 26, 5, 6, 2, 7], [4, 3, 26, 2]),
    ))
