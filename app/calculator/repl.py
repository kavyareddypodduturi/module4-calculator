from __future__ import annotations

from typing import List

from app.calculation.factory import CalculationFactory
from app.calculation.calculation import Calculation


HELP_TEXT = """Commands:
  add, subtract, multiply, divide   Perform calculations
  help                             Show this help message
  history                          Show calculation history
  exit                             Quit the calculator

Usage examples:
  add 2 3
  divide 10 2
"""


def parse_command(user_input: str) -> tuple[str, float, float] | None:
    """
    Parse a single-line command like: 'add 2 3'

    Returns:
        (operation, a, b) if valid
        None if the input is not a calculation command
    """
    parts = user_input.strip().split()
    if len(parts) != 3:
        return None  # LBYL: check format first

    op = parts[0].lower()

    try:  # EAFP: try converting to numbers
        a = float(parts[1])
        b = float(parts[2])
    except ValueError as exc:
        raise ValueError("Numbers must be valid numeric values.") from exc

    return op, a, b


def format_history(history: List[Calculation]) -> str:
    """Return a readable history string."""
    if not history:
        return "No calculations yet."
    lines = []
    for c in history:
        lines.append(f"{c.operation_name} {c.a} {c.b} = {c.compute()}")
    return "\n".join(lines)


def repl() -> None:  # pragma: no cover
    """Run the calculator REPL."""
    history: List[Calculation] = []
    print("Calculator started. Type 'help' for instructions.")

    while True:
        user_input = input("> ").strip()
        if not user_input:
            continue

        command = user_input.lower()

        if command == "help":
            print(HELP_TEXT)
            continue

        if command == "history":
            print(format_history(history))
            continue

        if command == "exit":
            print("Goodbye!")
            break

        try:
            parsed = parse_command(user_input)
            if parsed is None:
                print("Invalid input. Type 'help' for usage.")
                continue

            op, a, b = parsed
            calc = CalculationFactory.create(op, a, b)
            result = calc.compute()
            history.append(calc)
            print(result)

        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
