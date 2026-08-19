import json
from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parent.parent #goees to main project folder, which is the parent of the src folder(circular_economy_assistant)

RESOURCES_FILE = PROJECT_FOLDER / "data" / "resources.json" #goes to data in the main folder and opens resources.json

SYNONYMS_FILE = PROJECT_FOLDER / "data" / "synonyms.json" #goes to data in the main folder and opens synonyms.json


def load_resources():
    """Load resource records from resources.json."""

    with RESOURCES_FILE.open("r", encoding="utf-8") as file: #with opens the resources.json file in read mode and encoding utf-8(arabic,eng,symb), and assigns it to the variable "file"
        resources = json.load(file) #loads the json data from the file into a Python object (list of dictionaries) and assigns it to the variable "resources"

    return resources


def load_synonyms():
    """Load category synonyms from synonyms.json."""

    with SYNONYMS_FILE.open("r", encoding="utf-8") as file:
        synonyms = json.load(file)

    return synonyms

