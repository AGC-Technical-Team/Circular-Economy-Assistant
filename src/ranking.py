def calculate_score(resource):
    """Give a resource a score based on reliability."""

    score = 0

    if resource.get("verification_status") == "verified":
        score += 20

    if resource.get("verification_status") == "verified_with_warning":
        score += 10

    confidence = resource.get("confidence_level")

    if confidence == "high":
        score += 10
    elif confidence == "medium":
        score += 5

    return score


def rank_resources(resources):
    """Return resources ordered from highest score to lowest."""

    ranked_resources = sorted( #sorts them according to score, highest to lowest
        resources,
        key=calculate_score,
        reverse=True,
    )

    return ranked_resources