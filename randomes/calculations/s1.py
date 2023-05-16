"""
Дано:
Дано число n. Необходимо разложить факториал этого
число на простые множители и
представить результат в строковом виде.

Задание:
Напишите функцию decomp, которая будет возвращать строку
вида a^b * c^d * ... * e.
Примечание: Простые числа должны быть в порядке возрастания.
Примечание: Когда показатель простого числа равен 1, не
ставьте показатель степени.
Функция decomp принимает на вход только число n.
Важно: Лишних пробелов быть не должно. Но вокруг знаков
умножения должны быть пробелы.

Пример:
n = 12, Ответ: 2^10 * 3^5 * 5^2 * 7 * 11
n = 22, Ответ: 2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19
"""

from typing import Generator


def factorials() -> Generator:
    """Генератор бесконечного ряда факториалов."""
    res, num = 1, 0
    while True:
        num += 1
        res *= num
        yield res


def get_factorial(num: int) -> int:
    """Получить факториал заданного числа."""
    factor = factorials()
    for _ in range(num):
        result = next(factor)
    return result


def get_decomp(num: int) -> dict:
    """Декомпозиция числа на простые множители."""
    data = {}
    divider = 2
    while divider <= num:
        if num % divider:
            divider += 1
            continue
        num //= divider
        data[divider] = data.get(divider, 0) + 1

    return data


def decomp(num: int) -> None:
    """Представление данных в указанном виде."""
    data = get_decomp(get_factorial(num))
    res = ''
    for key, val in data.items():
        res += ' * ' if res else ''
        res += f'{key}'
        res += f'^{val}' if val > 1 else ''

    print(res)


def test() -> None:
    """Тестирование работы алгоритмов."""
    data1 = {2: 10, 3: 5, 5: 2, 7: 1, 11: 1}
    data2 = {2: 19, 3: 9, 5: 4, 7: 3, 11: 2, 13: 1, 17: 1, 19: 1}
    data3 = get_decomp(get_factorial(12))
    data4 = get_decomp(get_factorial(22))

    assert data1 == data3
    assert data2 == data4


if __name__ == '__main__':
    test()
