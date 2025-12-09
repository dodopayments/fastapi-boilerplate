# Dodo Payments FastAPI Boilerplate

A minimal FastAPI boilerplate for integrating [Dodo Payments](https://dodopayments.com/) into your Python application.

## Features

- **Quick Setup** - Get started in under 5 minutes
- **Payment Integration** - Pre-configured checkout flow using `dodopayments` Python SDK
- **Modern UI** - Clean, dark-themed pricing page with Tailwind CSS
- **Webhook Handler** - Ready-to-use webhook endpoint for payment events
- **Customer Portal** - One-click subscription management
- **Type Safety** - Fully typed with Pydantic models
- **Pre-filled Checkout** - Demonstrates passing customer data to improve UX

## Prerequisites

Before you begin, make sure you have:

- **Python 3.8+** (required for FastAPI and the Dodo Payments SDK)
- **Dodo Payments account** (to access API and Webhook Keys from dashboard)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/dodopayments/fastapi-boilerplate.git
cd fastapi-boilerplate
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get API Credentials

Sign up at [Dodo Payments](https://dodopayments.com/) and get your credentials from the dashboard:

- **API Key:** [Dashboard → Developer → API Keys](https://app.dodopayments.com/developer/api-keys)
- **Webhook Key:** [Dashboard → Developer → Webhooks](https://app.dodopayments.com/developer/webhooks)

> Make sure you're in **Test Mode** while developing!

### 5. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Update the values with your Dodo Payments credentials:

```env
DODO_PAYMENTS_API_KEY=your_api_key_here
DODO_PAYMENTS_WEBHOOK_KEY=your_webhook_signing_key_here
DODO_PAYMENTS_RETURN_URL=http://localhost:8000
DODO_PAYMENTS_ENVIRONMENT=test_mode
```

### 6. Add Your Products

Update `app/lib/products.py` with your actual product IDs from Dodo Payments:

```python
products: List[Product] = [
    Product(
        product_id="pdt_001",  # Replace with your product ID
        name="Basic Plan",
        description="Get access to basic features and support",
        price=9999,  # in cents
        features=[
            "Access to basic features",
            "Email support",
            "1 Team member",
            "Basic analytics",
        ],
    ),
    # ... add more products
]
```

### 7. Run the Development Server

```bash
uvicorn app.main:app --reload --port 8000
```

Open [http://localhost:8000](http://localhost:8000) to see your pricing page!

## Project Structure

```
app/
├── api/
│   ├── checkout.py      # Checkout session handler
│   ├── portal.py        # Customer portal redirect
│   └── webhook.py       # Webhook event handler
├── core/
│   └── config.py        # Configuration settings
├── lib/
│   ├── customers.py     # Customer utilities (normalization, payload helpers)
│   └── products.py      # Product definitions
├── templates/
│   ├── base.html        # Base template
│   └── index.html       # Pricing page
├── static/
│   └── css/             # Custom styles (if needed)
└── main.py              # App entry point
```

## Customization

### Update Product Information

Edit `app/lib/products.py` to modify:
- Product IDs (from your Dodo dashboard)
- Pricing
- Features
- Descriptions

### Pre-fill Customer Data

In `app/templates/index.html`, replace the hardcoded values with your actual user data:

```javascript
const customerData = {
    name: "John Doe",  // Replace with actual logged-in user's name
    email: "john@example.com"  // Replace with actual logged-in user's email
};
```

In a production app, you would get this data from your authentication system (e.g., session, JWT token, etc.).

### Update Customer Portal Link

In `app/templates/index.html`, replace the hardcoded customer ID:

```javascript
const customerId = "cus_001";  // Replace with actual customer ID
```

## Webhook Events

The boilerplate demonstrates handling two webhook events in `app/api/webhook.py`:

- `subscription.active` - Triggered when a subscription becomes active
- `payment.succeeded` - Triggered when a payment is successful

Add your business logic inside these handlers:

```python
if event_type == "subscription.active":
    # Grant access to your product
    # Update user database
    # Send welcome email
    pass
```

Add more webhook events as needed.

For local development, you can use tools like [ngrok](https://ngrok.com/) to create a secure tunnel to your local server and use it as your webhook URL. Remember to update your `.env` file with the correct webhook verification key.

## Deployment

### Build for Production

For production, you can use Gunicorn with Uvicorn workers:

```bash
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Deployment targets

You can deploy this FastAPI application to any platform that supports Python/FastAPI:
Note: FastAPI on Vercel is possible via Python Serverless Functions but is outside the scope of this boilerplate. Prefer Railway/Render for FastAPI.

Don't forget to add your environment variables (API key, Webhook key, Return URL, Environment) in the deployment platform's dashboard.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fdodopayments%2Ffastapi-boilerplate.git)


### Update Webhook URL

After deploying, update your webhook URL in the [Dodo Payments Dashboard](https://app.dodopayments.com/developer/webhooks):

```
https://yourdomain.com/api/webhook
```

## Learn More

- [Dodo Payments Documentation](https://docs.dodopayments.com/)
- [Python SDK Documentation](https://docs.dodopayments.com/developer-resources/sdks/python)
- [Webhooks Documentation](https://docs.dodopayments.com/developer-resources/webhooks)

## Support

Need help? Reach out:
- [Dodo Payments Discord](https://discord.com/invite/bYqAp4ayYh)
- [GitHub Issues](https://github.com/dodopayments/fastapi-boilerplate/issues)
