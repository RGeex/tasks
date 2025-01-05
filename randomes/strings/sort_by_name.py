"""
Эй, ты !

Отсортируйте эти целые числа для меня...

По имени...

Сделайте это сейчас!
Вход

    Диапазон 0- 999

    Могут быть дубликаты

    Массив может быть пустым

Пример

    Ввод: 1, 2, 3, 4
    Соответствующие имена: «один», «два», «три», «четыре».
    Сортировка по имени: «четыре», «один», «три», «два».
    Выход: 4, 1, 3, 2

Примечания

    Не объединяйте слова:
        например, 99 может быть «девяносто девять» или «девяносто девять»; но не «девяносто девять»
        например, 101 может быть «сто один» или «сто один»; но не "сто"
    Не беспокойтесь о правилах форматирования, потому что если правила применяются последовательно,
    это все равно не имеет никакого эффекта:
        например, «сто один», «сто два»; тот же порядок, что и «сто один » , «сто два »
        например, «девяносто восемь», «девяносто девять»; того же порядка, что и «девяносто восемь»,
        «девяносто девять».
"""
import typing


def int_to_word(num: int) -> str:
    """
    Number to word, from [0 - 999].
    """
    w1 = 'one two three four five six seven eight nine ' +\
         'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'
    w2 = 'twenty thirty forty fifty sixty seventy eighty ninety'

    db1, db2 = [{str(i): k for i, k in enumerate(x.split(), i)} for i, x in enumerate((w1, w2), 1)]

    st, res = str(num), []
    n1, n2 = st[-3:-2], st[-2:]

    if x := db1.get(n1):
        res.append(f'{x} hundred')

    if x := db1.get(n2):
        res.append(x)
    else:
        if x := db2.get(n2[:1]):
            res.append(x)
        if x := db1.get(n2[1:]):
            res.append(x)

    return [' '.join(res), 'zero'][not num]


def sort_by_name(arr: list[int]) -> list[int]:
    """
    Сортирует список чисел по написанию их слов.
    """
    return sorted(arr, key=int_to_word)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""
    import unittest

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_by_name, (
        ([8, 8, 9, 9, 10, 10], [8, 8, 9, 9, 10, 10]),
        ([1, 2, 3, 4], [4, 1, 3, 2]),
        ([9, 99, 999], [9, 999, 99]),
        ([0, 1, 2, 3], [1, 3, 2, 0]),
        ([], []),
        ([8, 8, 9, 9, 10, 10], [8, 8, 9, 9, 10, 10]),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 20, 2, 0]),
        ([99, 100, 200, 300, 999], [999, 99, 100, 300, 200]),
    ))
