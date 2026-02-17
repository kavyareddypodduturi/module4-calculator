import builtins
from app.calculator.repl import parse_command, format_history
from app.calculation.calculation import Calculation
from app.operation.operations import add


def test_parse_command_valid():
    op, a, b = parse_command("add 2 3")
    assert op == "add"
    assert a == 2.0
    assert b == 3.0


def test_parse_command_invalid_format():
    assert parse_command("add 2") is None


def test_format_history_empty():
    assert format_history([]) == "No calculations yet."


def test_format_history_with_values():
    calc = Calculation("add", 2, 3, add)
    result = format_history([calc])
    assert "add 2 3 = 5" in result
