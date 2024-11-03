"""
В некоторых языках, таких как китайский, японский и тайский, между словами нет
пробелов. Однако для большинства задач обработки естественных языков, таких как
разметка частей речи, требуются тексты, состоящие из сегментированных слов.
Простой и достаточно эффективный алгоритм разделения предложения на составные
слова называется «MaxMatch».

MaxMatch начинается с первого символа предложения и пытается найти самое
длинное допустимое слово, начинающееся с этого символа. Если слово не найдено,
первый символ считается самым длинным «словом», независимо от его
действительности. Чтобы найти остальные слова, MaxMatch затем рекурсивно
вызывается для всех оставшихся символов до тех пор, пока не останется ни одного
символа. Возвращается список всех найденных слов.

Итак, для строки "happyday", "happy" найден, потому что "happyday" не является
допустимым словом и не является "happyda", ни "happyd". Затем вызывается
MaxMatch. "day", и "day" найден. Результатом является список ["happy","day"] в
таком порядке.

Писать max_match, который принимает буквенно-цифровой символ без пробелов и
строчных букв. String в качестве входных данных и возвращает List из Strings
всех найденных слов в том порядке, в котором они были найдены. Все допустимые
слова находятся в Set VALID_WORDS, который содержит всего около 500 английских
слов.

Примечание. Этот алгоритм прост и лучше работает с китайским текстом, поэтому
примите тот факт, что некоторые слова будут сегментированы неправильно.
"""


VALID_WORDS = [
    "1", "1111", "1234", "4", "a", "about", "above", "abstraction", "adventure", "advised",
    "africa", "after", "again", "ago", "alive", "all", "alone", "always", "am", "amount", "an",
    "and", "any", "anyone", "anyway", "apple", "appreciated", "approaches", "are", "arrived",
    "as", "asia", "asked", "asking", "ass", "at", "attendance", "authority", "away", "babies",
    "back", "bad", "baggage", "be", "been", "best", "better", "bird", "blog", "blue", "body",
    "bold", "book", "borrowed", "bread", "broken", "brown", "bunny", "busy", "but", "buttered",
    "buy", "by", "calories", "camel", "can", "car", "caramel", "cats", "cheat", "check",
    "checked", "cheese", "chocolate", "christmas", "class", "clean", "clear", "clock",
    "clocks", "coherent", "colors", "combined", "combining", "come", "comes", "coming",
    "compensates", "completely", "conditions", "consumption", "cookies", "cool", "couldnt",
    "counting", "country", "cows", "crashing", "cream", "currently", "dark", "day",
    "decorated", "dentist", "dessert", "detailed", "diary", "did", "didnt", "different",
    "discovered", "do", "does", "dog", "doll", "donation", "donkey", "dont", "door", "drive",
    "each", "early", "easter", "eat", "eaters", "eating", "either", "else", "ended", "ends",
    "english", "enough", "environment", "ever", "everyone", "everything", "exciting", "fact",
    "fairy", "favorite", "fence", "find", "fine", "first", "fish", "flew", "floor", "folded",
    "for", "fox", "frame", "free", "freezer", "friday", "from", "front", "gem", "get",
    "getting", "glass", "glittering", "go", "gods", "going", "good", "goodbye", "got",
    "gotten", "great", "greatly", "green", "had", "hand", "handkerchief", "hands", "happy",
    "harder", "has", "hasnt", "have", "having", "he", "hear", "help", "her", "here", "hes",
    "high", "him", "his", "home", "hour", "house", "how", "however", "human", "hump", "hurry",
    "i", "ice", "id", "if", "ill", "impassable", "in", "information", "initially", "is", "isnt",
    "it", "italy", "its", "japanese", "jobs", "joe", "join", "jumps", "june", "just", "kite",
    "know", "lake", "laptop", "last", "later", "laugh", "lazy", "learning", "lease", "least",
    "leave", "legless", "let", "lets", "letter", "life", "like", "likes", "list", "little",
    "lizard", "long", "longer", "loss", "lot", "loud", "love", "lovely", "luck", "made", "make",
    "malls", "many", "maple", "mary", "math", "may", "me", "meal", "meet", "memory",
    "metaphysics", "middle", "midsent", "milk", "mind", "money", "more", "movie", "mum",
    "music", "my", "mysterious", "nancy", "neatly", "need", "never", "next", "nickname",
    "night", "no", "noisy", "nor", "not", "now", "of", "off", "officiates", "often", "oh", "old",
    "older", "on", "once", "one", "onesie", "only", "open", "or", "other", "otherwise", "our",
    "out", "outside", "over", "paints", "paper", "party", "passed", "pastels", "people",
    "perhaps", "person", "persons", "pets", "piano", "pie", "piece", "pig", "place", "places",
    "plan", "playing", "plays", "please", "poker", "popcorn", "pretty", "promotion", "proud",
    "purple", "quick", "quite", "rain", "ran", "random", "rather", "read", "real", "realise",
    "really", "reason", "recently", "recommend", "records", "red", "remember", "rent",
    "research", "returned", "revels", "right", "river", "roads", "rock", "roof", "room",
    "ruin", "said", "same", "sandwiches", "sauce", "saw", "saying", "says", "school", "seats",
    "see", "sentence", "sentences", "shake", "share", "she", "shooter", "shop", "shore",
    "short", "should", "shut", "sick", "sight", "sixtyfour", "sky", "slammed", "small", "so",
    "someone", "something", "sometimes", "song", "sounds", "speaks", "spend", "spotted",
    "stars", "start", "stay", "step", "still", "stole", "stop", "store", "story", "stranger",
    "striped", "subsequently", "sugar", "suit", "sunburnt", "sundays", "sure", "susan",
    "syrup", "table", "take", "taste", "teeth", "test", "than", "that", "the", "them", "there",
    "they", "thing", "things", "think", "thinking", "this", "thought", "thoughts", "three",
    "throughout", "time", "to", "toasted", "today", "together", "told", "tom", "tomato",
    "tomorrow", "too", "tooth", "town", "tries", "true", "try", "tuna", "turned", "twinkling",
    "two", "under", "unique", "until", "up", "us", "used", "vacant", "velocity", "very",
    "visited", "vividly", "voice", "wait", "walk", "want", "was", "wasnt", "waves", "way", "we",
    "wednesday", "weeks", "went", "were", "werent", "what", "when", "where", "white", "why",
    "will", "windows", "with", "within", "wont", "work", "works", "worm", "would", "wow",
    "writing", "wrote", "yeah", "year", "years", "yesterday", "yet", "you", "young", "your",
    "youre", "yourself",
]


def max_match(s: str, r: str='') -> list[str]:
    """
    Разделяет слова записанные слитно на раздельные.
    """
    x = next((x for i in range(len(s)) if s[:(x := -i or None)] in VALID_WORDS), 1)
    return max_match([s[x:], ''][not x], r + f' {s[:x]}') if s else r.split()


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("goodluck", ['good','luck']),
        ("ewingsa", ['e','w','in','g','s','a']),
    )
    for key, val in data:
        assert max_match(key) == val


if __name__ == '__main__':
    test()
