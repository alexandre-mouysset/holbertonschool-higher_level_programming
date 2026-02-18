#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return {"error": "User not found"}, 404


@app.post("/add_user")
def add_user():
    dictionnary = request.get_json()

    if not request.is_json or type(dictionnary) is not dict:
        return {"error": "Invalid JSON"}, 400

    if "username" not in dictionnary:
        return {"error": "Username is required"}, 400

    if dictionnary["username"] in users:
        return {"error": "Username already exists"}, 409

    users[dictionnary["username"]] = dictionnary
    return {
        "message": "User added",
        "user": dictionnary,
    }, 201


if __name__ == "__main__":
    app.run
