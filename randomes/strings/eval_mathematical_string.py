"""
Учитывая математическое выражение в виде строки, вы должны вернуть результат
в виде числа. Число может быть как целым числом, так и/или десятичным числом.
То же самое касается возвращаемого результата.

Вам необходимо поддерживать следующие математические операторы:
'+', '-', '*', '/', а так же скобки и унарный '-'.
"""

import re
import ast
import operator
from functools import reduce


def calc1(expression: str) -> int | float:
    """Вычисляет математическое выражение в строке."""

    binops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Div: operator.truediv,
        ast.Mult: operator.mul,
    }

    unops = {
        ast.USub: operator.neg,
    }

    def _eval(node: ast.parse) -> float | None:
        """Парсит строку и производит вычисления."""
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant):
            return float(node.value)
        if isinstance(node, ast.UnaryOp):
            return unops[type(node.op)](_eval(node.operand))
        if isinstance(node, ast.BinOp):
            return binops[type(node.op)](*map(_eval, (node.left, node.right)))

        return None

    result = _eval(ast.parse(expression, mode='eval'))

    return int(result) if result.is_integer() else result


def calc2(expression: str) -> int | float:
    """Вычисляет математическое выражение в строке."""
    binops = {
        '-': operator.sub,
        '+': operator.add,
        '*': operator.mul,
        '/': operator.truediv,
    }

    ops = '\\'.join([' ', *binops]).strip()

    def _eval(node: str) -> float:
        """Парсит строку и производит вычисления."""

        # замена подряд идущих знаков "+" и "-" на один
        for i, val in enumerate(['+-', '--']):
            node = node.replace(val, ['-', '+'][i])

        # раскрытие скобок в выражении
        if re.search(r'[\(\)]', node):
            tmp = {'(': 0, ')': 0}

            # поиск парной скобки
            for i, v in enumerate(node):
                if tmp.get(v) is not None:
                    tmp[0] = tmp.get(0, i)
                    tmp[v] += 1
                if reduce(lambda a, b: a and a == b, list(tmp.values())[:2]):
                    break

            return _eval(''.join([
                f'{node[:tmp[0]]}',
                f'{_eval(node[tmp[0]+1:i])}',
                f'{node[i+1:]}',
            ]))

        # вычисление выражения
        for i in range(0, 8, 4):
            if len(sch := re.split(f'(?<=\d)([{ops[i:i+4]}])', node)) > 1:
                return binops[sch[-2]](*map(_eval, (''.join(sch[:-2]), sch[-1])))

        return float(node)

    result = _eval("".join(expression.split()))
    return int(result) if result.is_integer() else result


def test() -> None:
    """Тестирование работы алгоритмов."""
    cases = (
        ("1 + 1", 2),
        ("8/16", 0.5),
        ("3 -(-1)", 4),
        ("2 + -2", 0),
        ("10- 2- -5", 13),
        ("(((10)))", 10),
        ("3 * 5", 15),
        ("-7 * -(6 / 3)", 14)
    )

    for case, val in cases:
        assert calc1(case) == val
        assert calc2(case) == val


if __name__ == '__main__':
    test()
