"""
Телефон президента сломан

Он не очень счастлив.

Единственные буквы, которые все еще работают, — это прописные.
E, F, I, R, U, Y.

Гневный твит отправляется в отдел, отвечающий за обслуживание президентских
телефонов.
Задача сказала

Расшифруйте твит, найдя слова с известными значениями.

    FIRE = «Вы уволены!»
    FURY = «Я в ярости».

Если известные слова не найдены или встречаются неожиданные буквы, то это
должен быть «Фейковый твит».
Примечания

    Твит читается слева направо.
    Любые буквы, не составляющие слова FIRE или FURY просто игнорируются
    Если несколько одинаковых слов встречаются подряд, применяются правила
    множественного числа:
    
    FIRE x 1 = "You are fired!"
    FIRE x 2 = "You and you are fired!"
    FIRE x 3 = "You and you and you are fired!"
    etc...
    FURY x 1 = "I am furious."
    FURY x 2 = "I am really furious."
    FURY x 3 = "I am really really furious."
    etc...

Examples

    ex1. FURYYYFIREYYFIRE = "I am furious. You and you are fired!"
    ex2. FIREYYFURYYFURYYFURRYFIRE = "You are fired! I am really furious. You are fired!"
    ex3. FYRYFIRUFIRUFURE = "Fake tweet."

"""


import re
from itertools import groupby as gb


def fire_and_fury(s: str) -> str:
    """
    Расшифровывает послание, переданное в строке.
    """
    x, s = {'FURY': (('I am ', 'furious.'), 'really '), 'FIRE': (('You ', 'are fired!'), 'and you ')}, ['', s][not set(s) - set('EFIRUY')]
    return ' '.join([f'{x[a][1] * (len(list(b)) - 1)}'.join(x[a][0]) for a, b in gb(re.findall('|'.join(x), s))]) or 'Fake tweet.'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("FYRYFIRUFIRUFURE", "Fake tweet."),
        ("FURYYYFIREYYFIRE", "I am furious. You and you are fired!"),
        ("FIREYYFURYYFURYYFURRYFIRE", "You are fired! I am really furious. You are fired!"),
    )
    for key, val in data:
        assert fire_and_fury(key) == val


if __name__ == '__main__':
    test()
