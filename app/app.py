from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Digital Heritage Twin API is running"

@app.route("/heritage")
def heritage():
    with open("../gis/sample_data.geojson") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
