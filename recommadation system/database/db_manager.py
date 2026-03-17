# Database connection and helper functions
import json
import os

def load_json_data(filepath):
    """Loads course data from a JSON file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

# Optional MySQL integration placeholders
def get_mysql_connection():
    """Connect to MySQL database using credentials from environment variables."""
    # import mysql.connector
    pass
