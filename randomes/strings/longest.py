"""
Найдите самую длинную подстроку в алфавитном порядке.

Пример: самая длинная алфавитная подстрока в "asdfaaaabbbbcttavvfffffdf"
является "aaaabbbbctt".

Есть тесты со строками до 10 000 символов, поэтому ваш код должен быть
эффективным.

Ввод будет состоять только из символов нижнего регистра и иметь длину
не менее одной буквы.

Если существует несколько решений, верните то, которое появится первым.
"""


def longest(s: str, x: int=0) -> str:
    """
    Поиск максимальной подстроки в строке, являющейся последовательными буквами
    алфавита.
    """
    return max([s[x:(x:=i)] for i, (a, b) in enumerate(zip(s, s[1:] + '@'), 1) if b < a], key=len)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('asd', 'as'),
        ('nab', 'ab'),
        ('abcdeapbcdef', 'abcde'),
        ('asdfaaaabbbbcttavvfffffdf', 'aaaabbbbctt'),
        ('asdfbyfgiklag', 'fgikl'),
        ('z', 'z'),
        ('zyba', 'z'),
    )
    for key, val in data:
        assert longest(key) == val


if __name__ == '__main__':
    test()
