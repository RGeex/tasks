"""
Завершите решение так, чтобы оно возвращало количество раз, когда искомый_текст встречается в
полном_тексте.

search_substr( full_text, search_text, allow_overlap = True )

так что перекрывающиеся решения (не) учитываются. Если searchText пуст, он должен вернуть 0.
Примеры использования:

search_substr('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
search_substr('aaabbbcccc', 'bbb') # should return 1
search_substr( 'aaa', 'aa' ) # should return 2
search_substr( 'aaa', '' ) # should return 0
search_substr( 'aaa', 'aa', False ) # should return 1
"""
import typing


def search_substr(st: str, sf: str, rep: bool = True, res: int = 0) -> int:
    """
    Подсчитывает кол-во вхождений подстроки в строку, учитывая или не учитывая перкрывания.
    """
    return search_substr(st[x + (not rep and len(sf) != 1):], sf, rep, res + 1) if st and sf and (x := st.find(sf) + 1) else res


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""
    import unittest

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(search_substr, (
        (('ccbcbccacaaaaccabcacaccbaca', 'c'), 13),
        (('aa_bb_cc_dd_bb_e', 'bb'), 2),
        (('aaabbbcccc', 'bbb'), 1),
        (('aaacccbbbcccc', 'cc'), 5),
        (('aaa', 'aa'), 2),
        (('aaa', 'aa', False), 1),
        (('aaabbbaaa', 'bb', False), 1),
        (('a', ''), 0),
        (('', 'a'), 0),
        (('', ''), 0),
        (('', '', False), 0),
    ))
