"""
Вам дан список уникальных целых чисел arr, и два целых числа aи b.
Ваша задача – выяснить, есть или нет a и b появляться последовательно
в arrи верните логическое значение ( True если a и b идут последовательно,
False в противном случае).

Гарантируется, что a и b оба присутствуют в arr.

"""


def consecutive(arr: list[int], a: int, b: int) -> bool:
    """
    Проверяет, послежовательные ли заданные элементы в списке.
    """
    return not next((set(arr[i:i+2]) != {a, b} for i, x in enumerate(arr) if x in (a, b)), 1)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([1, 3, 5, 7], 3, 7), False),
        (([1, 3, 5, 7], 3, 1), True),
        (([1, 6, 9, -3, 4, -78, 0], -3, 4), True),
    )
    for key, val in data:
        assert consecutive(*key) == val


if __name__ == '__main__':
    test()
