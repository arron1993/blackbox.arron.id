import requests
import os

from config import API_ENDPOINT

class BlackboxApi():
    def __init__(self):
        self.session = requests.Session()

    def _normalize_path(self, path):
        if not path.endswith("/"):
            path += "/"
        return path

    def get(self, path):
        path = self._normalize_path(path)
        return self.session.get(os.path.join(API_ENDPOINT, path))

    def post(self, path, data):
        path = self._normalize_path(path)

        return self.session.post(
            os.path.join(API_ENDPOINT, path),
            json=data)

    def create_session(self, data):
        return self.post("api/session/", data).json()

    def signin(self, username, password):
        resp = self.session.post(
            os.path.join(API_ENDPOINT, "api", "signin/"),
            json={"username": username, "password": password})

        if resp.ok:
            result = resp.json()
            self.refreshToken = result["refresh"]
            self.session.headers.update({'Authorization': f'Bearer {result["access"]}'})
        return resp
