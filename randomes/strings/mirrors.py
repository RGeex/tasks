"""
Вам дана строка n строки, каждая подстрока которых является nсимволов длиной: Например:

s = "abcd\nefgh\nijkl\nmnop"

Мы рассмотрим некоторые преобразования этого квадрата строк.

    Вертикальное зеркало: vert_mirror (или vertMirror или vert-mirror)

    vert_mirror(s) => "dcba\nhgfe\nlkji\nponm"

    Горизонтальное зеркало: hor_mirror (или horMirror или hor-mirror)

     hor_mirror(s) => "mnop\nijkl\nefgh\nabcd"

или распечатано:

vertical mirror   |horizontal mirror   
abcd --> dcba     |abcd --> mnop 
efgh     hgfe     |efgh     ijkl 
ijkl     lkji     |ijkl     efgh 
mnop     ponm     |mnop     abcd 

Задача:

    Напишите эти две функции

и

    функция высокого порядка oper(fct, s) где

    fct — это функция одной переменной f, применяемая к строке s
    (ФКТ будет одним из vertMirror, horMirror)

Примеры:

s = "abcd\nefgh\nijkl\nmnop"
oper(vert_mirror, s) => "dcba\nhgfe\nlkji\nponm"
oper(hor_mirror, s) => "mnop\nijkl\nefgh\nabcd"

Примечание:

Форма параметра fctв эксплуатации Изменения в зависимости от языка. Вы можете
увидеть каждую форму в зависимости от языка в разделе «Примеры тестов».
Примечание Bash:

Входные строки разделяются , вместо \n. Выходные строки должны быть
разделены \r вместо \n. См. «Примеры тестов».
"""
import typing
import unittest
from typing import Callable


def vert_mirror(strng: str) -> str:
    """
    Зеркально отражает строку по вертикали.
    """
    return '\n'.join(x[::-1] for x in strng.split('\n'))


def hor_mirror(strng: str) -> str:
    """
    Зеркально отражает строку по горизонтали.
    """
    return '\n'.join(strng.split('\n')[::-1])


def oper(fct: Callable[[str], str], s: str) -> str:
    """
    Вызывает функцию для зеркального отражения.
    """
    return fct(s)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(oper, (
        ((vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"), "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw"),
        ((vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"), "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP"),
        ((vert_mirror, "cuQW\nxOuD\nfZwp\neqFx"), "WQuc\nDuOx\npwZf\nxFqe"),
        ((vert_mirror, "CDGIdolo\nUstXfrIg\ntMqjvxWL\nBEyuCnAm\nxsxaEERa\nxZsvOiZS\nLutlBRXE\ntxshhbqE"), "olodIGDC\ngIrfXtsU\nLWxvjqMt\nmAnCuyEB\naREEaxsx\nSZiOvsZx\nEXRBltuL\nEqbhhsxt"),

        ((hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"), "yeCt\nCSbg\nJVhv\nlVHt"),
        ((hor_mirror, "njMK\ndbrZ\nLPKo\ncEYz"), "cEYz\nLPKo\ndbrZ\nnjMK"),
        ((hor_mirror, "QMxo\ntmFe\nWLUG\nowoq"), "owoq\nWLUG\ntmFe\nQMxo"),
        ((hor_mirror, "FYvi\ndZQn\nuGef\nQoSy"), "QoSy\nuGef\ndZQn\nFYvi"),
    ))
