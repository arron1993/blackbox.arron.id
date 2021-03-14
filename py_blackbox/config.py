import os

API_ENDPOINT = "http://192.168.0.139:8000/"

if os.environ.get("ENVIRONMENT") == "production":
    API_ENDPOINT = "http://fuel.arron.id/"