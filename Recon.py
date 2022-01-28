import json
import requests

class Recon:
    def __init__(self, bearer, band, url):
        self.bearer = bearer
        self.band = band

        self.url = url

        self.headers = {
            "Authorization": f"Bearer {self.bearer}"
        }

        self.securityMasks = {
            "16794626": "WPA2 PSK (CCMP)",
            "8932963": "WPA Mixed PSK (CCMP TKIP)"
        }
    
    def startScan(self):
        payload = {
            "live": False,
            "scan_time": 0,
            "band": str(self.band)
        }
        
        req = requests.post(f"{self.url}/api/recon/start", headers=self.headers, json=payload)

        response = json.loads(req.text)

        if "error" in response:
            return False, response["error"]
        
        return True, response["scanID"]
    
    def stopScan(self):
        req = requests.post(f"{self.url}/api/recon/stop", headers=self.headers)

        response = json.loads(req.text)

        if "success" in response and response["success"] == True:
            return True
        return False

    def getResults(self, scanID):
        
        req = requests.get(f"{self.url}/api/recon/scans/{scanID}", headers=self.headers)

        response = json.loads(req.text)

        if "APResults" in response:
            return True, response["APResults"]
        return False