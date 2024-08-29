"""
У Фредди очень толстый мизинец левой руки, и каждый раз, когда Фредди пытается
напечатать A, он случайно нажал клавишу CapsLock!

Учитывая строку, которую Фредди хочет набрать, эмулируйте промахи клавиатуры
там, где каждый A предположительно нажатая заменяется на CapsLock и возвращает
строку, которую на самом деле набирает Фредди. Не имеет значения, если A в
строке пишется с заглавной буквы или нет. Когда CapsLock включен, капитализация
меняется на обратную, но пунктуация не затрагивается.

Примеры:

"The quick brown fox jumps over the lazy dog."
-> "The quick brown fox jumps over the lZY DOG."

"aAaaaaAaaaAAaAa"
-> ""
"""


def fat_fingers(s: str, n: int=0) -> str:
    """
    Каждая буква a или A в строке инвертирует CapsLock.
    """
    return ''.join(['' * (n := not n) if x in 'aA' else [x, x.swapcase()][n] for x in s])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("aAaaaaAaaaAAaAa", ""),
        ("The quick brown fox jumps over the lazy dog.", "The quick brown fox jumps over the lZY DOG."),
    )
    for key, val in data:
        assert fat_fingers(key) == val


if __name__ == '__main__':
    test()
