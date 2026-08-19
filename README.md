# Circular Economy Assistant for Lebanon

A Python application that helps users find suitable circular-economy services in Lebanon.

## How it works

1. The user describes an item in normal language.
2. Gemini extracts:
   - item
   - category
   - condition
   - intent
   - location
3. Python validates the extracted information.
4. Python checks for safety risks.
5. The app searches verified records in `data/resources.json`.
6. Matching resources are ranked and displayed.

Gemini only understands the user's sentence. The local dataset is the source of truth for organizations and services.

## Install the packages

```powershell
python -m pip install -r requirements.txt
```

## Gemini API key

Create a `.env` file in the main project folder:

```text
GEMINI_API_KEY=your_api_key_here
```

Do not upload or share the `.env` file.

## Run the web application

```powershell
python -m streamlit run streamlit_app.py
```

## Run the command-line application

```powershell
python app.py
```

## Run the automated tests

```powershell
python -m unittest discover -s tests -p "test*.py" -v
```

## Main project files

- `app.py`: command-line application
- `streamlit_app.py`: browser interface
- `data/resources.json`: verified service records
- `src/llm_extractor.py`: Gemini request extraction
- `src/safety.py`: safety checks
- `src/search.py`: deterministic resource filtering
- `src/ranking.py`: result ranking
- `src/formatter.py`: result formatting
- `tests/`: automated tests