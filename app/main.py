from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api import checkout, webhook, portal
from app.lib.products import products
import os

app = FastAPI(title="Dodo Payments FastAPI Boilerplate")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Include routers
app.include_router(checkout.router, prefix="/api/checkout", tags=["checkout"])
app.include_router(webhook.router, prefix="/api/webhook", tags=["webhook"])
app.include_router(portal.router, prefix="/api/customer-portal", tags=["portal"])

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "products": products})
