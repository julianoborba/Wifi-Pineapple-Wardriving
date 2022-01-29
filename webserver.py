from flask import Flask
import json

app = Flask(__name__)

import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/map")
def mapReq():
    return "ok"

@app.route("/gps/<pos>")
def saveGPS(pos):

    lat = pos.split(",")[0]
    long = pos.split(",")[1]

    with open("location.json", "w") as f:
        json.dump({"latitude": lat, "longitude": long}, f)
    return "OK"

@app.route('/')
def hello_world():
    return """
    <!DOCTYPE html>
<html>
<body>

<p id="demo"></p>

<script>

var x = document.getElementById("demo");

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
  sendData(position);
}

function error() {
    x.innerHTML = "error";
}

function sendData(position) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', `/gps/${position.coords.latitude},${position.coords.longitude}`, true);

    xhr.onload = function () {
    };

    xhr.send(null);
}

navigator.geolocation.watchPosition(showPosition, error, {enableHighAccuracy:true});
</script>

</body>
</html>


    """

app.run(host="0.0.0.0", debug=False, port=8000, ssl_context=('cert.pem', 'key.pem'))