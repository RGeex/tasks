"""
Сложение больших чисел, больше типа int:

- Дано: 2 текстовых файла, в которых в первой
строке, записано число, состоящее из цифр
- Необходимо: вычислить сумму чисел из файлов
"""

from pathlib import Path
from typing import Generator


def get_num(filename: Path) -> str | None:
    """Считывает первую строку из файла."""
    if filename.exists() and filename.is_file():
        with open(filename, 'r', encoding='UTF-8') as file:
            return file.readline().rstrip('\n')
    return None


def zp(*args: str) -> Generator:
    """Возвращает по 1 элементу из каждого переданного итерированного
    объекта. Функция аналогична по своему действию zip_longest из модуля
    itertools, только извлекает элементы с конца последовательности.
    Заменяет значения элементов последовательностей меньшей длины на "0"."""
    for i in range(1, max(map(len, args)) + 1):
        yield list(map(lambda x, i=i: x[-i] if len(x) >= i else '0', args))


def func(*values: str) -> str:
    """Складывает числа посимвольно с конца числа. Возвращает
    результат сложения в виде строки."""
    tmp, res = [], ''
    for i in zp(*values):
        *tmp, data = str(sum(map(int, i + tmp)))
        res = data + res
    return str(*tmp) + res


def main(filenames: list[Path]) -> str:
    """Получает имена файлов, по ним из этих файлов извлекает числа и
    передает в функцию для их сложения. Возвращает получившееся число
    в виде строки."""
    return func(*map(get_num, filenames))


def test() -> None:
    """Тестирование работы алгоритмов."""
    data = [
        ('987', '9742'),
        ('0', '9742'),
        ('987', '0'),
        ('0', '0'),
    ]
    for nums in data:
        assert str(sum(map(int, nums))) == func(*nums)


if __name__ == '__main__':
    test()
