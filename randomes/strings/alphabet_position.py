"""
В этом ката вам необходимо по заданной строке заменить каждую букву ее позицией в алфавите.

Если что-то в тексте не является буквой, проигнорируйте это и не возвращайте.

"a" = 1, "b" = 2, и т. д.
Пример

alphabet_position("The sunset sets at twelve o' clock.")

Должен вернуться "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"(как строка) 
"""


def alphabet_position(text: str) -> str:
    """
    Переводит буквенные символы строки в их порядковый номер в алфавите.
    """
    return ' '.join(f'{ord(x) - 96}' for x in text.lower() if x.isalpha())


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("The sunset sets at twelve o' clock.",
         "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"),
        ("The narwhal bacons at midnight.", "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"),
    )
    for key, val in data:
        assert alphabet_position(key) == val


if __name__ == '__main__':
    test()
