import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SERP_API_KEY = os.getenv("SERP_API_KEY")
QUERY = os.getenv("QUERY", "Joana Trashlieva")

def run_scraper():
    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": QUERY,
        "api_key": SERP_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    timestamp = datetime.utcnow().isoformat()
    output = {
        "timestamp": timestamp,
        "query": QUERY,
        "results": data
    }

    with open("results.json", "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    run_scraper()
