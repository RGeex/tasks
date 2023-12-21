"""
Напиши функцию check_generator, который проверяет состояние выражения генератора Python gen
и возвращается 'Created', 'Started'или 'Finished'. Например:

gen = (i for i in range(1))>>> возвращается 'Created'(генератор запущен)

gen = (i for i in range(1)); next(gen, None)>>> возвращается 'Started'(генератор выдал значение)

gen = (i for i in range(1)); next(gen, None); next(gen, None)>>> возвращается 'Finished'(генератор сдох)
"""

from typing import Generator


def check_generator(x: Generator) -> str:
    """
    Определяет статус генератора.
    """
    return {x.gi_suspended: 'Started', not x.gi_frame: 'Finished'}.get(1, 'Created')


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    gen = (i for i in range(2))
    for key in 'Created Started Started Finished'.split():
        assert check_generator(gen) == key
        next(gen, None)


if __name__ == '__main__':
    test()
