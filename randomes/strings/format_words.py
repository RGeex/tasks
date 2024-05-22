"""
Завершите метод так, чтобы он форматировал слова в одно значение, разделенное
запятыми. Последнее слово должно быть отделено словом «и» вместо запятой.
Метод принимает массив строк и возвращает одну форматированную строку.

Примечание:

    Пустые строковые значения следует игнорировать.
    Пустые массивы или значения null/nil/None , передаваемые в метод, должны
    приводить к возврату пустой строки.

Пример: (Ввод -> вывод)

['ninja', 'samurai', 'ronin'] --> "ninja, samurai and ronin"
['ninja', '', 'ronin'] --> "ninja and ronin"
[] -->""
"""


def format_words(s: str) -> str:
    """
    Разделяет слова запятыми, кроме последнего.
    """
    s = [x for x in s if x] if s else ''
    return ' and '.join([x for x in (', '.join(s[:-1]), s[-1] if s else '') if x])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (['one', 'two', 'three', 'four'], 'one, two, three and four'),
        (['one'], 'one'),
        (['one', '', 'three'], 'one and three'),
        (['', '', 'three'], 'three'),
        (['one', 'two', ''], 'one and two'),
        ([], ''),
        (None, ''),
        ([''], ''),
    )
    for key, val in data:
        assert format_words(key) == val


if __name__ == '__main__':
    test()
