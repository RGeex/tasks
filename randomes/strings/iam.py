"""
Вы очень-очень счастливы и очень-очень рады решить эту Ката.
Покажите это нам, создав функцию iam такой как:

iam('happy') // returns the string "I am happy"
iam('excited') // returns the string "I am excited"
iam()('scared') // returns the string "I am very scared"
iam()()('interested') // returns the string "I am very very interested"

и так далее...

Как вы поняли, функция iam принять 1 необязательный параметр.
Если указано, функция возвращает string.
Если НЕ указано, он должен вернуть function позволяя продолжить предложение.

Мне очень-очень любопытно увидеть, как вы подходите к этой проблеме.
"""

from typing import Callable
from functools import partial


def iam(s: str | None=None, r: str='I am') -> str | Callable:
    """
    Строит предложение из дополнительных слов 'very' при пустом аргументе,
    и возвращает функцию, при наличии аргумента завершается строкой.
    """
    return [r := r + f" {s or 'very'}", partial(iam, r=r)][not s]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (iam("happy"), "I am happy"),
        (iam()("sad"), "I am very sad"),
        (iam()()("tall"), "I am very very tall"),
        (iam()()("tall and ") + iam()("funny"), "I am very very tall and I am very funny"),
    )
    for key, val in data:
        assert key == val

    a = iam()
    b = a()()
    c = b()()
    assert ', '.join([a('happy'), b('big')]) == 'I am very happy, I am very very very big'


if __name__ == '__main__':
    test()
