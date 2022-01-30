from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/gps/<pos>")
def saveGPS(pos):

    lat = pos.split(",")[0]
    long = pos.split(",")[1]

    with open("location.json", "w") as f:
        json.dump({"latitude": lat, "longitude": long}, f)
    return "OK"

@app.route('/')
def hello_world():
    return render_template('index.html')


app.run(host="0.0.0.0", debug=True, port=8000, ssl_context=('cert.pem', 'key.pem'))