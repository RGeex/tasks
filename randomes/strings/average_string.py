"""
Вам дана строка чисел от 0 до 9. Найдите среднее значение этих чисел и верните
его в виде целого числа (т. е. без десятичных знаков), записанного в виде
строки. Например:

«ноль девять пять два» -> «четыре»

Если строка пуста или содержит число больше 9, верните «н/д».
"""


def average_string(s: str) -> str:
    """
    Поиск среднего значения чисел, записанных в строке.
    """
    a, b = [dict(zip(*['zero one two three four five six seven eight nine'.split(), range(10)][::i or -1])) for i in range(2)]
    return a.get(sum(b.get(w) for w in s.split()) // len(s.split())) if s and all(x in b for x in s.split()) else 'n/a'



def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("zero nine five two", "four"),
        ("four six two three", "three"),
        ("one two three four five", "three"),
        ("five four", "four"),
        ("zero zero zero zero zero", "zero"),
        ("one one eight one", "two"),
        ("one", "one"),
        ("", "n/a"),
        ("ten", "n/a"),
        ("pippi", "n/a"),
    )
    for key, val in data:
        assert average_string(key) == val


if __name__ == '__main__':
    test()
