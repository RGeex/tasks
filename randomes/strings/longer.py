"""
Создать функцию longerкоторый принимает строку и сортирует содержащиеся в ней слова по их длине в
порядке возрастания. Если есть два слова одинаковой длины, отсортируйте их по алфавиту.
Для получения более подробной информации посмотрите примеры ниже.

longer("Another Green World") => Green World Another
longer("Darkness on the edge of Town") => of on the Town edge Darkness
longer("Have you ever Seen the Rain") => the you Have Rain Seen ever

Предположим, что в качестве входных данных будут введены только алфавиты. Символы верхнего регистра
имеют приоритет над символами нижнего регистра. То есть,

longer("hello Hello") => Hello hello

"""


def longer(s: str) -> str:
    """
    Сортирует строку по длине слов, по словам (приоритет заглавные).
    """
    return ' '.join(sorted(s.split(), key=lambda x: (len(x), x)))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("Another Green World", "Green World Another"),
        ("Darkness on the edge of Town", "of on the Town edge Darkness"),
        ("Have you ever Seen the Rain", "the you Have Rain Seen ever"),
        ("Like a Rolling Stone", "a Like Stone Rolling"),
        ("This will be our Year", "be our This Year will"),
        ("hello Hello", "Hello hello"),
    )
    for key, val in data:
        assert longer(key) == val


if __name__ == '__main__':
    test()
