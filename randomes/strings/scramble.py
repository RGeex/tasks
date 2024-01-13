"""
Завершите функцию scramble(str1, str2)который возвращает trueесли часть str1символы можно
переставлять в соответствии с str2, в противном случае возвращает false.

Примечания:

    Будут использоваться только строчные буквы (az). Никакие знаки препинания и цифры не
    будут включены.
    Необходимо учитывать производительность.

Примеры

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False


"""

from collections import Counter


def scramble(s1: str, s2: str) -> bool:
    """
    Проверяет, можно ли составить из букв первого слова второе.
    """
    return not Counter(s2) - Counter(s1)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (('rkqodlw', 'world'), True),
        (('cedewaraaossoqqyt', 'codewars'), True),
        (('katas', 'steak'), False),
        (('scriptjava', 'javascript'), True),
        (('scriptingjava', 'javascript'), True)
    )
    for key, val in data:
        assert scramble(*key) == val


if __name__ == '__main__':
    test()
