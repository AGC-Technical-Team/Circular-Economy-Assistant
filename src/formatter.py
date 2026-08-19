def format_resource(resource, user_request):
    """Create a clear response for one matching resource."""

    organization = resource.get("organization_name", "Unknown organization")
    service = resource.get("service_name", "Unknown service") #print service name else put unknown

    accepted_items = resource.get("accepted_items", [])
    locations = resource.get("locations_covered", [])
    warnings = resource.get("warnings", [])

    item = user_request.get("item", "item")
    intent = user_request.get("intent", "requested action")
    source_url = resource.get("source_url") or "unknown"

    lines = [
        f"Organization: {organization}", #f string is a string that u can put variable in 
        f"Service: {service}",
        f"Why it matches: It accepts {item} and supports {intent}.",
        f"Accepted items: {', '.join(accepted_items)}",
        f"Locations covered: {', '.join(locations)}",
        f"Pickup or drop-off: {resource.get('pickup_or_dropoff', 'unknown')}",
        f"Fee status: {resource.get('fee_status', 'unknown')}",
        (
            "Contact first: "
            + ("Yes" if resource.get("contact_required") else "No")
        ),
        f"Last verified: {resource.get('last_verified_date', 'unknown')}",
        f"Official source: {source_url}",
    ]

    if warnings:
        lines.append("Warnings: " + " ".join(warnings))

    return "\n".join(lines) #combines list into 1 string (cup,chair,...)