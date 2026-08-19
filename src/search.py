from src.freshness import is_resource_current

DISPLAYABLE_STATUSES = [
    "verified",
    "verified_with_warning"
]

def location_matches(requested_location, covered_locations):
    """Check whether a resource covers the user's location."""

    cleaned_requested_location = requested_location.strip().lower()

    cleaned_covered_locations = []

    for location in covered_locations:
        cleaned_location = location.strip().lower()
        cleaned_covered_locations.append(cleaned_location)

    if cleaned_requested_location == "":
        return False

    if "lebanon" in cleaned_covered_locations:
        return True

    if cleaned_requested_location in cleaned_covered_locations:
        return True

    return False



def search_resources(resources, user_request):
    """Find verified resources matching category, intent and condition."""

    matches = [] #creating new list to store matches 

    for resource in resources:
        # Check whether this resource is allowed to appear.
        status = resource.get("verification_status") #use get because it returns none and better search in dictionary

        if status not in DISPLAYABLE_STATUSES:
            continue
        if not is_resource_current(resource): #any expired resource will not be shown
            continue

        # Check whether the categories match.
        resource_category = resource.get("category") #get the category from the resource, if not found, return None
        requested_category = user_request.get("category")

        if resource_category != requested_category:
            continue

        # Check whether the resource supports the user's intention.
        supported_intents = resource.get("supported_intents", []) # get the supported_intents from the resource, if not found, return an empty list
        requested_intent = user_request.get("intent")

        #return None if single values and return list for more than 1 value

        if requested_intent not in supported_intents:
            continue

        # Check whether the resource accepts the item's condition.
        accepted_conditions = resource.get("condition_accepted", [])
        requested_condition = user_request.get("condition")

        if (
            requested_condition != "unknown"
            and requested_condition not in accepted_conditions
        ):
            continue

        # The resource passed every check.
        matches.append(resource)

    return matches

DISPLAYABLE_STATUSES = [
    "verified",
    "verified_with_warning"
]


def location_matches(requested_location, covered_locations):
    """Check whether a resource covers the user's location."""

    cleaned_requested_location = requested_location.strip().lower()

    cleaned_covered_locations = []

    for location in covered_locations:
        cleaned_location = location.strip().lower()
        cleaned_covered_locations.append(cleaned_location)

    # The user did not provide a location.
    if cleaned_requested_location == "":
        return False

    # A resource covering Lebanon matches any Lebanese location.
    if "lebanon" in cleaned_covered_locations:
        return True

    # Check for an exact location match.
    if cleaned_requested_location in cleaned_covered_locations:
        return True

    return False


def search_resources(resources, user_request):
    """Find verified resources matching category, intent, condition and location."""

    # Store every resource that passes all checks.
    matches = []

    # Check each resource dictionary one by one.
    for resource in resources:

        # Check whether the resource is allowed to appear.
        # If the key is missing, .get() returns None.
        status = resource.get("verification_status")

        if status not in DISPLAYABLE_STATUSES:
            continue

        # Check whether the categories match.
        resource_category = resource.get("category")
        requested_category = user_request.get("category")

        if resource_category != requested_category:
            continue

        # Get the intentions supported by the resource.
        # If the field is missing, use an empty list.
        supported_intents = resource.get("supported_intents", [])
        requested_intent = user_request.get("intent")

        requested_item = user_request.get("item")

        accepted_items = resource.get("accepted_items", [])
        excluded_items = resource.get("excluded_items", [])

        if requested_item is None:
            continue

        if requested_item in excluded_items:
            continue

        if requested_item not in accepted_items:
            continue

        if requested_intent not in supported_intents:
            continue

        # Check whether the resource accepts the item's condition.
        accepted_conditions = resource.get("condition_accepted", [])
        requested_condition = user_request.get("condition")

        if (
            requested_condition != "unknown"
            and requested_condition not in accepted_conditions
        ):
            continue

        # Check whether the resource covers the user's location.
        covered_locations = resource.get("locations_covered", [])
        requested_location = user_request.get("location", "")

        if not location_matches(
            requested_location,
            covered_locations
        ):
            continue

        # The resource passed every check.
        matches.append(resource)

    return matches

