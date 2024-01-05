"""
В этом ката мы собираемся имитировать систему управления версиями программного обеспечения.

Вам необходимо реализовать VersionManagerсорт.

Он должен принимать необязательный параметр, представляющий исходную версию. Входные данные будут в
одном из следующих форматов: "{MAJOR}", "{MAJOR}.{MINOR}", или "{MAJOR}.{MINOR}.{PATCH}".
Дополнительные значения могут быть предоставлены после PATCHно их следует игнорировать.
Если эти 3 части не являются десятичными значениями, возникает исключение с сообщением
"Error occured while parsing version!"следует бросить. Если исходная версия не указана
или представляет собой пустую строку, используйте "0.0.1"по умолчанию.

Этот класс должен поддерживать следующие методы, все из которых должны быть цепочками
(кроме release):

    major()- увеличивать MAJORк 1, набор MINORи PATCHк 0
    minor()- увеличивать MINORк 1, набор PATCHк 0
    patch()- увеличивать PATCHк 1
    rollback()- вернуть MAJOR, MINOR, и PATCHк своим значениям до предыдущего major/ minor/ patch
    позвоните или выдайте исключение с сообщением "Cannot rollback!"если нет версии, на которую
    можно откатиться. Несколько обращений к rollback()должно быть возможно и восстановить историю
    версий
    release()- вернуть строку в формате "{MAJOR}.{MINOR}.{PATCH}"

Да пребудет с вами бинарная сила!
"""


class VersionManager:
    """
    Менеджер версий вида "{MAJOR}.{MINOR}.{PATCH}".
    """
    def __init__(self, version=None):
        vs = version and version.split('.')[:3] or list('001')
        if next((1 for x in vs if not x.isdigit()), 0):
            raise ValueError('Error occured while parsing version!')
        self._history = [vs + ['0'] * (3 - len(vs))]

    def _change_version(self, n):
        """
        Повышает текущую версию и сохраняет в историю.
        """
        self._history.append([[[x, '0'][n < i], str(int(x) + 1)][i == n] for i, x in enumerate(self._history[-1])])
        return self

    def release(self):
        """
        Выдает текущую версию.
        """
        return '.'.join(self._history[-1])

    def rollback(self):
        """
        Откатывает текущую версию на предыдущую, если это возможно.
        """
        if len(self._history) == 1:
            raise ValueError('Cannot rollback!')
        return self._history.pop() and self

    # Повышение версии
    def major(self): return self._change_version(0)
    def minor(self): return self._change_version(1)
    def patch(self): return self._change_version(2)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """

    # "Initialization tests"
    data = (
        (VersionManager().release(), "0.0.1"),
        (VersionManager("").release(), "0.0.1"),
        (VersionManager("1.2.3").release(), "1.2.3"),
        (VersionManager("1.2.3.4").release(), "1.2.3"),
        (VersionManager("1.2.3.d").release(), "1.2.3"),
        (VersionManager("1").release(), "1.0.0"),
        (VersionManager("1.1").release(), "1.1.0"),
    )
    for key, val in data:
        assert key == val

    # "Major releases tests"
    data = (
        (VersionManager().major().release(), "1.0.0"),
        (VersionManager("1.2.3").major().release(), "2.0.0"),
        (VersionManager("1.2.3").major().major().release(), "3.0.0"),
        (VersionManager("10.11.12").major().major().release(), "12.0.0"),
    )
    for key, val in data:
        assert key == val

    # "Minor releases tests"
    data = (
        (VersionManager().minor().release(), "0.1.0"),
        (VersionManager("1.2.3").minor().release(), "1.3.0"),
        (VersionManager("1").minor().release(), "1.1.0"),
        (VersionManager("4").minor().minor().release(), "4.2.0"),
    )
    for key, val in data:
        assert key == val

    # "Patch releases tests"
    data = (
        (VersionManager().patch().release(), "0.0.2"),
        (VersionManager("1.2.3").patch().release(), "1.2.4"),
        (VersionManager("4").patch().patch().release(), "4.0.2"),
    )
    for key, val in data:
        assert key == val

    # "Rollbacks tests"
    data = (
        (VersionManager().major().rollback().release(), "0.0.1"),
        (VersionManager().minor().rollback().release(), "0.0.1"),
        (VersionManager().patch().rollback().release(), "0.0.1"),
        (VersionManager().major().patch().rollback().release(), "1.0.0"),
        (VersionManager().major().patch().rollback().major().rollback().release(), "1.0.0"),
        (VersionManager().major().patch().rollback().rollback().release(), "0.0.1"),
    )
    for key, val in data:
        assert key == val

    # "Seperated calls"
    m = VersionManager("1.2.3")
    m.major()
    m.minor()
    assert m.release() == "2.1.0"

    # "Invalid initial versions"
    for version in ("a", "a.b.c", "1.a", "0.1.a.5"):
        try:
            VersionManager(version)
            raise ValueError('invalid values')
        except ValueError as e:
            assert str(e) == "Error occured while parsing version!"

    # "Invalid rollbacks"
    vm = VersionManager()
    try:
        vm.rollback()
        raise ValueError('Should throw when cannot rollback')
    except ValueError as e:
        assert str(e) == "Cannot rollback!"
        vm.major()
        assert vm.release() == "1.0.0"
        vm.rollback()
        assert vm.release() == "0.0.1"


if __name__ == '__main__':
    test()
