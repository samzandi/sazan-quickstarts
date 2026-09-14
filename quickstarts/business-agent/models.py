from dataclasses import dataclass


@dataclass(frozen=True)
class BusinessInput:
    business_id: str
    monthly_units: int
    unit_price: float
    unit_variable_cost: float
    monthly_fixed_cost: float


@dataclass(frozen=True)
class BusinessAnalysis:
    business_id: str
    revenue: float | None
    variable_cost: float | None
    contribution_margin: float | None
    operating_result: float | None
    break_even_units: int | None
    assumptions: tuple[str, ...]
    supported: bool
    reason: str | None = None
