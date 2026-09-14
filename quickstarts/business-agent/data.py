from models import BusinessInput


BUSINESSES = {
    "demo-shop": BusinessInput(
        business_id="demo-shop",
        monthly_units=120,
        unit_price=50.0,
        unit_variable_cost=20.0,
        monthly_fixed_cost=2400.0,
    ),
    "loss-case": BusinessInput(
        business_id="loss-case",
        monthly_units=100,
        unit_price=10.0,
        unit_variable_cost=12.0,
        monthly_fixed_cost=500.0,
    ),
}


def get_business(business_id: str) -> BusinessInput | None:
    return BUSINESSES.get(business_id)
