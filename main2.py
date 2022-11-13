from flask import Flask, jsonify, request
from data2 import data

app = Flask(__name__)

@app.route("/")
def showData():
    return jsonify({
        "data" : data,
        "message" : "success"
    }), 200
    
#http://127.0.0.1:5000/star?name=value
@app.route("/star")
def Star():
    name = request.args.get("name")
    starData = next(i for i in data if i["name"] == name)
    return jsonify({
        "data": starData,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()