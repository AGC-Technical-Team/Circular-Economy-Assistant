from src.data_loader import load_resources, load_synonyms
from src.router import (
    find_category,
    find_intent,
    find_condition,
    find_item,
)
from src.search import search_resources
from src.safety import check_safety
from src.ranking import rank_resources
from src.formatter import format_resource
from src.logger import log_search
from src.llm_extractor import extract_request


def main():
    # Load the resource dataset and synonym dictionary.
    resources = load_resources()
    synonyms = load_synonyms()

    print("Circular Economy Assistant for Lebanon")
    print("----------------------------------------")
    print("Number of resource records:", len(resources))
    # Let the user describe everything naturally
    user_text = input(
        "Describe your item, its condition, what you want to do, "
        "and your location: "
    )

    # Ask Gemini to extract structured information
    extracted_request = extract_request(user_text)

    # Use an empty dictionary if Gemini fails
    if extracted_request is None:
        extracted_request = {}

    # Save the original sentence for the user_request dictionary later
    item_input = user_text

    # Take the item and category extracted by Gemini
    item = extracted_request.get("item")
    category = extracted_request.get("category")

    while item is None or category is None:  # if gemini fails to extract item or category, ask the user for them
        item_input = input("What item do you have? ")

        item = find_item(item_input)
        category = find_category(item_input, synonyms)

    if item is None:
        print("I could not identify the exact item.")

    if category is None:
        print("I could not identify the item category.")

    if item is None or category is None:
        print("Please describe the item differently.")

    print("Detected item:", item)
    print("Detected category:", category)

    # Use Gemini's condition when it recognized one.
    # Otherwise, use "unknown" so the manual question runs.
    condition = extracted_request.get("condition") or "unknown"

    while condition == "unknown":
        condition_input = input("What condition is it in? ")

        condition = find_condition(condition_input)

        if condition == "unknown":
            print("I could not identify the item's condition.")
            print(
                "Try words like: usable, worn, broken, "
                "not working, or swollen battery."
            )

    print("Detected condition:", condition)

    # Check safety immediately after detecting the condition.
    safety_request = {
        "condition": condition
    }

    safety_result = check_safety(safety_request)

    if not safety_result["safe_to_continue"]:
        print()
        print("Safety warning:")
        print(safety_result["message"])
        return

    # These questions are asked only if the item is safe.
    # Use Gemini's intent when it recognized one.
    # Otherwise, None makes the manual question run.
    intent = extracted_request.get("intent")

    while intent is None:
        intent_input = input(
            "Would you like to repair, donate, reuse, resell or recycle it? "
        )

        intent = find_intent(intent_input)

    if intent is None:
        print("I could not identify what you want to do.")
        print(
            "Please choose: repair, donate, reuse, resell, or recycle."
        )

    print("Detected intention:", intent)
    # Use Gemini's location when it found one.
    # Convert it to lowercase so it matches the dataset.
    location = (
        extracted_request.get("location") or ""
    ).strip().lower()

    while location == "":
        location_input = input(
            "What is your approximate neighborhood, municipality or district? "
        )

        location = location_input.strip().lower()

        if location == "":
            print("Please provide an approximate location.")

    # Combine the user's information into one dictionary.
    user_request = {
        "item_description": item_input.strip().lower(),
        "item": item,
        "category": category,
        "condition": condition,
        "intent": intent,
        "location": location,
    }
    missing_fields = []

    if user_request.get("item") is None:
        missing_fields.append("item")

    if user_request.get("category") is None:
        missing_fields.append("category")

    if user_request.get("intent") is None:
        missing_fields.append("intent")

    if user_request.get("condition") == "unknown":
        missing_fields.append("condition")

    if user_request.get("location") == "":
        missing_fields.append("location")

    if len(missing_fields) > 0:
        print()
        print("I need more information before searching.")
        print("Missing information:", ", ".join(missing_fields))
        return

    # Search for resources that match the request.
    matching_resources = search_resources(resources, user_request)
    ranked_resources = rank_resources(matching_resources)
    log_search(
        user_request,
        len(ranked_resources)
    )

    print()
    print("Number of matching resources:", len(ranked_resources))

    if len(ranked_resources) == 0:
        print("No matching resource was found.")
    else:
        for resource in ranked_resources:
            formatted_response = format_resource(
                resource,
                user_request
            )

            print()
            print(formatted_response)
            print("----------------------------------------")


if __name__ == "__main__":
    main()

