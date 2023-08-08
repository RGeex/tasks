# def get_error(pos: str):


def available_moves(pos: str):
    # tmp = ([chr(x + 65) for x in range(8)], [str(x + 1) for x in range(8)])

    # a, b = ord(position[0]) - 64, int(position[1])
    # print(all())
    # print([x for k in [[1], [2]] for x in k])
    # res = ''.join([f'{chr(x + 65)}{str(x + 1)}' for x in range(8)])[1::2]

    res = []
    tmp = ''.join([f'{chr(x + 65)}{str(x + 1)}' for x in range(8)])

    if len(pos) == 2 and all(x in tmp[i::2] for i, x in enumerate(pos)):
        for m in range(1, 9):
            for n in range(1, 9):
                if str(n) == pos[1] or chr(m + 64) == pos[0]:
                    res.append(f'{chr(m+64)}{n}')
        # print(123)
    # data = ''.join([f'{x+1}{chr(x+65)}' for x in range(8)])
    # if len(pos) == 2 and all(x in data for x in list(pos)):

    # if all(x in arr for x, arr in zip(pos, tmp)):
    #     print(123)
        # print(a in b)
    # if len(pos) == 2:
    #     a, b = list(pos)
    #     if a in [chr(x + 65) for x in range(8)] and b in [str(x + 1) for x in range(8)]:
    #     # all(x in data for x in list(pos)):

    # x = [[f'{chr(i+64)}{j}' for j in range(1, 9)] for i in range(1, 9)]
    # x = [v for k in x for v in k]

    a, b = ord(pos[0]) - 65, int(pos[1]) - 1
    print(a, b)
    res = [[n for n in range(8)] for m in range(8)]
    res = [f'{chr(a+x+65)}{b+x+1}' for x in range(9 - max(a, b)+2)]

    return res
    # print(a, b)


q = 'A4'
result = available_moves(q)
# boards = [['-']*8 for _ in range(8)]
print(result)
# for a, b in result:
#     boards[ord(a) - 65][int(b)-1] = 'X'
# boards[ord(q[0]) - 65][int(q[1])-1] = 'Q'
# for line in boards:
#     print(line)

a, b = 8, 3
a1, b1 = a - (min(a, b) - 1), b - (min(a, b) - 1)
a2, b2 = a + (min(a, b) - 1), b - (min(a, b) - 1)
print(a1, b1)
print([f'{chr(a1+x+64)}{b1+x}' for x in range(9 - max(a1, b1))])
print(a2, b2)
print([f'{chr(a2-x+64)}{b2+x}' for x in range(9 - max(a2, b2))])
