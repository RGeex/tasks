"""
У вас есть строка. Строка состоит из слов. Прежде чем слова могут быть восклицательными знаками !.
Также некоторые слова помечены как один набор квадратными скобками. [].
Ваша задача — разбить строку на отдельные слова и множества.
Набор не может содержаться в другом наборе.

Вход:
Строка со словами (разделенными пробелами), !и [].

Выход:
Массив с разделенными словами и множествами.

Примеры:

('Buy a !car [!red green !white] [cheap or !new]')  =>  ['Buy', 'a', '!car', '[!red green !white]', '[cheap or !new]']
('!Learning !javascript is [a joy]')                =>  ['!Learning', '!javascript', 'is', '[a joy]']
('[Cats and dogs] are !beautiful and [cute]')       =>  ['[Cats and dogs]', 'are', '!beautiful', 'and', '[cute]']
"""


import re


def clever_split(s: str) -> list:
    """
    Разбивает строку по пробелам, игнорируя выражения в квадратных скобках.
    """
    return [x for x in re.split(r'(\s|\[[^\]]*\])', s) if x and x != ' ']


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('Buy a !car [!red green !white] [cheap or !new]', [
            'Buy', 'a', '!car', '[!red green !white]', '[cheap or !new]']),
        ('!Learning !javascript is [a joy]', ['!Learning', '!javascript', 'is', '[a joy]']),
        ('[Cats and dogs] are !beautiful and [cute]', [
            '[Cats and dogs]', 'are', '!beautiful', 'and', '[cute]'])
    )

    for key, val in data:
        assert clever_split(key) == val


if __name__ == '__main__':
    test()
