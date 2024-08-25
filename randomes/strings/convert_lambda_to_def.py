"""
Преобразование лямбды в Def

в этой ката вам будет предоставлена ​​строка с лямбда-функцией. Ваша задача —
преобразовать эту лямбда-функцию в функцию def с теми же переменными, тем же
именем и той же функцией, которую она выполняет.

Функция, как обычная def функция должна быть возвращена в отдельной строке.

Вывод должен быть возвращен в виде строки.
Примеры

код будет таким:

convert_lambda_to_def("func = lambda a: a * 1")
# the output should == "def func(a):\n    return a * 1"

вам нужно поставить 4 четыре пробела перед return часть вашего результата.

переменное количество пробелов, позиционные/ключевые аргументы или нулевые
аргументы не будут проверяться. двойные параметры не будут проверяться.
"""


import re


def convert_lambda_to_def(s: str) -> str:
    """
    Переводит lambda функцию в def функцию.
    """
    return re.sub(r'(.*) = lambda (.*?):', r'def \1(\2):\n    return', s)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("func = lambda a: a * 2", "def func(a):\n    return a * 2"),
        ("somes = lambda s: s + 1", "def somes(s):\n    return s + 1"),
        ("act = lambda h: h + ' ' + 'i'", "def act(h):\n    return h + ' ' + 'i'"),
    )
    for key, val in data:
        assert convert_lambda_to_def(key) == val


if __name__ == '__main__':
    test()
