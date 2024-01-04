
"""
Создайте функцию, принимающую положительное целое число от 1 до 3999 (оба включены) в качестве
параметра и возвращающую строку, содержащую представление этого целого числа римскими цифрами.

Современные римские цифры записываются путем выражения каждой цифры отдельно, начиная с самой левой
цифры и пропуская любую цифру со значением ноль. Римскими цифрами обозначается 1990 год: 1000=М,
900=СМ, 90=ХС; в результате получается MCMXC. 2008 год записывается как 2000=ММ, 8=VIII;
или ММВIII. В 1666 году каждый римский символ используется в порядке убывания: MDCLXVI.

Пример:

solution(1000) # should return 'M'

Помощь:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

Помните, что в ряду не может быть более 3 одинаковых символов.
"""


def arabic_num_to_rome(num: int) -> str:
    """
    Создает представление арабских чисел в виде римских от 1 до 3999.
    """
    r, data = '', 'IVXLCDM'
    for i, v in enumerate(str(num)[::-1]):
        n = int(v)
        x = (n - n // 5) // 4 * 5 - n
        a, *b = data[i*2:i*2+3]
        r = ''.join([a * abs(x), ([''] + b)[(n - n // 5) // 4]][::not x or x // abs(x)]) + r
    return r


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (1, 'I'),
        (4, 'IV'),
        (6, 'VI'),
        (14, 'XIV'),
        (21, 'XXI'),
        (89, 'LXXXIX'),
        (91, 'XCI'),
        (984, 'CMLXXXIV'),
        (1000, 'M'),
        (1889, 'MDCCCLXXXIX'),
        (1989, 'MCMLXXXIX'),
    )
    for key, val in data:
        assert arabic_num_to_rome(key) == val


if __name__ == '__main__':
    test()
