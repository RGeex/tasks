"""
Задача:

создавать уникальный слаг путем добавления порядкового номера
на основе существующих записей.
"""


from itertools import zip_longest as zl


def create_slug(arr: list[str], s: str) -> str:
    """
    Создает уникальный слаг на основе списка существующих слагов.
    """
    tmp = [x.rsplit('-', 1) for x in arr + [f'{s}-0'] if x.startswith(s)]
    num = int(max(filter(str.isdigit, list(zl(*tmp, fillvalue='0'))[1]), key=int))
    return f'{s}-{num + 1}' if len(tmp) > 1 else s


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((['ss', '321', 'new-world', 'hello-world'], '123'), '123'),
        ((['ss', '321', '123', 'new-world', 'hello-world'], '123'), '123-1'),
        ((['ss', '321', '123', '123-1', 'new-world', 'hello-world'], '123'), '123-2'),
        ((['ss', '321', '123', '123-a1', 'new-world', 'hello-world'], '123'), '123-1'),
    )
    for key, val in data:
        assert create_slug(*key) == val


if __name__ == '__main__':
    test()
