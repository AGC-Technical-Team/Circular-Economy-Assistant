from src.request_schema import (
    ALLOWED_CATEGORIES,
    ALLOWED_INTENTS,
    ALLOWED_CONDITIONS,
)


def validate_request_data(request_data):
    """Reject invalid values, but allow missing values."""

    category = request_data.get("category")
    intent = request_data.get("intent")
    condition = request_data.get("condition")

    # Only check category when Gemini found one
    if category is not None and category not in ALLOWED_CATEGORIES:
        return False

    # Only check intent when Gemini found one
    if intent is not None and intent not in ALLOWED_INTENTS:
        return False

    # Only check condition when Gemini found one
    if condition is not None and condition not in ALLOWED_CONDITIONS:
        return False

    return True