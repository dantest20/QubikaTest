import requests


class BaseClient:
    def __init__(self):
        self.session = requests.Session()

    def post(self, url, data):
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def get(self, url):
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
