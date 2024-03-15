"""
Завершите решение так, чтобы он удалил весь текст, следующий за любым из переданных маркеров
комментариев. Любые пробелы в конце строки также следует удалить.

Пример:

Учитывая входную строку:

apples, pears # and bananas
grapes
bananas !apples

Ожидаемый результат будет следующим:

apples, pears
grapes
bananas

Код будет называться так:

result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


import re


def strip_comments(s: str, m: list) -> str:
    """
    Удаляет комментарии из текста построчно (\n), по заданным ключевым символам начала комментария.
    """
    return re.sub(rf' *[\\{x}].*', '', s) if (x := '\\'.join(m)) else s


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']), 'apples, pears\ngrapes\nbananas'),
        (('a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd'),
        ((' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd'),
    )
    for key, val in data:
        assert strip_comments(*key) == val


if __name__ == '__main__':
    test()
