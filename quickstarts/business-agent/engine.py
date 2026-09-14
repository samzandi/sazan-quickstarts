import math

from models import BusinessAnalysis, BusinessInput


def analyze(data: BusinessInput) -> BusinessAnalysis:
    if data.monthly_units < 0 or data.unit_price < 0 or data.unit_variable_cost < 0 or data.monthly_fixed_cost < 0:
        return BusinessAnalysis(
            business_id=data.business_id,
            revenue=None,
            variable_cost=None,
            contribution_margin=None,
            operating_result=None,
            break_even_units=None,
            assumptions=(),
            supported=False,
            reason="invalid_negative_input",
        )

    contribution_per_unit = data.unit_price - data.unit_variable_cost
    if contribution_per_unit <= 0:
        return BusinessAnalysis(
            business_id=data.business_id,
            revenue=data.monthly_units * data.unit_price,
            variable_cost=data.monthly_units * data.unit_variable_cost,
            contribution_margin=data.monthly_units * contribution_per_unit,
            operating_result=data.monthly_units * contribution_per_unit - data.monthly_fixed_cost,
            break_even_units=None,
            assumptions=(
                "monthly_units is treated as stable for the analysis period",
                "unit price and costs are treated as constant",
            ),
            supported=False,
            reason="no_positive_unit_contribution",
        )

    revenue = data.monthly_units * data.unit_price
    variable_cost = data.monthly_units * data.unit_variable_cost
    contribution_margin = revenue - variable_cost
    operating_result = contribution_margin - data.monthly_fixed_cost
    break_even_units = math.ceil(data.monthly_fixed_cost / contribution_per_unit)

    return BusinessAnalysis(
        business_id=data.business_id,
        revenue=revenue,
        variable_cost=variable_cost,
        contribution_margin=contribution_margin,
        operating_result=operating_result,
        break_even_units=break_even_units,
        assumptions=(
            "monthly_units is treated as stable for the analysis period",
            "unit price and costs are treated as constant",
            "taxes, financing costs, and exceptional items are excluded",
        ),
        supported=True,
    )
