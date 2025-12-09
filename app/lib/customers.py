from typing import Optional, Dict, Any
from pydantic import BaseModel, EmailStr


class CustomerData(BaseModel):
    """Common customer data used across checkout and portal operations."""
    name: Optional[str] = None
    email: Optional[EmailStr] = None


def normalize_email(value: Optional[str]) -> Optional[str]:
    """Normalize email to lowercase and trim spaces."""
    if not value:
        return None
    return value.strip().lower()


def to_dodo_customer_payload(customer: Optional[CustomerData]) -> Optional[Dict[str, Any]]:
    """
    Convert CustomerData into a payload compatible with Dodo Payments SDK.
    Returns None if no usable customer info is supplied.
    """
    if not customer:
        return None

    payload: Dict[str, Any] = {}
    email = normalize_email(str(customer.email)) if customer.email else None

    if email:
        payload["email"] = email
    if customer.name:
        payload["name"] = customer.name

    return payload or None


def sanitize_customer_id(customer_id: str) -> str:
    """
    Basic customer_id sanitizer for portal creation.
    Raises ValueError if empty after trimming.
    """
    if not isinstance(customer_id, str):
        raise ValueError("customer_id must be a string")
    trimmed = customer_id.strip()
    if not trimmed:
        raise ValueError("customer_id is required")
    return trimmed