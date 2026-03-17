import os
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    print("==================================================")
    print("Welcome to the AI-Based Course Recommendation System")
    print("==================================================")
    print("Initialization complete.")
    print("")
    print("To start the Web UI, please run the following command in your terminal:")
    print("  streamlit run ui/app.py")
    print("==================================================")

if __name__ == "__main__":
    main()
