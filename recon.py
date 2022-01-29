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
            "8932963": "WPA Mixed PSK (CCMP TKIP)",
            "0": "No Security"
        }

        self.scanData = []
    
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

        return response
    
    def newAPS(self, scanID):
        results = self.getResults(scanID)

        aps = []
        newAps = []

        if "APResults" in results and results["APResults"] != None:
            for i in range(len(results["APResults"])):
                ssid = results["APResults"][i]["ssid"]
                bssid = results["APResults"][i]["bssid"]

                if str(results["APResults"][i]["encryption"]) in self.securityMasks:
                    encryption = self.securityMasks[str(results["APResults"][i]["encryption"])]
                else:
                    encryption = "Unknown"
                
                isHidden = bool(results["APResults"][i]["hidden"])
                isWPS = bool(results["APResults"][i]["wps"])
                channel = results["APResults"][i]["channel"]
                signal = results["APResults"][i]["signal"]

                newData = [ssid, bssid, channel, signal, encryption, isHidden, isWPS]

                aps.append(newData)

        for i in range(len(aps)):
            toAdd = True

            for j in range(len(self.scanData)):
                if self.scanData[j][1] == aps[i][1]:
                    toAdd = False
                    break
            
            if toAdd:
                newAps.append(aps[i])
                self.scanData.append(aps[i])
        
        if newAps:
            return True, newAps
        return False, None