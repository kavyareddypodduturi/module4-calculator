from dataclasses import dataclass
from typing import Callable

@dataclass
class Calculation:
    operation_name: str
    a: float
    b: float
    operation: Callable[[float, float],float]

    def compute(self) -> float:
        return self.operation(self.a, self.b)