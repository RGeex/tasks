"""
Задача
Вам дана строка, состоящая из «D», «P» и «C».
Положительное целое число N называется DPC этой
строки, если оно удовлетворяет следующим свойствам:

Для каждого i = 1, 2,... размер строки:
- Если i-й символ "D", то N можно разделить на i
- Если i-й символ "P", то N и i должны быть взаимно простыми
- Если i-й символ "C", то N не должно делиться на i,
и не быть взаимно простым с i

Ваша задача — найти наименьший DPC заданной строки или вернуть -1,
если такового нет.  Результат гарантированно будет <= 10^9.

Пример
Для s = "DDPDD" результат должен быть 20.
«DDPDD» означает, что N должно быть разделено на 1,2,4,5, а N,3 должно
быть взаимно простым числом. Наименьшее N должно быть равно 20.

Ввод, вывод:
[ввод] строка с
Данная строка

[выход] целое число
Наименьший DPC из s или -1, если он не существует.
"""


def get_lcm(arr: list) -> int:
    """Поиск наименьшего общего кратного"""
    num = -1 + (s := [1, 0][any(not i % 2 for i in arr)])
    while True:
        num += 1
        val = (int(not num - s) or num) * arr[-1]
        if all(not val % x for x in arr):
            return val


def coprime(arr: list, num: int) -> bool:
    """Поиск наибольших общих делителей"""
    for i in arr:
        for x in range(2, min(i, num) + 1):
            if not i % x and not num % x:
                return False
    return True


def DPC_sequence(s: str) -> int:
    """Дешифрование строки по заданному алгоритму"""
    outs, data = [], {}
    for i, val in enumerate(s, 1):
        data[val] = data.get(val, []) + [i]

    N = get_lcm(data.get('D'))

    for key, val in data.items():
        if key == 'P':
            outs.append(coprime(val, N))
        if key == 'C':
            outs.append(not coprime(val, N))
            outs.append(all(N % x for x in val))

    return N if all(outs) else -1


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        ("DPPPPPDPPPPPPCPPPPPPCPPPPPPCPPPPPPCPPPPPPCPPPPPP", 7),
        ("DDDDPDDCCCPDPDCCPCPCDCPCPCCDPCPCCCCCPCC", 84),
        ("DDDDPDDCCCDDPDCCPCDCDDPCPCCDDCD", 15782844),
        ("DDPDPCPCPCPCPCPCPCPCPCPCPCPCPCPCPC", 4),
        ("DPCPDPPPDCPDPDPC", -1),
        ("DDDDDDPCCDPDPP", -1),
        ("PDCDDDDDD", -1),
        ("DDDDDDCD", -1),
        ("CDDDPDDD", -1),
        ("CDDCCD", -1),
        ("DDPDD", 20),
    )

    for key, val in data:
        assert DPC_sequence(key) == val


if __name__ == '__main__':
    test()
