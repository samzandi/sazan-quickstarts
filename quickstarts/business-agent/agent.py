from data import get_business
from engine import analyze
from models import BusinessAnalysis


def run_analysis(business_id: str) -> BusinessAnalysis:
    data = get_business(business_id)
    if data is None:
        return BusinessAnalysis(
            business_id=business_id,
            revenue=None,
            variable_cost=None,
            contribution_margin=None,
            operating_result=None,
            break_even_units=None,
            assumptions=(),
            supported=False,
            reason="unknown_business_id",
        )
    return analyze(data)
