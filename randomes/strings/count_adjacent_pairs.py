"""
Знаете, как иногда два раза пишешь одно и то же слово в предложении,
а потом не замечаешь, что это произошло? Например, вы отвлеклись на
секунду. Вы заметили, что в первом предложении этого описания слово
«the» удваивается?

Как вы можете видеть, эти ошибки нелегко обнаружить, особенно если
слова различаются по регистру, например «as» в начале этого предложения.

Напишите функцию, которая подсчитывает количество разделов, повторяющих
одно и то же слово (без учета регистра). Появление двух или более
одинаковых слов подряд друг за другом считается за одно.
Примеры

"dog cat"                  -->  0
"dog DOG cat"              -->  1
"apple dog cat"            -->  0
"pineapple apple dog cat"  -->  0
"apple apple dog cat"      -->  1
"apple dog apple dog cat"  -->  0
"dog dog DOG dog dog dog"  -->  1
"dog dog dog dog cat cat"  -->  2
"cat cat dog dog cat cat"  -->  3
"""


from itertools import groupby as gb


def count_adjacent_pairs(s: str) -> int:
    """
    Подсчитывает кол-во повторений одинаковых слов, независимо от регистра,
    идущих друг за другом.
    """ 
    return len([a for a, b in gb(s.lower().split()) if len(list(b)) > 1])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('', 0),
        ('orange Orange kiwi pineapple apple', 1),
        ('banana banana banana', 1),
        ('banana banana banana terracotta banana terracotta terracotta pie!', 2),
        ('pineapple apple', 0),
    )
    for key, val in data:
        assert count_adjacent_pairs(key) == val


if __name__ == '__main__':
    test()
