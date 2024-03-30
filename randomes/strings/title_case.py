"""
Строка считается написанной в заглавном регистре, если каждое слово в строке либо (а) написано с
заглавной буквы (т. е. только первая буква слова находится в верхнем регистре), либо (б) считается
исключением и полностью помещается в регистр. в нижнем регистре, если только это не первое слово,
которое всегда пишется с заглавной буквы.

Напишите функцию, которая преобразует строку в регистр заголовка с учетом необязательного списка
исключений (второстепенных слов). Список второстепенных слов будет представлен в виде строки,
где каждое слово будет отделено пробелом. Ваша функция должна игнорировать регистр второстепенных
слов — она должна вести себя таким же образом, даже если регистр второстепенных слов изменяется.
Аргументы (Haskell)

    Первый аргумент : список второстепенных слов, разделенных пробелами, которые всегда должны быть
    в нижнем регистре, за исключением первого слова в строке.
    Второй аргумент : исходная строка, которую нужно преобразовать.

Аргументы (другие языки)

    Первый аргумент (обязательный) : исходная строка, подлежащая преобразованию.
    Второй аргумент (необязательный) : список второстепенных слов, разделенных пробелами, которые
    всегда должны быть в нижнем регистре, за исключением первого слова в строке. Тесты
    JavaScript/CoffeeScript пройдут успешно. undefinedкогда этот аргумент не используется.

Пример

title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'

"""

def title_case(s1: str, s2: str='') -> str:
    """
    Каждое слово в заданной строке начинается с заглавной буквы, кроме указанных слов, кроме начала предложения.
    """
    return ' '.join(x if i and x in s2.lower().split() else x.title() for i, x in enumerate(s1.lower().split()))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (('',), ''),
        (('the quick brown fox',), 'The Quick Brown Fox'),
        (('a clash of KINGS', 'a an the of'), 'A Clash of Kings'),
        (('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows'),
    )
    for key, val in data:
        assert title_case(*key) == val


if __name__ == '__main__':
    test()