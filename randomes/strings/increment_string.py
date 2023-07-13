"""
Ваша задача — написать функцию, которая увеличивает строку,
чтобы создать новую строку.

Если строка уже заканчивается числом, число должно быть увеличено на 1.
Если строка не заканчивается цифрой, число 1 должно быть добавлено к новой строке.

Внимание: Если в числе есть ведущие нули, следует учитывать количество цифр.
"""

import re
from typing import Generator


def zip_from_end(*args: str) -> Generator:
    """Возвращает по 1 элементу из каждого переданного итерированного
    объекта. Функция аналогична по своему действию zip_longest из модуля
    itertools, только извлекает элементы с конца последовательности.
    Заменяет значения элементов последовательностей меньшей длины на "0"."""
    for i in range(1, max(map(len, args)) + 1):
        yield list(map(lambda x, i=i: x[-i] if len(x) >= i else '0', args))


def stacking(*values: str) -> str:
    """Складывает числа посимвольно с конца числа. Возвращает
    результат сложения в виде строки."""
    tmp, res = [], ''
    for i in zip_from_end(*values):
        *tmp, data = str(sum(map(int, i + tmp)))
        res = data + res
    return str(*tmp) + res


def increment_string(strng: str) -> str:
    """Обновление имени, увеличивая на 1 цифровое окончание или добавляя его."""
    s = re.search(r'\d+$', strng)
    x = s and strng[:s.span()[0]] or strng

    return x + stacking(s.group() if s else '0', '1')


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        ("", "1"),
        ("foo", "foo1"),
        ("foobar1", "foobar2"),
        ("foobar00", "foobar01"),
        ("foobar99", "foobar100"),
        ("foobar099", "foobar100"),
        ("foobar001", "foobar002"),
        ("fo99obar99", "fo99obar100"),
    )

    for key, val in data:
        assert increment_string(key) == val


if __name__ == '__main__':
    test()
