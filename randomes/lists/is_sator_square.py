"""
Открытие

Однажды, когда фермер Арепо усердно трудился над обработкой земли, он обнаружил поле,
усеянное странными каменными табличками. Заметив, что на них высечены буквы в квадратном порядке,
он благоразумно сохранил их на случай, если какие-нибудь окажутся особенными.
Ваше задание

Пожалуйста, помогите фермеру Арепо, проверив каждую таблетку, чтобы убедиться,
что она образует корректный квадрат Сатора !
[квадрат сатора]
Площадь

Это двумерный палиндром, составленный из слов одинаковой длины,
которые можно читать четырьмя разными способами:

    1)    left-to-right    (across)
    2)    top-to-bottom    (down)
    3)    bottom-to-top    (up)
    4)    right-to-left    (reverse)

Пример

Рассмотрим этот квадрат:

    B A T S
    A B U T
    T U B A
    S T A B

Вот четыре способа, которыми слово (в данном случае) "TUBA") можно прочитать:

 вниз
                          ↓
           BATSBA  T  SB  A  TSBATS
           АБУТАБ  У  ТА  Б  УТ  АБУТ  ← реверс
  поперек →  ТУБА  ТУ  Б  АТ  У  БАТУБА
           СТАБСТ  А  БС  Т  АБСТАБ
                                   ↑
                                   вверх
 

ВАЖНЫЙ:

    В trueНа площади Сатор все слова можно прочитать всеми четырьмя способами.
    Если возникнут какие-либо отклонения, это будет falseсчитать его квадратом Сатора.

Некоторые подробности

    Размеры планшета (квадратной формы) варьируются от... 2x2 к 33x33инклюзивный
    Все используемые символы будут заглавными буквами алфавита.
    Нет необходимости проверять какие-либо входные данные.

Вход

    N x N (квадратная) двумерная матрица из заглавных букв

Выход

    логический true или falseявляется ли планшет Sator Square или нет.
"""
import unittest
from typing import Any, Callable, List, Tuple


def is_sator_square(tablet: List[List[str]]) -> bool:
    """
    Проверяет является ли матрица квадратом Сатора.
    """
    data = {}
    for tab in (map(tuple, tablet), zip(*tablet)):
        for line in set(tab):
            for i in range(2):
                x = line[::-i or 1]
                data[x] = data.get(x, 0) + 1
    return 4 in data.values() and next((False for x in data.values() if x not in (1, 4)), True)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(is_sator_square, (
        (
            [['T', 'E', 'N'],
             ['E', 'Y', 'E'],
             ['N', 'E', 'T']],
            True,
        ),
        (
            [['N', 'O', 'T'],
             ['O', 'V', 'O'],
             ['N', 'O', 'T']],
            False,
        ),
        (
            [['B', 'A', 'T', 'S'],
             ['A', 'B', 'U', 'T'],
             ['T', 'U', 'B', 'A'],
             ['S', 'T', 'A', 'B']],
            True,
        ),
        (
            [['P', 'A', 'R', 'T'],
             ['A', 'G', 'A', 'R'],
             ['R', 'A', 'G', 'A'],
             ['T', 'R', 'A', 'M']],
            False,
        ),
        (
            [['S', 'A', 'T', 'O', 'R'],
             ['A', 'R', 'E', 'P', 'O'],
             ['T', 'E', 'N', 'E', 'T'],
             ['O', 'P', 'E', 'R', 'A'],
             ['R', 'O', 'T', 'A', 'S']],
            True,
        ),
        (
            [['S', 'A', 'L', 'A', 'S'],
             ['A', 'R', 'E', 'N', 'A'],
             ['L', 'E', 'V', 'E', 'L'],
             ['A', 'R', 'E', 'N', 'A'],
             ['S', 'A', 'L', 'A', 'S']],
            False,
        ),
    ))
