
"""
Вы, наверное, знаете систему «лайков» из Facebook и других страниц.
Люди могут «лайкать» сообщения в блогах, изображения или другие элементы.
Мы хотим создать текст, который должен отображаться рядом с таким элементом.

Реализуйте функцию, которая принимает массив, содержащий имена людей, которым
понравился элемент.

Он должен возвращать отображаемый текст, как показано в примерах:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this
"""


def likes(names: list) -> str:
    """Распределение подсказок для лайков по шаблону."""
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this',
    }[min(4, n)].format(*names[:3], others=n-2)


def test() -> None:
    """Тестирование работы алгоритмов."""
    data1 = (
        [],
        ['Peter'],
        ['Jacob', 'Alex'],
        ['Max', 'John', 'Mark'],
        ['Alex', 'Jacob', 'Mark', 'Max'],
    )
    data2 = (
        'no one likes this',
        'Peter likes this',
        'Jacob and Alex like this',
        'Max, John and Mark like this',
        'Alex, Jacob and 2 others like this',
    )

    for v1, v2 in zip(data1, data2):
        assert likes(v1) == v2


if __name__ == '__main__':
    test()
