"""
Дан набор слов. Слова соединяются, если последняя буква одного слова и первая
буква другого слова совпадают. Возвращаться true если все слова множества можно
объединить в одно слово. Каждое слово можно и нужно использовать только один раз.
В противном случае верните false.
Вход

Список от 3 до 7 слов произвольной длины. Никаких заглавных букв.
Пример true

Набор: раскопать, терпеть, желание, экран, театр, избыток, ночь.
Многоножка: Желание Терпеть Выкапывать Лишний Экран Ночной Театр.
Пример false

Комплект: торговля, столб, вид, могила, лестница, гриб, президент.
Многоножка: президентТ Трейд.
"""


def little_train(arr: list[str], r: str = ''):
    """
    Проверяет могут ли слова из заданного списка объединиться в 1 непрерывную строку.
    """
    if not arr:
        return True
    for i, x in enumerate(arr):
        if not r or r[-1] == x[0]:
            if little_train(arr[:i] + arr[i+1:], r + x):
                return True
    return False


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (['no', 'dog', 'on', 'good'], False),
        (['no', 'dog', 'on', 'good', 'goon'], True),
        (["excavate", "endure", "screen", "desire", "theater", "excess", "night"], True),
        (["trade", "pole", "view", "grave", "ladder", "mushroom", "president"], False),
    )
    for key, val in data:
        assert little_train(key) == val


if __name__ == '__main__':
    test()
