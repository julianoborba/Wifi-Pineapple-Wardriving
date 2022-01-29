from ast import Try
import re
import requests
import json

class auth:
    def __init__(self, user, password, url):
        self.user = user
        self.password = password
        self.url = url

    def generateBearer(self):
        payload = {
            "username": self.user,
            "password": self.password
        }

        try:
            req = requests.post(f"{self.url}/api/login", json=payload, timeout=10)
        except Exception as e:
            return False, "Connection Error"

        response = json.loads(req.text)

        if "error" in response:
            return False, response["error"]
        
        return True, response["token"]