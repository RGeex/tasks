"""
Для участия в ничьей призов каждый дает свое первое имя.

Каждая буква первого имени имеет ценность, которая является его рангом в английском алфавите.
A и a иметь звание 1, B и b классифицировать 2 и так далее.

Длина этих рангов , первого имени добавлена ​​к сумме следовательно, число som.

Массив случайных весов связан с первыми и каждым som умножается на соответствующий вес, чтобы
получить то, что они называют winning number.
Пример:

names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
weights: [1, 4, 4, 5, 2, 1]

PauL -> som = length of firstname + 16 + 1 + 21 + 12 = 4 + 50 -> 54
The *weight* associated with PauL is 2 so PauL's *winning number* is 54 * 2 = 108.

Теперь можно сортировать первые имена в уменьшения порядке winning numbersПолем Когда два человека
имеют одинаковое winning number Сортировать их в алфавитном порядке по их первым именам.
Задача:

    параметры: st строка первых имен, we множество весов, n ранга

    Возврат: первое название участника, чей ранг n (Ранги пронумерованы от 1)

Пример:

names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
weights: [1, 4, 4, 5, 2, 1]
n: 4

The function should return: "PauL"

Примечания:

    Массив веса, по крайней мере, столько же, сколько и имен, он может быть длиннее.

    Если st пустое возвращение "нет участников".

    Если n больше, чем количество участников, то возвращайте «недостаточно участников».

    См. Примеры тестовые случаи для получения дополнительных примеров.
"""
import typing
import unittest
from string import ascii_lowercase as abc


def rank(st: str, we: list[int], n: int) -> str:
    """
    Поиск заданного ранга участника.
    """
    if not st:
        return 'No participants'
    if len(st.split(',')) < n:
        return 'Not enough participants'
    return sorted(zip(st.split(','), we), key=lambda x: (-((sum(map(f'_{abc}'.index, x[0].lower())) + len(x[0])) * x[1]), x[0]))[n - 1][0]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(rank, (
        (("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4), "Benjamin"),
        (("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1, 3, 5, 5, 3, 6], 2), "Matthew"),
        (("Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth", [3, 1, 4, 4, 3, 2], 4), "Abigail"),
        (("Lagon,Lily", [1, 5], 2), "Lagon"),
    ))
