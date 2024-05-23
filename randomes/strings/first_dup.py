"""
Найдите первый символ, который повторяется в строке, и верните этот символ.

first_dup('tweet') => 't'
first_dup('like') => None

Это не то же самое, что найти символ, который повторяется первым.
В этом случае ввод «tweet» даст «e».

Другой пример:

В 'translator' тебе следует вернуться 't', нет 'a'.

v      v  
translator
  ^   ^

В то время как второй 'a' появляется перед вторым 't', первый 't'
это перед первым 'a'.
"""


def first_dup(s: str) -> str | None:
    """
    Поиск первого символа дублирующегося в строке.
    """
    return next((x for i, x in enumerate(s, 1) if x in s[i:]), None)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('tweet', 't'),
        ('Ode to Joy', ' '),
        ('ode to joy', 'o'),
        ('bar', None),
        ('123123', '1'),
        ('!@#$!@#$', '!'),
        ('1a2b3a3c', 'a'),
    )
    for key, val in data:
        assert first_dup(key) == val


if __name__ == '__main__':
    test()
