from typing import Dict, Callable
from app.calculation.calculation import Calculation
from app.operation.operations import add,subtract, multiply, divide

class CalculationFactory:
    operations: Dict[str, Callable[[float, float], float]] = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    @classmethod
    def create(cls, operation_name: str, a:float, b:float) -> Calculation:
        if operation_name not in cls.operations:
            raise ValueError(f" does not support the operation: {operation_name}")
        
        operation_function = cls.operations[operation_name]
        return Calculation(operation_name, a, b, operation_function)
