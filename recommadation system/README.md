# AI-Based Course Recommendation System

## Abstract
Many students face confusion after completing their 12th grade when choosing a suitable course for higher education. Due to limited guidance and awareness about different career paths, students often struggle to select the right domain based on their interests and abilities.

This project proposes an AI‑Based Course Recommendation System that helps students identify suitable courses based on their interests, skills, and academic preferences. The system interacts with users through a simple interface, collects their responses, and recommends appropriate fields such as Engineering, Medical, Commerce, Arts, or Design.

The system aims to support students in making better career decisions and reduce confusion during course selection.

## Technologies Used
- **Programming:** Python
- **Framework:** Langchain (with potential Flowise integration)
- **AI Model:** LLM API (e.g., OpenAI, Google Gemini, Anthropic)
- **Database:** JSON (for fast prototyping) & MySQL (for production data)
- **Interface:** Web UI (Streamlit recommended for fast AI UIs, or Flask/FastAPI)
- **Platform:** Windows

## Project Structure
- `core/`: Contains the Langchain logic, prompt templates, and LLM communication.
- `ui/`: Contains the web interface application code.
- `database/`: Database connection routines and models (MySQL/JSON handling).
- `data/`: Directory to store local JSON datasets or exported files.
- `utils/`: Configuration management and helper scripts.

## Setup Instructions
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill in your actual API keys.
5. Run the application: `python main.py` or (if using Streamlit) `streamlit run ui/app.py`
