"""
Если чередовать гласные и согласные в строке "have", мы получаем следующий
список, расположенный в алфавитном порядке: ['ahev', 'aveh', 'ehav', 'evah',
'have', 'heva', 'vahe', 'veha']. Это единственные возможности, в которых
чередуются гласные и согласные. Первый элемент, ahev, является самым низким
в алфавитном порядке.

Дана строка:

    чередуйте гласные и согласные и возвращайте лексикографически самый низкий
    элемент в списке
    Если какие-либо две или более гласные или согласные должны следовать друг
    за другом, верните "failed"
    если количество гласных и согласных одинаково, первая буква результата
    должна быть гласной.

Примеры:

solve("codewars") = "failed". However you alternate vowels and consonants,
two consonants must follow each other
solve("oruder") = "edorur"
solve("orudere") = "ederoru". This is the only option that allows you to
alternate vowels & consonants.

Гласные будут любыми из «aeiou». Ввод будет строкой в ​​нижнем регистре, без
пробелов. Дополнительные примеры см. в тестовых примерах.
"""

from operator import add, sub
from itertools import zip_longest as zl


def alternation_of_letters(s: str) -> str:
    """
    Чередует гласные и согласные в слове, находя самый лексографически низний.
    """
    x = [sorted(filter(bool, x)) for x in zip(*[['', x][::[1, -1][x in 'aeiou']] for x in s])]
    return ''.join([add(*x)[::[1, -1][n < 0]] for x in zl(*x, fillvalue='')]) if abs(n := sub(*map(len, x))) in (0, 1) else 'failed'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("java", 'ajav'),
        ("oruder", 'edorur'),
        ("zodiac", 'acidoz'),
        ("apple", 'lapep'),
        ("acidity", 'caditiy'),
        ("codewars", 'failed'),
        ("orudere", 'ederoru'),
    )
    for key, val in data:
        assert alternation_of_letters(key) == val


if __name__ == '__main__':
    test()
