"""
ДНК – это биомолекула, несущая генетическую информацию. Он состоит из четырех
различных строительных блоков, называемых нуклеотидами: аденина (А), тимина (Т),
цитозина (С) и гуанина (G). Две цепи ДНК соединяются, образуя двойную спираль,
при этом нуклеотиды одной цепи связываются с нуклеотидами другой цепи в
соответствующих положениях. Связь возможна только в том случае, если нуклеотиды
комплементарны: А всегда соединяется с Т, а С всегда соединяется с G.

Из-за асимметрии ДНК каждая цепь ДНК имеет связанное с ней направление. Две
нити двойной спирали направлены в противоположных друг другу направлениях,
которые мы называем направлениями «вверх-вниз» и «вниз-вверх».

Напишите функцию checkDNA который принимает две последовательности ДНК как
строки и проверяет, подходят ли они для формирования полностью комплементарной
двойной спирали ДНК. Функция должна возвращать логическое значение true если
они дополняют друг друга и false если имеется несоответствие последовательности
(Пример 1 ниже).

Примечание:

    Все последовательности будут иметь ненулевую длину и состоять только из
    A, T, C и G персонажи.
    Все последовательности будут даны в направлении вверх-вниз .
    Две сравниваемые последовательности могут иметь разную длину. Если это так,
    и одна цепь полностью связана с другой, и между ними нет несоответствия
    последовательности (пример 2 ниже), ваша функция все равно должна вернуть
    результат. true.
    Если обе нити связаны лишь частично (пример 3 ниже), функция должна
    вернуть false.

Пример 1:

seq1 = 'GTCTTAGTGTAGCTATGCATGC';  // NB up-down
seq2 = 'GCATGCATAGCTACACTACGAC';  // NB up-down

checkDNA (seq1, seq2);
// --> false

// Because there is a sequence mismatch at position 4:
// (seq1)    up-GTCTTAGTGTAGCTATGCATGC-down
//              ||| ||||||||||||||||||
// (seq2)  down-CAGCATCACATCGATACGTACG-up

Пример 2:

seq1 = 'GCGCTGCTAGCTGATCGA';             // NB up-down
seq2 = 'ACGTACGATCGATCAGCTAGCAGCGCTAC';  // NB up-down

checkDNA (seq1, seq2);
// --> true

// Because one strand is entirely bonded by the other:
// (seq1)       up-GCGCTGCTAGCTGATCGA-down
//                 ||||||||||||||||||
// (seq2)  down-CATCGCGACGATCGACTAGCTAGCATGCA-up

Пример 3:

seq1 = 'CGATACGAACCCATAATCG';  // NB up-down
seq2 = 'CTACACCGGCCGATTATGG';  // NB up-down

checkDNA (seq1, seq2);
// --> false

// Because both strands are only partially bonded:
// (seq1)  up-CGATACGAACCCATAATCG-down
//                      |||||||||
// (seq2)          down-GGTATTAGCCGGCCACATC-up

"""


def check_DNA(seq1: str, seq2: str) -> bool:
    """
    Проверяет, подходят переданные цепочки ДНК для формирования
    полностью комплементарной двойной спирали ДНК.
    """
    return min(seq1, seq2, key=len).translate(str.maketrans('ATCG', 'TAGC')) in max(seq2, seq1, key=len)[::-1]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = ( 
        (('GTCTTAGTGTAGCTATGCATGC', 'GCATGCATAGCTACACTACGAC'), False),
        (('ATGCTACG', 'CGTAGCAT'), True),
        (('AGTCTGTATGCATCGTACCC', 'GGGTACGATGCATACAGACT'), True),
        (('TGCTACGTACGATCGACGATCCACGAC', 'GTCGTGGATCGTCGATCGTACGTAGCA'), True),
        (('ATGCCTACGGCCATATATATTTAG', 'CTAAATATGTATGGCCGTAGGCAT'), False),
        (('GTCACCGA', 'TCGGCTGAC'), False),
    )
    for key, val in data:
        assert check_DNA(*key) == val


if __name__ == '__main__':
    test()
