"""
Порядковые номера используются для обозначения позиции чего-либо в списке.
В отличие от обычных чисел, к их концу добавляется специальный суффикс.

Задача

Ваша задача написать ordinal(number, brief) функция. number будет целым числом.
Вам нужно найти порядковый номер указанного числа.

brief является необязательным параметром и по умолчанию имеет значение false.
При использовании кратких обозначений nd и rd использовать d вместо.
Все остальные такие же.

ordinal(number, brief) должен возвращать строку, содержащую эти два символ
(или один символ), которые будут отмечены в конце числа.

Последние две цифры определяют порядковый суффикс.

Notation for general notation

0  1  2  3  4  5  6  7  8  9
th st nd rd th th th th th th

Notation for brief notation

0  1  2  3  4  5  6  7  8  9
th st d  d th th th th th th

 

Однако, когда последние две цифры номера равны 11, 12 или 13, th используется
вместо st, nd, rd соответственно.

Примеры

*General
1 - 1st
2 - 2nd
3 - 3rd
5 - 5th
11- 11th
149 - 149th
903 - 903rd

*Brief
1 - 1st
2 - 2d
3 - 3d
5 - 5th
11- 11th
149 - 149th
903 - 903d

 

Примечания

    Числа могут передаваться вместо логических значений, поэтому false может
    быть передано как 0 и true может быть передано как 1.

"""


def ordinal(n: int, brief: bool=False) -> str:
    """
    По переданному числу выводит правильное окончание суффикса.
    """
    return (dict(enumerate('th st nd rd'.split() + ['th'] * 10)).get(n := int(x := str(n)[-2:])) or ordinal(int(x[-1]), brief))[brief and n in (2, 3):]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = ( 
        ((1,), "st"),
        ((11,), "th"),
        ((111,), "th"),
        ((121,), "st"),
        ((20,), "th"),
        ((52,), "nd"),
        ((53,), "rd"),
        ((903, True), "d"), 
    )
    for key, val in data:
        assert ordinal(*key) == val


if __name__ == '__main__':
    test()
