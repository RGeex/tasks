"""
Вступление:

Я решал задачу по кодированию. Это была одна из тех многоэтапных задач.
Не знаю, хороший у меня подход или плохой, но на одном из этих шагов я
писал функцию для преобразования слов в числа. Я это сделал... в конце
концов, но... мне не понравилось, как это было написано. Вот я и подумал,
а почему бы не создать ката и не проверить, как это делают другие люди :)
Итак:
Задача:

Ваша задача — написать конвертер слов в числа. Цифры числа должны
соответствовать буквам в слове. Плюс сгенерированное число должно
быть наименьшим возможным числом, которое вы можете получить.

    Слова могут содержать максимум 10 различных букв, но длина слова может
    быть любой, даже более 10 символов.
    Номер НЕ может начинаться с 0
    Одни и те же буквы имеют одну и ту же цифру независимо от регистра.
    Для возврата пустой строки 0

Примеры:

    "A" -> 1 - ХОРОШО

    "ABA" -> 353 - НЕПРАВИЛЬНО (число в порядке, но это не самое маленькое
    число)

    "ABA" -> 333 - НЕПРАВИЛЬНО (разные буквы соответствуют одним и тем же
    цифрам)

    "ABA" -> 357 - НЕПРАВИЛЬНО (одни и те же буквы соответствуют разным цифрам)
"""


def convert(s: str) -> int:
    """
    Переводит слово в минимально возможное число, не начинающееся
    с 0. Идентичные символы имеют одинаковые цифры.
    """
    s = s.lower()
    x = sorted([(s.index(x), x) for x in set((s)) - {s and s[0], }])
    x = dict((x, i - 1 and i) for i, (_, x) in enumerate(x, 1))
    return int(f"0{''.join([str(x.get(v, 1)) for v in s])}")


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("CodeWars", 10234567),
        ("KATA", 1020),
        ("KaTA", 1020),
    )
    for key, val in data:
        assert convert(key) == val


if __name__ == '__main__':
    test()
