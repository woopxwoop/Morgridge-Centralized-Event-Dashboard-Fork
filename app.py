from flask import Flask, request, jsonify
import sqlite3
from database_controller import database_controller

app = Flask(__name__)
db = database_controller()
db.init_event_db()
db.init_source_db()

@app.post("/insert-event")
def insert_event():
    request_body = request.get_json()
    required_fields = {"name", "description", "location", "start", "duration",
                       "food", "media"}
    missing = required_fields - request_body.keys()
    if missing:
        return jsonify({
            "error": "Missing required fields",
            "missing": list(missing)
        }), 400

    if len(request_body.keys()) != len(required_fields):
        return jsonify({"error": "Too many fields in body", "received": list(request_body.keys())}), 400

    try:
        db.insert_event(request_body)
        return jsonify({"message": "Event inserted"}), 201

    except Exception as e:
        print(e)
        return jsonify({"message": "Something went wrong while trying to write, try again later"}), 500

@app.route("/retrieve-event", methods=["GET"])
def retrieve_events():
    try:
        events = db.retrieve_events()
        return jsonify(events), 200
    
    except Exception:
        return jsonify({"msg": "Something went wrong while trying to retrieve, try again later"}), 500


@app.route("/insert-discord", methods=["GET"])
def insert_discord():
    request_body = request.get_json()
    required_fields = {"server_id", "channel_ids",}
    missing = required_fields - request_body.keys()
    if missing:
        return jsonify({
            "error": "Missing required fields",
            "missing": list(missing)
        }), 400

    if len(request_body.keys()) != len(required_fields):
        return jsonify({"error": "Too many fields in body", "received": list(request_body.keys())}), 400

    try:
        events = db.insert_discord(request_body)
        return jsonify(events), 200
    
    except Exception:
        return jsonify({"msg": "Something went wrong while trying to retrieve, try again later"}), 500


@app.route("/retrieve-sample-event", methods=["GET"])
def sample():
    payload={
        "name": "UPL Research Talk 📚",
        "description": "The UPL is hosting a talk on getting into research as an undergrad for the first time! I’ll be sharing what I\’ve personally learned about reaching out to labs, finding advisors, and making the most of your time once you’re in. Whether you\'re interested in research for grad school, industry, or pure curiosity, feel free to stop by.",
        "location": "Morgridge Hall Rm. 1524",
        "start": "6:00 PM",
        "duration": "1 hour",
        "food": True,
        "media":
        ["https://cdn.discordapp.com/attachments/1423716763711045705/1473462011881848842/flyer.jpg?ex=69a180af&is=69a02f2f&hm=48183abc7d49de6070f133fa6ca6c1f18490fe424c85be3624f3b840ae8c2347&"]
    }
    return jsonify(payload), 200

