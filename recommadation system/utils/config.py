import os

def get_config():
    """Returns application configuration."""
    return {
        "APP_NAME": "AI Course Recommender",
        "DEBUG": os.getenv("DEBUG", "False").lower() == "true",
    }
