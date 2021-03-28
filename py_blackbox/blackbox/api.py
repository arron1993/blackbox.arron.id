import requests
import os
import jwt
import datetime

from config import API_ENDPOINT


class BlackboxApi():
    def __init__(self):
        self.session = requests.Session()
        self.token = None
        self.refresh_token = None

    def _normalize_path(self, path):
        if not path.endswith("/"):
            path += "/"
        return f'{API_ENDPOINT}{path}'

    def _set_auth_header(self, tokens):
        self.refresh_token = tokens["refresh"]
        self.token = tokens["access"]
        self.session.headers.update(
            {'Authorization': f'Bearer {tokens["access"]}'})

    def signin(self, username, password):
        resp = self.post(
            "api/signin/",
            {"username": username, "password": password})

        if resp.ok:
            result = resp.json()
            self._set_auth_header(result)
        return resp

    def refresh(self):
        if self.token:
            token_expiry = jwt.decode(
                self.token, options={"verify_signature": False})["exp"]
            token_expiry = datetime.datetime.fromtimestamp(token_expiry)
            time_til_expires = token_expiry - datetime.datetime.now()

            if time_til_expires < datetime.timedelta(days=1):
                resp = self.post('signin/refresh/',
                                 {"refresh": self.refresh_token})
                if resp.ok:
                    self._set_auth_header(resp.json())

    def get(self, path):
        self.refresh()
        path = self._normalize_path(path)
        return self.session.get(path)

    def post(self, path, data):
        self.refresh()
        path = self._normalize_path(path)

        return self.session.post(
            path,
            json=data)

    def create_session(self, data):
        return self.post("api/session/", data)

    def create_stint(self, session_id):
        return self.post(f"api/session/{session_id}/stints/", {})

    def create_lap(self, session_id, stint_id, data):
        return self.post(f"api/session/{session_id}/stints/{stint_id}/laps/", data)
