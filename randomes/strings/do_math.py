"""
Ваша задача — написать функцию, которая получает в качестве единственного
аргумента строку, содержащую числа, разделенные одинарными пробелами.
Внутри каждого числа есть одна буква алфавита.

Example : "24z6 1x23 y369 89a 900b"

Как показано выше, эта буква алфавита может появляться в любом месте числа.
Вам нужно извлечь буквы и отсортировать числа по соответствующим буквам.

Example : "24z6 1x23 y369 89a 900b" will become 89 900 123 369 246
(ordered according to the alphabet letter)

Вот и наступает самая сложная часть: теперь вам нужно выполнить серию
вычислений над извлеченными вами числами.

    Последовательность вычислений такова: + - * /. Основные математические
    правила НЕ применяются, вы должны выполнять каждое вычисление именно в
    этом порядке.
    Это должно работать для любого размера отправленных чисел (после деления
    вернуться к сложению и т. д.).
    В случае повторяющихся букв алфавита их необходимо расположить по номеру,
    который появился первым во входной строке.
    Не забудьте также округлить окончательный ответ до ближайшего целого числа.

Examples :
"24z6 1x23 y369 89a 900b" = 89 + 900 - 123 * 369 / 246 = 1299
"24z6 1z23 y369 89z 900b" = 900 + 369 - 246 * 123 / 89 = 1414
"10a 90x 14b 78u 45a 7b 34y" = 10 + 45 - 14 * 7 / 78 + 90 - 34 = 60
"""


from itertools import cycle
from operator import add, sub, mul, truediv


def do_math(s: str) -> int:
    """
    Сортирует числа в строке по букве содержащийся в них.
    Затем циклически применяет операторы +-*/ к последующей паре чисел.
    """
    f = cycle([add, sub, mul, truediv])
    t, *x = [int(''.join(n for n in x if n.isdigit())) for x in sorted(s.split(), key=lambda x: next(w for w in x if w.isalpha()))]
    return round([t := next(f)(t, x.pop(0)) for _ in range(len(x))][-1] if x else t)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("24z6 1z23 y369 89z 900b",1414),
        ("24z6 1x23 y369 89a 900b",1299),
        ("10a 90x 14b 78u 45a 7b 34y",60),
        ("111a 222c 444y 777u 999a 888p",1459),
        ("1z 2t 3q 5x 6u 8a 7b",8),
    )
    for key, val in data:
        assert do_math(key) == val


if __name__ == '__main__':
    test()
