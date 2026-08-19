def find_category(user_input, synonyms):
    """Find the category of an item using synonym matching."""

    cleaned_input = user_input.strip().lower() #remove spaces from the beginning and end of the input string and convert it to lowercase

    for category, words in synonyms.items(): #category is the key and words is the value in the synonyms dictionary
        for word in words:
            if word in cleaned_input:
                return category

    return None

INTENT_KEYWORDS = {
    "repair": [
        "repair",
        "fix"
    ],
    "donate": [
        "donate",
        "give away",
        "give it away"
    ],
    "reuse": [
        "reuse",
        "use again"
    ],
    "resell": [
        "resell",
        "sell",
        "second hand"
    ],
    "recycle": [
        "recycle",
        "recycling"
    ]
}


def find_intent(user_input):
    """Find what the user wants to do with the item."""

    cleaned_input = user_input.strip().lower()

    for intent, words in INTENT_KEYWORDS.items():
        for word in words:
            if word in cleaned_input:
                return intent

    return None

CONDITION_KEYWORDS = {
    "unsafe_contaminated": [
        "leaking battery",
        "swollen battery",
        "battery is swollen",
        "burning smell",
        "sparking",
        "on fire",
        "contaminated",
        "unsafe"
    ],
    "non_working": [ #non working before usuable because user might say "not working" and we want to catch that first
        "not working",
        "does not work",
        "doesn't work",
        "does not turn on",
        "doesn't turn on",
        "stopped working",
        "dead"
    ],
    "end_of_life": [
        "end of life",
        "cannot be used again",
        "beyond repair",
        "completely destroyed"
    ],
    "damaged_repairable": [
        "damaged",
        "cracked",
        "broken",
        "torn",
        "needs repair"
    ],
    "worn": [
        "worn",
        "faded",
        "old but usable",
        "used condition"
    ],
    "usable": [
        "new",
        "working",
        "usable",
        "good condition",
        "like new",
        "still works"
    ]
}


def find_condition(user_input):
    """Find the condition of the user's item."""

    cleaned_input = user_input.strip().lower()

    for condition, words in CONDITION_KEYWORDS.items():
        for word in words:
            if word in cleaned_input:
                return condition

    return "unknown"

ITEM_KEYWORDS = {
    "phone": [
        "phone",
        "mobile",
        "cellphone",
        "smartphone"
    ],
    "laptop": [
        "laptop",
        "notebook computer"
    ],
    "tablet": [
        "tablet",
        "ipad"
    ],
    "printer": [
        "printer"
    ],
    "router": [
        "router",
        "wifi router"
    ],
    "television": [
        "television",
        "tv"
    ],
    "refrigerator": [
        "refrigerator",
        "fridge"
    ],
    "washing_machine": [
        "washing machine",
        "washer"
    ],
    "oven": [
        "oven"
    ],
    "air_conditioner": [
        "air conditioner",
        "ac unit"
    ],
    "clothing": [
        "clothes",
        "clothing",
        "shirt",
        "pants",
        "trousers",
        "jacket",
        "dress"
    ],
    "chair": [
        "chair"
    ],
    "table": [
        "table"
    ],
    "cupboard": [
        "cupboard",
        "cabinet"
    ],
    "sofa": [
        "sofa",
        "couch"
    ],
    "mattress": [
        "mattress"
    ]
}

def find_item(user_input):
    """Find the user's exact item using keyword matching."""

    cleaned_input = user_input.strip().lower()

    for item, words in ITEM_KEYWORDS.items():
        for word in words:
            if word in cleaned_input:
                return item

    return None