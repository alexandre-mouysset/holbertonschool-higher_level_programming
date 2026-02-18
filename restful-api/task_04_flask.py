#!/usr/bin/python3
"""
Simple Flask API with an in-memory user store.

This module provides a tiny set of endpoints useful for learning or
manual testing. Data is kept in the module-level `users` dictionary
and is not persistent.

Endpoints
- GET  /               -> Welcome message
- GET  /data           -> JSON list of usernames
- GET  /status         -> "OK" (health check)
- GET  /users/<username> -> Return stored user JSON or 404
- POST /add_user       -> Add a user from JSON body (expects `username`)
"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """
    Root endpoint that returns a short welcome string.

    Returns:
        str: Welcome message displayed to clients.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """
    Return a JSON array containing all stored usernames.

    Returns:
        Response: JSON list of usernames (list of str).
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Health-check endpoint.

    Returns:
        str: "OK" when the application is running.
    """
    return "OK"


@app.route("/users/<username>")
def user(username):
    """
    Retrieve a stored user by username.

    Args:
        username (str): Username to look up.

    Returns:
        Response or tuple: JSON representation of the user if found;
        otherwise a tuple (error dict, 404).
    """
    if username in users:
        return jsonify(users[username])
    else:
        return {"error": "User not found"}, 404


@app.route("/add_user")
def add_user():
    """
    Add a user from a JSON payload in the request body.

    Expected JSON payload example:
        {"username": "alice", "email": "alice@example.com"}

    Validation and responses:
    - 400: Invalid or missing JSON body.
    - 400: Missing required `username` key.
    - 409: Username already exists.
    - 201: User successfully created (response includes the stored user).

    Returns:
        tuple: (response dict, status_code)

    Side effects:
        Mutates the module-level `users` dict by adding the new user.
    """

    dictionnary = request.get_json()

    if dictionnary is None:
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
    app.run()
