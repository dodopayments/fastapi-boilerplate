from typing import List
from pydantic import BaseModel

class Product(BaseModel):
    product_id: str
    name: str
    description: str
    price: int  # in cents
    features: List[str]

# Products from your Dodo Payments dashboard
products: List[Product] = [
    Product(
        product_id="pdt_otkoyXBAqasLqEhXNt0vX",
        name="Test classx",
        description="Test classxTest classxTest classx",
        price=10000,  # $100.00 in cents
        features=[
            "One-time purchase",
            "EdTech category",
            "Tax inclusive pricing",
            "Lifetime access",
        ],
    ),
    Product(
        product_id="pdt_OvNcp8MhCZRFNxM8k5UsU",
        name="C# sdks for dodo payments",
        description="C# sdks for dodo payments",
        price=0,  # Pay what you want
        features=[
            "Pay what you want pricing",
            "One-time purchase",
            "SaaS category",
            "Flexible pricing model",
        ],
    ),
    Product(
        product_id="pdt_igecL7YGL061DttyAialC",
        name="Classx",
        description="Classx",
        price=1000000,  # $10,000.00 in cents
        features=[
            "Monthly recurring at $10,000/month",
            "EdTech category",
            "Tax inclusive pricing",
            "1-day subscription period",
        ],
    ),
]
