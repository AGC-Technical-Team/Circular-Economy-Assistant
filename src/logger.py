import json
from datetime import datetime
from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parent.parent # __file___ is the path of the current file, resolve() gets the absolute path, parent.parent gets the parent folder of src
LOG_FILE = PROJECT_FOLDER / "search_logs.jsonl" #save the searcg logs in search logs file in parent folder of src


def log_search(user_request, result_count):
    """Save anonymous structured information about one search."""

    log_entry = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),  #date time gets current date and time, isoformat converts it to string, timespec="seconds" removes milliseconds
        "item": user_request.get("item"),
        "category": user_request.get("category"),
        "condition": user_request.get("condition"),
        "intent": user_request.get("intent"),
        "result_count": result_count,
    }

    with LOG_FILE.open("a", encoding="utf-8") as file: #append mode, encoding="utf-8" ensures that the file is read and written in UTF-8 encoding
        file.write(json.dumps(log_entry) + "\n") #writes the log entry as a JSON string followed by a newline character to the log file