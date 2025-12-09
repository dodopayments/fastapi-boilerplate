from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from dodopayments import DodoPayments
from app.core.config import settings
from app.lib.customers import CustomerData, to_dodo_customer_payload
router = APIRouter()

client = DodoPayments(
    bearer_token=settings.DODO_PAYMENTS_API_KEY,
    environment=settings.DODO_PAYMENTS_ENVIRONMENT
)

# Using shared CustomerData from app.lib.customers

class CheckoutRequest(BaseModel):
    product_id: str
    quantity: int = 1
    customer: Optional[CustomerData] = None

@router.post("/")
async def create_checkout(request: CheckoutRequest):
    """
    Create a checkout session for a product.
    Returns the payment link URL for the customer to complete payment.
    """
    try:
        # Build Dodo-compatible customer payload via shared helper
        customer_block = to_dodo_customer_payload(request.customer)

        # Create checkout session using the SDK
        checkout_session = client.checkout_sessions.create(
            product_cart=[
                {
                    "product_id": request.product_id,
                    "quantity": request.quantity,
                }
            ],
            customer=customer_block,
            show_saved_payment_methods=True,
            feature_flags={
                "allow_discount_code": True
            },
            return_url=settings.DODO_PAYMENTS_RETURN_URL,
        )

        return {
            "session_id": checkout_session.session_id,
            "checkout_url": checkout_session.checkout_url
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
