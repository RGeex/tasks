"""
Вам дана входная строка.

Для каждого символа в строке, если это первый символ, замените его на «1»,
в противном случае замените на количество раз, которое вы его уже видели.
Примеры:

input   =  "Hello, World!"
result  =  "1112111121311"

input   =  "aaaaaaaaaaaa"
result  =  "123456789101112"

В строке могут быть символы, отличные от ASCII.
Обратите внимание на производительность.
"""


def numericals(s: str) -> str:
    """
    Заменяет символы строки на кол-во аналогичных символов,
    встречающихся с начала строки до текущего момента.
    """
    r, t = '', {}
    for x in s:
        t[x] = t.get(x, 0) + 1
        r += str(t[x])
    return r


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = ( 
        ("Hello, World!", "1112111121311"),
        ("Hello, World! It's me, JomoPipi!", "11121111213112111131224132411122"),
        ("hello hello", "11121122342"),
        ("Hello", "11121"),
        ("aaaaaaaaaaaa","123456789101112"),
    )
    for key, val in data:
        assert numericals(key) == val


if __name__ == '__main__':
    test()
