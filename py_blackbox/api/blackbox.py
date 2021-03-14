import requests
import os

from config import API_ENDPOINT


class BlackboxApi():
    def __init__(self):
        self.session = requests.Session()

    def _normalize_path(self, path):
        if not path.endswith("/"):
            path += "/"
        return f'{API_ENDPOINT}{path}'

    def get(self, path):
        path = self._normalize_path(path)
        return self.session.get(path)

    def post(self, path, data):
        path = self._normalize_path(path)

        return self.session.post(
            path,
            json=data)

    def create_session(self, data):
        print(data)
        return self.post("api/session/", data)

    def create_lap(self, session_id, data):
        print(data)
        return self.post(f"api/session/{session_id}/laps/", data)
        
    def signin(self, username, password):
        resp = self.post(
            "api/signin/",
            {"username": username, "password": password})

        if resp.ok:
            result = resp.json()
            self.refreshToken = result["refresh"]
            self.session.headers.update(
                {'Authorization': f'Bearer {result["access"]}'})
        return resp
