from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route("/RunAdbCommand")
def RunAdbCommand():
    command = request.json["adbCommand"]
    cmd_arr = command.split()
    output = subprocess.check_output(cmd_arr).decode("utf-8")
    return jsonify({'commandOutput': output})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3234)