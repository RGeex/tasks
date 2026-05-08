"""
Краткий

Иногда нам нужна информация о списках/массивах, с которыми мы работаем.
В этом задании вам придётся написать такую ​​функцию.
Ваша функция должна предоставлять следующую информацию:

    Длина массива
    Количество целых элементов в массиве
    Количество элементов с плавающей запятой в массиве
    Количество строковых символов в массиве
    Количество пробельных элементов в массиве

Информация будет предоставляться в виде массивов, элементы которых являются элементами другого
массива. Как показано ниже:

Output array = [[array length],[no of integer items],[no of float items],
[no of string chars items],[no of whitespace items]]
Повышенная сложность

Если количество элементов в массиве равно нулю, вам придётся заменить его значением None/nil/null
(в зависимости от языка программирования). И, конечно же, если массив пуст,
верните 'В массиве ничего нет!' . Для простоты предположим, что вложенных структур нет.
Выход ====== Если у вас голова кружится (шутка!), то эти примеры вам помогут.

   
array_info([1,2,3.33,4,5.01,'bass','kick',' '])--------->[[8],[3],[2],[2],[1]]    
array_info([0.001,2,' '])------------------------------>[[3],[1],[1],[None],[1]]   
array_info([])----------------------------------------->'Nothing in the array!'
array_info([' '])-------------------------------------->[[1],[None],[None],[None],[1]]


Примечания

Входными данными всегда будут массивы/списки. Поэтому проверять входные данные не нужно.
Намекать ==== Смотрите теги!!!
Итак, приступим!
"""
import unittest
from typing import Any, Callable, List, Tuple


def array_info(x: List[int | float | str]) -> List[List[int]] | str:
    """
    Предоставляет данные о переданном списке.
    """
    return [[len(x)]] + [[sum(z) or None] for z in zip(*[{int: [1, 0, 0, 0], float: [0, 1, 0, 0], str: [0, 0, e != ' ', e == ' ']}[type(e)] for e in x])] if x else 'Nothing in the array!'


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(array_info, (
        ([1, 2, 3.33, 4, 5.01, 'bass', 'kick', ' '], [[8], [3], [2], [2], [1]]),
        ([0.001, 2, ' '], [[3], [1], [1], [None], [1]]),
        ([], 'Nothing in the array!'),
        ([' '], [[1], [None], [None], [None], [1]]),
    ))
