"""
В этом ката вам будет предоставлен список строк, и ваша задача будет состоять
в том, чтобы найти строки, имеющие одинаковые символы, и вернуть сумму их
позиций следующим образом:

solve(["abc","abbc", "ab", "xyz", "xy", "zzyx"]) = [1,8]
-- мы видим, что элементы с индексами 0 и 1 имеют те же символы, что и элементы с индексами 3 и 5.
-- поэтому мы возвращаем [1,8], потому что [0+1,3+5] = [1,8]. Этот результат отсортирован. 
-- игнорируйте те, у которых нет хотя бы одного подходящего партнера, например «ab» и «xy».

Another example...
solve(["wkskkkkkk","fokoo","wkskk","uizzzz","fokooff","wkskkkk","uizzzzzzz"]),[5,7,9]);
--Элемент с индексом 0 аналогичен элементам с индексами 2 и 5; итак 0+2+5=7.
--Элемент с индексом 1 аналогичен элементу с индексом 4; итак 1+4=5. 
--Элемент с индексом 3 аналогичен элементу с индексом 6; итак 3+6=9.
--Результат необходимо отсортировать. Получаем [5,7,9].

"""


def find_indexes(s: list[str]) -> list[int]:
    """
    Поиск индексов массива с одинаковыми наборами символов.
    """
    return (t := []) or sorted(([i+x-1 for i, m in enumerate(s, 1) if (x := sum(t.append(j) or j for j, n in enumerate(s[i:], i) if j not in t and set(n) == set(m)))]))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (["abc","abbc","ab","xyz","xy","zzyx"],[1,8]),
        (['wkskkkkkk','fokoo','wkskk','uizzzz','fokooff','wkskkkk','uizzzzzzz'],[5,7,9]) ,
        (['xhuhhh','dghgg','dghgghh','mrerrrrrr','xhuhhhhhh','mrerrr'],[3,4,8]),
        (['uczcccccc','idffffiii','pnjjjjjjj','pnjjjj','idffff','uczcccc','uczcc'],[5,5,11]),
        (['rvjvvvv','mihhhh','mihhhhmmm','rvjvv','wsnssww','wsnss'],[3,3,9]),
        (['ayqqqq','epqqqqqqq','epqqqqqqqqqq','rdsddss','ayqqqqqqq','epqqqq','rdsdd'],[4,8,9]),
    )
    for key, val in data:
        assert find_indexes(key) == val


if __name__ == '__main__':
    test()
