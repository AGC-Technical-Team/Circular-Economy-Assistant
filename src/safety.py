def check_safety(user_request):
    """Check whether the item's condition creates a safety risk."""

    condition = user_request.get("condition")

    if condition == "unsafe_contaminated":
        return {
            "safe_to_continue": False,
            "message": (
                "This item may be unsafe. Do not open it or attempt "
                "a home repair. Contact a professional service."
            )
        }

    return {
        "safe_to_continue": True,
        "message": None
    }