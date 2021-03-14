import os

API_ENDPOINT = "http://localhost:8000/"

if os.environ.get("ENVIRONMENT") == "production":
    API_ENDPOINT = "http://fuel.arron.id/"