"""
Учитывая математическое выражение в виде строки, вы должны вернуть результат
в виде числа. Число может быть как целым числом, так и/или десятичным числом.
То же самое касается возвращаемого результата.

Вам необходимо поддерживать следующие математические операторы:
'+', '-', '*', '/', а так же скобки и унарный '-'.
"""

import ast
import operator


def calc(expression: str):
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
        assert calc(case) == val


if __name__ == '__main__':
    test()
