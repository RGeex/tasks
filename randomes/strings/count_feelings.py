"""
У вас есть два аргумента: string - строка случайных букв (только строчные) и
array- массив строк(чувств). Ваша задача — узнать, сколько конкретных чувств
содержится в array.

Например:

string -> 'yliausoenvjw'
array -> ['anger', 'awe', 'joy', 'love', 'grief']
output -> '3 feelings.' // 'awe', 'joy', 'love'


string -> 'griefgriefgrief'
array -> ['anger', 'awe', 'joy', 'love', 'grief']
output -> '1 feeling.' // 'grief'


string -> 'abcdkasdfvkadf'
array -> ['desire', 'joy', 'shame', 'longing', 'fear']
output -> '0 feelings.'

Если чувство можно сформировать один раз – плюс один к ответу.

Если чувство можно составить несколько раз из разных букв – плюс одна к ответу.

Каждая буква в stringучаствует в формировании всех чувств. 'angerw' -> 2
чувства: 'anger' и 'awe'.
"""


from collections import Counter


def count_feelings(st: str, arr: list[str]) -> str:
    """
    Определяет, сколько заданных чувств можно сформировать из предоствленного слова.
    """
    return f'{(x:=sum((Counter(x) & Counter(st)) == Counter(x) for x in arr))} {"feelings"[:-(x==1) or None]}.'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (('longi', ['anger', 'awe', 'joy', 'longing', 'grief']), '0 feelings.'),
        (('yliausoenvjw', ['anger', 'awe', 'joy', 'love', 'grief']), '3 feelings.'),
        (('angerw', ['anger', 'awe', 'joy', 'love', 'grief']), '2 feelings.'),
        (('griefgriefgrief', ['anger', 'awe', 'joy', 'love', 'grief']), '1 feeling.'),
        (('abcdkasdfvkadf', ['desire', 'joy', 'shame', 'longing', 'fear']), '0 feelings.'),
    )
    for key, val in data:
        assert count_feelings(*key) == val


if __name__ == '__main__':
    test()
