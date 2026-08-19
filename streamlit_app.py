# Install Streamlit once with:
# python -m pip install streamlit

# Run this web app with:
# python -m streamlit run streamlit_app.py


# Streamlit creates the web page
import streamlit as st

# Sends the user's sentence to Gemini
# and returns a structured dictionary
from src.llm_extractor import extract_request

# Loads real services from data/resources.json
from src.data_loader import load_resources

# Checks whether the item's condition may be dangerous
from src.safety import check_safety

# Searches the real resource data for matches
from src.search import search_resources

# Sorts matching resources from best to worst
from src.ranking import rank_resources

# Turns each matching resource into readable text
from src.formatter import format_resource

# Records anonymous search details
from src.logger import log_search

# Load the real organizations and services
resources = load_resources()


# Display the main page title
st.title("Circular Economy Assistant for Lebanon")


# Display a short explanation
st.write(
    "Describe your item, its condition, what you want to do, "
    "and your location."
)


# Create a text box for the user's sentence
user_text = st.text_area(
    "Describe your item:",
    placeholder=(
        "Example: I have a usable chair in Zalka "
        "and I want to donate it."
    ),
)


# Create the button that starts the search
search_button = st.button("Find a service")


# Run only when the user clicks the button
if search_button:

    # Check whether the text box is empty
    if user_text.strip() == "":
        st.warning("Please describe your item first.")

    else:
        # Send the user's sentence to Gemini
        extracted_request = extract_request(user_text)

        # Stop if Gemini failed or returned invalid data
        if extracted_request is None:
            st.error(
                "I could not understand the request. "
                "Please describe it differently."
            )

        else:
            # Create an empty list for missing information
            missing_fields = []

            # Check whether Gemini found the item
            if extracted_request.get("item") is None:
                missing_fields.append("item")

            # Check whether Gemini found the category
            if extracted_request.get("category") is None:
                missing_fields.append("category")

            # Check whether Gemini found the condition
            if extracted_request.get("condition") is None:
                missing_fields.append("condition")

            # Check whether Gemini found the intent
            if extracted_request.get("intent") is None:
                missing_fields.append("intent")

            # Check whether Gemini found the location
            if extracted_request.get("location") is None:
                missing_fields.append("location")

            # Stop when required information is missing
            if missing_fields:
                st.warning(
                    "Please include this missing information: "
                    + ", ".join(missing_fields)
                )

            else:
                # Check the condition inside Gemini's dictionary
                safety_result = check_safety(extracted_request)

                # Stop when the item may be unsafe
                if not safety_result["safe_to_continue"]:
                    st.error(safety_result["message"])

                else:
                    # Compare Gemini's dictionary with resources.json
                    matching_resources = search_resources(
                        resources,
                        extracted_request,
                    )

                    # Sort matches from best to worst
                    ranked_resources = rank_resources(
                        matching_resources
                    )
                    # Record the search and how many results were found
                    log_search(
                        extracted_request,
                        len(ranked_resources),
                    )

                    # Show what Gemini understood
                    st.subheader("Information detected")

                    st.write(extracted_request)

                    # Show the number of matches
                    st.write(
                        "Number of matching resources:",
                        len(ranked_resources),
                    )

                    # Show a warning when nothing matches
                    if len(ranked_resources) == 0:
                        st.warning(
                            "No matching resource was found."
                        )

                    # Display every matching service
                    else:
                        st.subheader("Matching services")

                        for resource in ranked_resources:

                            # Create readable text for this service
                            formatted_response = format_resource(
                                resource,
                                extracted_request,
                            )

                            # Display the service information
                            st.text(formatted_response)

                            # Draw a line between services
                            st.divider()
