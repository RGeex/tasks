"""
Если вы не знакомы с фантастическими кулинарными изысками Британских островов, возможно,
вы не знаете о сэндвиче с хлебом.

Идея очень проста: если у вас есть кусок хлеба между двумя другими ломтиками хлеба,
то это бутерброд с хлебом. Кроме того, если у вас есть сэндвич с хлебом между двумя
другими ломтиками хлеба, вы получите сэндвич с хлебом и так далее.

В этой ката мы определим следующие термины следующим образом:

    Сэндвич — два ломтика хлеба с начинкой или без нее.
    Сэндвич с хлебом - два ломтика хлеба, в центре которых находится один ломтик хлеба в
    качестве начинки.

Вам нужно будет создать две функции:

    Учитывая количество ломтиков хлеба, верните фразу, обозначающую сэндвич.

     2 - 'sandwich'
     5 - 'bread sandwich sandwich'

    Обратная функция — по названию сэндвича вернуть количество ломтиков хлеба в сэндвиче

    'bread sandwich' - 3
    'sandwich sandwich' - 4

    Тебе следует вернуться None/ nullесли ввода нет/ввод неверен/нет сэндвича
    Максимум 100 ломтиков хлеба
"""


def slices_to_name(n: int) -> str:
    """
    Учитывая кол-во ломтиков хлеба, возвращает словами порядок по шаблону.
    """
    return ' '.join(n % 2 * ['bread'] + n // 2 * ['sandwich']) if isinstance(n, int) and 1 < n else None


def name_to_slices(name: str) -> int:
    """
    Из заднной строки сендивичей, определяет кол-во ломтиков хлеба.
    """
    if isinstance(name, str):
        x = [{n == 'bread' and not i: 1, n == 'sandwich': 2}.get(1) for i, n in enumerate(name.split())]
        return None if len(x) < 2 or None in x else sum(x)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data1 = (
        (0, None),
        (1, None),
        (-2, None),
        ('bread', None),
        (2, 'sandwich'),
        (3, 'bread sandwich'),
        (11, 'bread sandwich sandwich sandwich sandwich sandwich'),
        (8, 'sandwich sandwich sandwich sandwich'),
    )
    for key, val in data1:
        assert slices_to_name(key) == val

    data2 = (
        (12, None),
        ('', None),
        ('sandwich bread sandwich', None),
        ('sand wich', None),
        ('sandwich sandwich sandwich sandwich', 8),
        ('bread', None),
        ('bread sandwich sandwich sandwich', 7),
        ('bread sandwich bread sandwich', None),
        ('banana sandwich', None),
        ('breadsandwich', None),
    )
    for key, val in data2:
        assert name_to_slices(key) == val


if __name__ == '__main__':
    test()
