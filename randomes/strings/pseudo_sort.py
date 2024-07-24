"""
Учитывая стандартное английское предложение, переданное в виде строки,
напишите метод, который будет возвращать предложение, состоящее из тех же
слов, но отсортированное по первой букве. Однако метод сортировки имеет
особенность:

    Все слова, начинающиеся со строчной буквы, должны находиться в начале
    отсортированного предложения и отсортироваться по возрастанию.
    Все слова, начинающиеся с заглавной буквы, должны идти после этого и
    сортироваться по убыванию.

Если слово встречается в предложении несколько раз, оно должно быть возвращено
несколько раз в отсортированном предложении. Любые знаки препинания должны быть
отброшены.
Пример

Например, учитывая входную строку "Land of the Old Thirteen! Massachusetts
land! land of Vermont and Connecticut!", ваш метод должен вернуть результат
"and land land of of the Vermont Thirteen Old Massachusetts Land Connecticut".
Строчные буквы сортируются a -> l -> l -> o -> o -> t и заглавные буквы
сортируются V -> T -> O -> M -> L -> C.
"""


import re


def pseudo_sort(s: str) -> str:
    """
    Сортирует строку группами слов начинающихся с заглавных и строчных букв отдельно
    друг от друга в обратной и прямой сортировке соответственно. Сначала строчные.
    """
    return ' '.join([w for x in [sorted(re.findall(rf'\b[{x}]\w*', s), reverse=i) for i, x in enumerate(('a-z', 'A-Z'))] for w in x])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("I, habitan of the Alleghanies, treating of him as he is in himself in his own rights", "as habitan he him himself his in in is of of own rights the treating I Alleghanies"),
        ("take up the task eternal, and the burden and the lesson", "and and burden eternal lesson take task the the the up"),
        ("Land of the Old Thirteen! Massachusetts land! land of Vermont and Connecticut!", "and land land of of the Vermont Thirteen Old Massachusetts Land Connecticut"),
        ("Pioneers, O Pioneers!", "Pioneers Pioneers O"),
    )
    for key, val in data:
        assert pseudo_sort(key) == val


if __name__ == '__main__':
    test()
