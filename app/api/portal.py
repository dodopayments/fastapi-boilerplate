from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dodopayments import DodoPayments
from app.core.config import settings
from app.lib.customers import sanitize_customer_id
router = APIRouter()

client = DodoPayments(
    bearer_token=settings.DODO_PAYMENTS_API_KEY,
    environment=settings.DODO_PAYMENTS_ENVIRONMENT
)

class PortalRequest(BaseModel):
    customer_id: str

@router.post("/")
async def create_customer_portal(request: PortalRequest):
    """
    Create a customer portal session for the given customer ID.
    Returns a URL that the customer can use to access their portal.
    """
    try:
        # Sanitize and validate the incoming customer_id
        customer_id = sanitize_customer_id(request.customer_id)

        # Create customer portal session using the Dodo Payments SDK
        portal_session = client.customers.customer_portal.create(
            customer_id=customer_id
        )
        return {"url": portal_session.link}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
