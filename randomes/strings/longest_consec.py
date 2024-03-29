"""
Вам дан массив (список) strarrстрок и целого числа k.
Ваша задача — вернуть первую самую длинную строку состоящий
из k последовательных строк, взятых в массив.
Примеры:

strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) -->
"abigailtheta"

n — длина массива строк, если n = 0или k > nили k <= 0вернуть ""
(вернуть Nothingв Elm, «ничего» в Erlang).
Примечание

последовательные строки: следуют друг за другом без перерыва
"""

def longest_consec(strarr: list[str], k: int) -> str:
    """
    Находит максимально возможную по длине строку, состоящую из заданного кол-ва подряд идущих подстрок.
    """
    return max([''.join(strarr[i:i+k]) for i in range(len(strarr) - k + 1)], key=len) if k in range(len(strarr) + 1) else ''


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([], 3), ""),
        ((["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), ""),
        ((["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), ""),
        ((["zone", "abigail", "theta", "form", "libe", "zas"], -2), ""),
        ((["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta"),
        ((["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz"),
        ((["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu"),
        ((["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh"),
        ((["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"),
    )
    for key, val in data:
        assert longest_consec(*key) == val


if __name__ == '__main__':
    test()
