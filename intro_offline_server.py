import os
from flask import Flask, send_from_directory

OFFLINE_BUILD_DIRECTORY = os.environ["OFFLINE_BUILD_DIRECTORY"]
assert OFFLINE_BUILD_DIRECTORY, "Set the OFFLINE_BUILD_DIRECTORY variable to " \
                                "point to the directory to serve the offline " \
                                "build from."
app = Flask(__name__, )

@app.route('/<path:path>')
@app.route('/')
def display(path=""):
    if path.endswith("/") or not path:
        path += "index.html"
    return send_from_directory(OFFLINE_BUILD_DIRECTORY, path)

app.run(debug=True, host='0.0.0.0', port=25444)
