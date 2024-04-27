"""
Все знают пароли. Парольные фразы можно выбирать из стихов, песен, названий фильмов и т. д., но часто их можно угадать по общим культурным отсылкам. Вы можете сделать свои парольные фразы более надежными разными способами. Один из них следующий:

выберите текст заглавными буквами, включающий или не включающий цифры и неалфавитные символы,

    сдвинуть каждую букву на заданное число, но преобразованная буква должна быть буквой (круговой сдвиг),
    заменить каждую цифру ее дополнением до 9,
    сохраняйте такие символы, как небуквенные и нецифровые символы,
    уменьшите каждую букву в нечетной позиции, пропишите каждую букву в четной позиции (первый символ находится в позиции 0),
    полностью изменить результат.

Пример:

your text: "BORN IN 2015!", shift 1

1 + 2 + 3 -> "CPSO JO 7984!"

4 "CpSo jO 7984!"

5 "!4897 Oj oSpC"

При более длинных парольных фразах лучше иметь небольшую и простую программу. Вы бы это написали? 
"""


def play_pass(s: str, n: int) -> str:
    """
    Шифрование строки по заданному алгоритму.
    """
    r = []
    for i, x in enumerate(s):
        x = chr(65 + ((ord(x) - 65 + n) % 26)) if x.isalpha() else str(9 - int(x)) if x.isdigit() else x
        r.append(x.lower() if i % 2 else x)
    return ''.join(r[::-1])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("I LOVE YOU!!!", 1), "!!!vPz fWpM J"),
        (("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2), "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO"),
        (("AAABBCCY", 1), "zDdCcBbB"),
        (("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2), "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO"),
        (("TO BE HONEST WITH YOU I DON'T USE THIS TEXT TOOL TOO OFTEN BUT HEY... MAYBE YOUR NEEDS ARE DIFFERENT.", 5), ".ySjWjKkNi jWf xIjJs wZtD JgDfR ...dJm yZg sJyKt tTy qTtY YcJy xNmY JxZ Y'StI N ZtD MyNb yXjStM Jg tY"),
        (("IN 2012 TWO CAMBRIDGE UNIVERSITY RESEARCHERS ANALYSED PASSPHRASES FROM THE AMAZON PAY SYSTEM...", 20), "...gYnMsM SuJ HiTuGu yBn gIlZ MyMuLbJmMuJ XyMsFuHu mLyBwLuYmYl sNcMlYpChO YaXcLvGuW IqN 7897 hC"),
        (("IN 2012 TWO CAMBRIDGE UNIVERSITY RESEARCHERS ANALYSED PASSPHRASES FROM THE AMAZON PAY SYSTEM...", 10), "...wOdCiC IkZ XyJkWk oRd wYbP CoCkBrZcCkZ NoCiVkXk cBoRmBkOcOb iDsCbOfSxE OqNsBlWkM YgD 7897 xS"),
        (("1ONE2TWO3THREE4FOUR5FIVE6SIX7SEVEN8EIGHT9NINE", 5), "JsNs0yMlNj1sJaJx2cNx3jAnK4WzTk5jJwMy6tBy7jSt8"),
        (("AZ12345678ZA", 1), "bA12345678aB"),
        (("!!!VPZ FWPM J", 25), "I LoVe yOu!!!"),
        (("BOY! YOU WANTED TO SEE HIM? IT'S YOUR FATHER:-)", 15),")-:gTwIpU GjDn h'iX ?bXw tTh dI StIcPl jDn !NdQ"),
        (("FOR THIS REASON IT IS RECOMMENDED THAT PASSPHRASES NOT BE REUSED ACROSS DIFFERENT OR UNIQUE SITES AND SERVICES.", 15), ".hTrXkGtH ScP HtIxH TjFxCj gD IcTgTuUxS HhDgRp sThJtG Tq iDc hThPgWeHhPe iPwI StScTbBdRtG Hx iX CdHpTg hXwI GdU"),
        (("ONCE UPON A TIME YOU DRESSED SO FINE (1968)", 12), ")1308( qZuR Ae pQeEqDp gAk qYuF M ZaBg qOzA"),
        (("AH, YOU'VE GONE TO THE FINEST SCHOOL ALL RIGHT, MISS LONELY", 12), "KxQzAx eEuY ,fTsUd xXm xAaToE FeQzUr qTf aF QzAs qH'GaK ,tM"),
        (("THE SPECIES, NAMED AFTER THE GREEK GOD OF THE UNDERWORLD, LIVES SOME 3,600 FEET UNDERGROUND.", 8), ".LvCwZoZmLvC BmMn 993,6 mUwA AmDqT ,lTzWeZmLvC MpB Nw lWo sMmZo mPb zMbNi lMuIv ,AmQkMxA MpB"),
    )
    for key, val in data:
        assert play_pass(*key) == val


if __name__ == '__main__':
    test()
