from fastapi import APIRouter
from models import Ticket, TicketResult
from logic import classify_ticket

router = APIRouter()

@router.get("/")
def home() -> dict[str, str]:
    """Return a simple API status message."""
    return {"message": "CS415 Ticket API is running"}

@router.post(
    "/tickets/classify",
    response_model=TicketResult,
)
def classify_ticket_endpoint(ticket: Ticket) -> TicketResult:
    """Classify an incoming customer support ticket."""
    return classify_ticket(ticket)
