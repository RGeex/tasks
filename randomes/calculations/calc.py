import inspect
from operator import mul, add, sub, floordiv


NUMS = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

FUNC = {
    'plus': add,
    'minus': sub,
    'times': mul,
    'divided_by': floordiv,
}


def calc(_=None):

    string = inspect.stack()[1][4][0].strip()
    a, f, b = string[string.find('(') + 1:-1].split('(')[:3]

    return FUNC[f](NUMS[a], NUMS[b])


globals().update({num: calc for num in NUMS | FUNC})


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (two(plus(two())), 4),
        (seven(times(five())), 35),
    )
    for key, val in data:
        assert key == val


if __name__ == '__main__':
    test()
