"""
Фон

Если на кнопках вашего телефона есть буквы, то длинные телефонные номера легко запомнить,
составив слова из заменяемых цифр.

https://en.wikipedia.org/wiki/Phoneword


Это характерно для номеров 1-800.
Формат чисел 1-800

Этот формат, вероятно, различается в разных странах, но для целей этой Ката вот мои правила:

Номер 1-800 — это 11-значный телефонный номер, который начинается с 1-800префикс.

Остальные 7 цифр можно записать в виде комбинации слов из 3 или 4 букв. например

    1-800-CODE-WAR
    1-800-NEW-KATA
    1-800-GOOD-JOB

The -включены только для улучшения читаемости.
История

Местная компания решила зарезервировать номер 1-800, чтобы помочь с рекламой.

Они уже выбрали, какие слова хотят использовать, но обеспокоены тем, что, возможно, тот же номер
телефона может означать и другие слова. Возможно, плохие слова. Возможно, неловкие слова.

Им нужен кто-то, кто их проверит, чтобы избежать случайных пиар-скандалов!

Вот тут-то ты и заходишь...
Задача сказала

Существует предварительно загруженный массив слов из 3 и 4 букв (заглавных):

    Для Python это: WORDS

Учитывая номер 1-800 (телефонное слово), который компания хочет использовать, вам необходимо
проверить все известные слова и вернуть набор всех возможных номеров 1-800, которые можно
сформировать с использованием тех же цифр.

Примечания
    Желаемый номер телефона, предоставленный компанией, имеет правильный формат. Нет необходимости
    проверять.
    Все буквы в верхнем регистре. Нет необходимости проверять.
    Разрешены только слова из списка.

"""

from itertools import product as pd


WORDS = [
    "ACT", "ADD", "ALL", "APE", "AND", "ANN", "ANY", "ANT", "ARE", "ART", "ASS",
    "BAD", "BAR", "BAT", "BAY", "BEE", "BIG", "BIT", "BOB", "BOY", "BUN", "BUT",
    "CAN", "CAR", "CAT", "COT", "COW", "CUT",
    "DAD", "DAY", "DEW", "DID", "DIN", "DOG", "DON", "DOT", "DUD",
    "EAR", "EAT", "EEL", "EGG", "ERR", "EYE",
    "FAG", "FAR", "FLY", "FOR", "FUN", "FUR",
    "GAY", "GET", "GOT", "GUM", "GUN", "GUY", "GUT", "GYM",
    "HAS", "HAT", "HER", "HEY", "HIM", "HIS", "HIT", "HOW", "HUG", "HUN",
    "ICE", "INK", "ITS", "IVE",
    "JAN", "JET", "JOB", "JOT", "JOY",
    "KEY",
    "LAP", "LAY", "LIE", "LET", "LOG",
    "MAN", "MAP", "MAY", "MEN", "MOM", "MUD", "MUM",
    "NAP", "NEW", "NOD", "NOT", "NOW",
    "OAR", "ODD", "OFF", "OLD", "ONE", "OUR", "OUT",
    "PAN", "PAL", "PAT", "PAW", "PEN", "PET", "PIG", "PIT", "POT", "PRO", "PUT",
    "QUO",
    "RAG", "RAM", "RAN", "RAP", "RAT", "RED", "RIP", "ROD", "ROT", "RUN", "RUT",
    "SAT", "SAW", "SAY", "SEA", "SEE", "SEX", "SHE", "SOY", "SUN", "SUX",
    "TAN", "TAT", "TEA", "THE", "TIN", "TIP", "TIT", "TON", "TOP", "TOO", "TWO",
    "URN", "USE",
    "VAN", "VET", "VIP",
    "WAR", "WAS", "WAY", "WED", "WHO", "WHY", "WIN", "WON",
    "XXX",
    "YAK", "YAM", "YAP", "YOU", "YUM",
    "ZAP", "ZIP", "ZIT", "ZOO",

    # Four letter words
    "ABLE", "ACED", "AGOG", "AHEM", "AHOY", "ALLY", "AMEN", "ANTI", "ANTS", "ANUS",
    "APES", "ARMY", "ARSE", "ARTY", "AVID", "AWED",
    "BABY", "BARS", "BATS", "BAYS", "BEAR", "BEES", "BILL", "BITE", "BITS", "BLOW",
    "BLUE", "BOLD", "BONE", "BOOB", "BOOM", "BOSS", "BOYS", "BUFF", "BUNG", "BUNS",
    "BUMS", "BURP", "BUST", "BUSY", "BUZZ",
    "CANS", "CANT", "CARS", "CART", "CATS", "CHAP", "CHIC", "CHUM", "CIAO", "CLAP",
    "COCK", "CODE", "COOL", "COWS", "COZY", "CRAB", "CREW", "CURE", "CULT",
    "DADS", "DAFT", "DAWN", "DAYS", "DECK", "DEED", "DICK", "DING", "DOGS", "DOTS",
    "DOLL", "DOLT", "DONG", "DOPE", "DOWN", "DRAW", "DUCK", "DUDE", "DUMB", "DUTY",
    "EARL", "EARN", "EARS", "EASY", "EATS", "EDGE", "EELS", "EGGS", "ENVY", "EPIC",
    "EYES",
    "FACE", "FAGS", "FANG", "FARM", "FART", "FANS", "FAST", "FEAT", "FEET", "FISH",
    "FIVE", "FIZZ", "FLAG", "FLEW", "FLIP", "FLOW", "FOOD", "FORT", "FUCK", "FUND",
    "GAIN", "GEEK", "GEMS", "GIFT", "GIRL", "GIST", "GIVE", "GLEE", "GLOW", "GOLD",
    "GOOD", "GOSH", "GRAB", "GRIN", "GRIT", "GROT", "GROW", "GRUB", "GUNS", "GUSH",
    "GYMS",
    "HAIL", "HAIR", "HALO", "HANG", "HATS", "HEAD", "HEAL", "HEIR", "HELL", "HELP",
    "HERE", "HERO", "HERS", "HIGH", "HIRE", "HITS", "HOLY", "HOPE", "HOST", "HUNK",
    "HUGE", "HUNG", "HUNS", "HURT",
    "ICON", "IDEA", "IDLE", "IDOL", "IOTA",
    "JAZZ", "JERK", "JESS", "JETS", "JINX", "JOBS", "JOHN", "JOKE", "JUMP", "JUNE",
    "JULY", "JUNK", "JUST",
    "KATA", "KEYS", "KICK", "KIND", "KING", "KISS", "KONG", "KNOB", "KNOW",
    "LARK", "LATE", "LEAN", "LICE", "LICK", "LIKE", "LION", "LIVE", "LOGS", "LOCK",
    "LONG", "LOOK", "LORD", "LOVE", "LUCK", "LUSH",
    "MAKE", "MANY", "MART", "MATE", "MAXI", "MEEK", "MIKE", "MILD", "MINT", "MMMM",
    "MOMS", "MOOD", "MOON", "MOOT", "MUCH", "MUFF", "MUMS", "MUTT",
    "NAPS", "NAZI", "NEAT", "NECK", "NEED", "NEWS", "NEXT", "NICE", "NICK", "NOON",
    "NOSE", "NOTE",
    "OARS", "OATS", "ONCE", "ONLY", "OPEN", "ORGY", "OVAL", "OVER",
    "PANS", "PALS", "PART", "PAST", "PATS", "PAWS", "PEAR", "PERT", "PENS", "PETS",
    "PHEW", "PIPE", "PIPS", "PLAN", "PLUM", "PLUS", "POET", "POOF", "POOP", "POSH",
    "POTS", "PROS", "PSST", "PUKE", "PUNK", "PURE", "PUSH", "PUSS",
    "QUAD", "QUAK", "QUID", "QUIT",
    "RANT", "RAPE", "RAPS", "RAPT", "RATE", "RAMS", "RATS", "REAP", "RICK", "RING",
    "RIPE", "ROOT", "ROSE", "ROSY", "ROTS", "RUNT", "RUTS",
    "SAFE", "SAGE", "SANE", "SAVE", "SAWS", "SEEK", "SEXY", "SHAG", "SHIT", "SICK",
    "SIGH", "SIRE", "SLAG", "SLIT", "SLUT", "SNAP", "SNOG", "SNUG", "SOFT", "SOON",
    "SOUL", "SOUP", "SPRY", "STIR", "STUN", "SUCK", "SWAG", "SWAY",
    "TACT", "TANK", "TANS", "THAT", "THIS", "TIME", "TINS", "TINY", "TITS", "TOES",
    "TONS", "TONY", "TOPS", "TOYS",
    "UBER", "URNS", "USED", "USER", "USES",
    "VAIN", "VAMP", "VARY", "VEIN", "VENT", "VERY", "VEST", "VIEW", "VIVA", "VOLT",
    "VOTE",
    "WAFT", "WAGE", "WAKE", "WALK", "WALL", "WANG", "WANK", "WANT", "WARD", "WARM",
    "WARP", "WARS", "WART", "WASH", "WAVE", "WEAR", "WEDS", "WEED", "WEEN", "WELD",
    "WHAT", "WHEE", "WHEW", "WHIP", "WHIZ", "WHOA", "WIFE", "WILL", "WIND", "WING",
    "WINK", "WINS", "WIRE", "WISH", "WITH", "WORD", "WORK", "WRAP",
    "XMAN", "XMEN", "XRAY", "XTRA", "XXXX",
    "YANK", "YAKS", "YAMS", "YAPS", "YARD", "YARN", "YELP", "YERN", "YOKE", "YOLK",
    "YULE",
    "ZANY", "ZAPS", "ZIPS", "ZITS", "ZERO", "ZOOM", "ZOOS"
]


def check1800(s: str) -> set:
    """
    Поиск схожих номеров телеонов.
    """
    x = [next(x for x in 'ABC DEF GHI JKL MNO PQRS TUV WXYZ'.split() if w in x) for w in s.replace('-', '')[4:]]
    w = [[[r for x in pd(*w) if (r := ''.join(x)) in WORDS] for w in c] for c in [(x[:[3, 4][i]], x[[3, 4][i]:]) for i in range(2)]]
    return {'-'.join(('1', '800') + x) for n in [pd(*c) for c in w] for x in n}


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("1-800-CODE-WAR", {"1-800-CODE-WAR", "1-800-CODE-YAP",
         "1-800-CODE-WAS", "1-800-CODE-ZAP"}),
        ("1-800-BOY-ARMY", {"1-800-BOY-ARMY", "1-800-COW-ARMY", "1-800-ANY-ARMY"}),
        ("1-800-INK-WANT", {"1-800-INK-WANT", "1-800-HOLY-ANT", "1-800-HOLY-COT"}),
        ("1-800-WORD-WTF", set()),
        ("1-800-WORD-TTT", set()),
        ("1-800-QQQQ-YOU", set()),
        ("1-800-XXXX-XXX", {"1-800-XXXX-XXX", "1-800-XXX-XXXX"}),
        ("1-800-OUR-MUTT", {"1-800-OUR-MUTT"}),
        ("1-800-SEX-TOYS", {"1-800-SEX-TOYS"}),
        ("1-800-GOOD-JOB", {"1-800-GOOD-JOB"}),
        ("1-800-FUN-KATA", {"1-800-FUN-KATA"}),
        ("1-800-BIG-JOHN", {"1-800-BIG-JOHN"}),
        ("1-800-SUX-EGGS", {"1-800-SUX-EGGS"}),
    )
    for key, val in data:
        assert check1800(key) == val


if __name__ == '__main__':
    test()
