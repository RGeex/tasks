"""
В генетике две разные последовательности ДНК могут кодировать один и тот же белок.

Это связано с избыточностью генетического кода; фактически, два разных тринуклеотида могут кодировать одну
и ту же аминокислоту.
Например, тринуклеотид «TTT» и тринуклеотид «TTC» оба кодируют аминокислоту «F».
Для получения дополнительной информации вы можете ознакомиться здесь .

Ваша задача в этом задании — определить, кодируют ли две разные последовательности ДНК один и тот же белок.
Ваша функция принимает две последовательности, которые вы должны сравнить. Для простоты, последовательности
здесь будут подчиняться следующим правилам:

Это полная последовательность белка, начинающаяся со стартового кодона и заканчивающаяся стоп-кодоном.
Она будет содержать только действительные тринуклеотиды.
"""
import unittest
from typing import Any, Callable, Tuple
import re
from operator import eq


codons = {'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCT': 'A', 'GCC': 'A',
          'GCA': 'A', 'GCG': 'A', 'TAT': 'Y', 'TAC': 'Y', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'TAA': '*', 'TGA': '*', 'TAG': '*'}


def code_for_same_protein(seq1: str, seq2: str) -> bool:
    """
    Определяет, кодируют ли две разные последовательности ДНК один и тот же белок.
    """
    return all(codons[seq1[c:c + 3]] == codons[seq2[c:c + 3]] for c in range(0, len(seq1), 3))


def code_for_same_protein_2(seq1: str, seq2: str) -> bool:
    """
    Определяет, кодируют ли две разные последовательности ДНК один и тот же белок.
    """
    return eq(*map(lambda x: list(map(codons.get, re.findall("...", x))), (seq1, seq2)))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(code_for_same_protein, (
        (("ATGTCGTCAATTTAA", "ATGTCGTCAATTTAA"), True),
        (("ATGTTTTAA", "ATGTTCTAA"), True),
        (("ATGTTTTAA", "ATGATATAA"), False),
        (("ATGTTTTAA", "ATGATATAA"), False),
        (("ATGTTTGGGAATAATTAAGGGTAA", "ATGTTCGGGAATAATGGGAGGTAA"), False),
    ))
    test(code_for_same_protein_2, (
        (("ATGTCGTCAATTTAA", "ATGTCGTCAATTTAA"), True),
        (("ATGTTTTAA", "ATGTTCTAA"), True),
        (("ATGTTTTAA", "ATGATATAA"), False),
        (("ATGTTTTAA", "ATGATATAA"), False),
        (("ATGTTTGGGAATAATTAAGGGTAA", "ATGTTCGGGAATAATGGGAGGTAA"), False),
    ))
