"""
Вам необходимо извлечь часть имени файла следующим образом:

    Предположим, что он начнется с даты, представленной в виде длинного числа.
    Далее следует подчеркивание
    Тогда у вас будет имя файла с расширением
    в конце всегда будет дополнительное расширение

Входы:

1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION

1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34

1231231223123131_myFile.tar.gz2

Выходы

FILE_NAME.EXTENSION

This_is_an_otherExample.mpg

myFile.tar

Допустимые символы для случайных тестов:

abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-0123456789

Рекомендуемый способ решения этой проблемы — использование RegEx и,
в частности, групп.
"""


def extract_file_name(dirty_file_name: str) -> str:
    """
    Извлекает истинное имя файла с его первым расширением.
    """
    return '.'.join(dirty_file_name.split('_', 1)[1].split('.')[:2])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION","FILE_NAME.EXTENSION"),
        ("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34","FILE_NAME.EXTENSION"),
    )
    for key, val in data:
        assert extract_file_name(key) == val


if __name__ == '__main__':
    test()
