from fastapi import APIRouter, Request, HTTPException
from dodopayments import DodoPayments
from app.core.config import settings
import json

router = APIRouter()

client = DodoPayments(
    bearer_token=settings.DODO_PAYMENTS_API_KEY,
    environment=settings.DODO_PAYMENTS_ENVIRONMENT,
    webhook_key=settings.DODO_PAYMENTS_WEBHOOK_KEY,
)

@router.post("/")
async def handle_webhook(request: Request):
    """
    Handle incoming webhooks from Dodo Payments.
    Verifies the webhook signature using the Dodo Payments SDK's unwrap feature.
    Extracts event_type from the raw JSON payload.
    """
    try:
        body = await request.body()

        unwrapped = client.webhooks.unwrap(
            body,
            headers={
                "webhook-id": request.headers.get("webhook-id", ""),
                "webhook-signature": request.headers.get("webhook-signature", ""),
                "webhook-timestamp": request.headers.get("webhook-timestamp", ""),
            },
        )

        if not unwrapped:
            raise HTTPException(status_code=400, detail="Webhook verification failed: missing dodo-signature header")


        try:
            raw_text = body.decode("utf-8") if isinstance(body, (bytes, bytearray)) else body
            payload = json.loads(raw_text)
        except json.JSONDecodeError as e:
            raise HTTPException(status_code=400, detail="Invalid JSON payload")

        event_type = payload.get("type", "")
        event_data = payload.get("data", {})  # optional if you need to use it later

        print(f"✅ Verified webhook: {event_type}")

        # Handle different event types
        if event_type == "subscription.active":
            print("🎉 Subscription is active!")
            # TODO: Grant access, update DB, send email

        elif event_type == "payment.succeeded":
            print("💰 Payment succeeded!")
            # TODO: Fulfill order, update DB, send email

        elif event_type == "subscription.cancelled":
            print("❌ Subscription cancelled")
            # TODO: Revoke access, update user status

        elif event_type == "payment.failed":
            print("⚠️ Payment failed")
            # TODO: Notify user, update payment status

        else:
            print(f"ℹ️ Unhandled event type: {event_type}")

        return {"status": "success", "event": event_type}

    except HTTPException:
        # re-raise explicit HTTP errors
        raise
    except Exception as e:
        print(f"❌ Webhook verification failed: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Webhook verification failed: {str(e)}")
