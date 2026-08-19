from datetime import date


def is_resource_current(resource):
    """Return True if the resource has not passed its review date."""

    next_review_date = resource.get("next_review_date")

    if not next_review_date:
        return False

    review_date = date.fromisoformat(next_review_date) #converts to 2026,6,21 
    today = date.today() #get today's date 

    return review_date >= today 