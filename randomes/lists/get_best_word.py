"""
Вы играете в скраббл. Но подсчитывать очки сложно.

Вы решаете создать небольшой скрипт для расчета наилучшего возможного значения.

Функция принимает два аргумента:

    `points`: массив целых чисел, представляющий для каждой буквы от A до Z очки, которые он платит.
    `words`: массив строк, в верхнем регистре.


Вы должны вернуть индекс самого короткого слова, получившего наивысший балл.

Если длина и оценка одинаковы для двух элементов, верните индекс первого.

"""


def get_best_word(points: tuple, words: list) -> int:
    """
    Поиск индекса с максимальным значением очков и минимальной длине слова.
    """
    return max(range(len(words)), key=lambda x: (sum(points[ord(w)-65] for w in words[x]), -len(words[x])))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    points = (1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 10, 1, 2, 1, 1, 3, 8, 1, 1, 1, 1, 4, 10, 10, 10, 10)
    data = (
        (["WHO", "IS", "THE", "BEST", "OF", "US"], 0),
        (["AABCDEF", "WHO", "IS", "THE", "BEST", "OF", "US"], 1),
        (["NOQ", "TXAY", "S", "OM", "ESFT", "CJUKQ", "QL", "QO", "ASTK", "Y"], 5),
        (["N", "AO", "TQGZW", "P", "OBTP", "CLWXB", "Y", "JQGFJ", "Q", "RP", "OC", "MRQCZ", "ZWN", "ZRT", "OIRYH", "GWPMSZP", "LQRYUKQ", "LBM", "LFEI", "VHUX", "RTALLIC",
          "JEMUPS", "XUW", "X", "ZLXFMWS", "LFAGR", "HJ", "RTUAI", "JRBNG", "ZUYSC", "CIEYV", "FUY", "B", "EJS", "CINBTQS", "JEAC", "JX", "LLILSEK", "W", "KLUV"], 16),
        (["SVWLIDP", "FCPKTHW", "EREMN", "NFEF", "PQ", "FSC", "ZYPOSXJ", "BOR", "YCGG", "RC", "DVPE", "VAOE", "OIGK", "OTQE", "REJFUFD", "FVBCSSB", "VHJ", "BEC", "MWZQ", "WX", "L", "ZPCB", "JKLHE", "RYFTY", "NKP", "ID", "O", "KA", "VRXX", "NTDB", "OERKPC", "YFLUI", "SKQCJ", "PXDSW", "ITYWD", "TC", "LOIDQEJ", "NE", "YND", "VJHOCEC", "RPRANZ", "BQ", "STM", "RGVBFW",
          "SMWUYLW", "KT", "SXHY", "XCE", "T", "SC", "UDJU", "CHDR", "UGXNQ", "CQOOBA", "O", "NWW", "V", "L", "BAQ", "AZN", "LBTR", "N", "QSURR", "KADPH", "M", "LCBEAKM", "ZHEVXS", "F", "TVAIQCY", "MF", "KCI", "YQ", "RCG", "AKYPCP", "WJXG", "RQXOI", "SJI", "TWXZ", "J", "HIKCGHV", "EAAXGG", "AETSH", "EO", "BUET", "TDIQCO", "TKL", "FJCRY", "ZHAJLK", "OLMCVA", "F"], 6),
        (["RBBL", "ZJ", "ZOFXE", "LMBFCFX", "O", "JG", "SYRYE", "VXG", "EU", "DAIFZR", "BQUNZHH",
          "WKO", "TFPHPLX", "SWLG", "CY", "JYQNDSM", "ITPS", "B", "UVSDMWR", "LCPS"], 15),
        (['LGVMJDW', 'HSPASA', 'CFHMVZNGH', 'ESKSKB', 'JDO', 'BQJUECZ', 'BB', 'IVVLXBC', 'ZRENSWMG'], 5),
    )
    for key, val in data:
        assert get_best_word(points, key) == val


if __name__ == '__main__':
    test()
