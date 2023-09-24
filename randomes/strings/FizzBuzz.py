"""
Вывести числа от 1 до 100, заменяя числа
кратные 3 на Fizz, кратные 5 на Buzz, а
кратные и 3 и 5 на FizzBuzz.
"""

from typing import Generator


def fizzbuzz(n: int) -> Generator:
    """
    Выводит числа от 1 до n, заменяя
    кратные 3 на Fizz, 5 на Buzz, 3 и 5 на
    FizzBuzz.
    """
    for i in range(1, n + 1):
        result = ''
        if not i % 3:
            result += 'Fizz'
        if not i % 5:
            result += 'Buzz'
        yield result if result else i


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = list(fizzbuzz(15))
    lst1 = [1, 2, 4, 7, 8, 11, 13, 14]
    lst2 = ['Fizz', 'Buzz', 'Fizz', 'Fizz', 'Buzz', 'Fizz', 'FizzBuzz']
    lst3 = list(filter(lambda x: isinstance(x, int), data))
    lst4 = list(filter(lambda x: isinstance(x, str), data))

    assert lst1 == lst3
    assert lst2 == lst4


if __name__ == '__main__':
    test()
