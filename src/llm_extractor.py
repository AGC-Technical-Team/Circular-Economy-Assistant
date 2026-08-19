# Reads the Gemini API key from the .env file
from dotenv import load_dotenv

# Tools for communicating with Gemini
from google import genai
from google.genai import types, errors

# Lets us describe the required structure of Gemini's answer
from pydantic import BaseModel

# Checks that Gemini returned only approved values
from src.request_validator import validate_request_data


# Load GEMINI_API_KEY from the .env file
load_dotenv()


# Describe the required answer structure
class ExtractedRequest(BaseModel):
    item: str | None
    category: str | None
    condition: str | None
    intent: str | None
    location: str | None


# Instructions Gemini will read
EXTRACTION_INSTRUCTIONS = """
Read the user's sentence and extract information about their item.

Allowed categories:
electronics, appliances, clothing, furniture_household

Allowed conditions:
usable, worn, damaged_repairable, non_working,
end_of_life, unsafe_contaminated, unknown

Allowed intents:
repair, donate, reuse, resell, recycle

Use None when information is missing.
Do not guess or invent information.
"""


def extract_request(user_text):
    """Send the user's sentence to Gemini and return checked data."""

    try:
        # Create the Gemini connection
        client = genai.Client()

        # Send the user's sentence to Gemini
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=user_text,
            config=types.GenerateContentConfig(
                system_instruction=EXTRACTION_INSTRUCTIONS,
                response_mime_type="application/json",
                response_schema=ExtractedRequest,
            ),
        )

        # Get Gemini's structured answer
        parsed_request = response.parsed

        if parsed_request is None:
            print("Problem: Gemini returned no structured data.")
            print("Raw response:", response.text)
            return None

        # Convert Gemini's answer into a normal dictionary
        request_data = parsed_request.model_dump()

        # Reject values that are not allowed
        if not validate_request_data(request_data):
            return None

        # Return the valid request
        return request_data

    # Stop safely if Gemini has an API problem
    except errors.APIError:
        return None

    # Stop safely if Gemini's answer cannot be converted
    except ValueError:
        return None