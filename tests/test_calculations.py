import pytest
from app.calculation.factory import CalculationFactory


@pytest.mark.parametrize(
    "op,a,b,expected",
    [
        ("add", 2, 3, 5),
        ("subtract", 5, 3, 2),
        ("multiply", 2, 4, 8),
        ("divide", 10, 2, 5),
    ],
)
def test_factory_create_and_compute(op, a, b, expected):
    calc = CalculationFactory.create(op, a, b)
    assert calc.operation_name == op
    assert calc.a == a
    assert calc.b == b
    assert calc.compute() == expected


def test_factory_unsupported_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create("power", 2, 3)
