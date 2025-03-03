"""
Задача

В качестве входных данных вы получите строку, состоящую из строчных, прописных
букв и цифр. Ваша задача — вернуть эту строку в виде блоков, разделенных тире
( "-"). Элементы блока должны быть отсортированы в соответствии с иерархией,
указанной ниже, и каждый блок не может содержать несколько экземпляров одного
и того же символа. Элементы следует помещать в первый подходящий блок.

Иерархия такая:

    строчные буквы ( a - z), в алфавитном порядке
    заглавные буквы ( A - Z), в алфавитном порядке
    цифры ( 0 - 9), в порядке возрастания

Примеры

    "21AxBz" -> "xzAB12" - поскольку входные данные не содержат повторяющихся
    символов, вам понадобится всего 1 блок
    "abacad" -> "abcd-a-a" - символ «а» повторяется 3 раза, следовательно
    необходимо 3 блока
    "" -> "" - пустой ввод должен привести к пустому выводу
    "hbh420sUUW222IWOxndjn93cdop69NICEep832" ->
    "bcdehjnopsxCEINOUW0234689-dhnpIUW239-2-2-2" - более сложный пример
"""


from collections import Counter
from itertools import zip_longest as zl


def blocks(s: str) -> str:
    """
    Сортирует и форматирует строку заданным образом.
    """
    return '-'.join([''.join(sorted(x, key=lambda x: ({x.isupper():1, x.isdigit(): 2}.get(1, 0), x))) for x in zl(*[[w] * x for w, x in Counter(s).items()], fillvalue='')])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("21AxBz", "xzAB12"),
        ("abacad", "abcd-a-a"),
        ("", ""),
    )
    for key, val in data:
        assert blocks(key) == val


if __name__ == '__main__':
    test()
