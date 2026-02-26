from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    con = sqlite3.connect("events.db")
    cur = con.cursor()
    create_table_query = "CREATE TABLE IF NOT EXISTS events(name, description, location, start, duration, food)"
    cur.execute(create_table_query)
    con.commit()
    con.close()

init_db()

@app.post("/insert")
def insert_event():
    request_body = request.get_json()
    required_fields = {"name", "description", "location", "start", "duration", "food"}
    missing = required_fields - request_body.keys()
    if missing:
        return jsonify({
            "error": "Missing required fields",
            "missing": list(missing)
        }), 400

    if len(request_body.keys()) != 6:
        return jsonify({"error": "Too many fields in body", "received": list(request_body.keys())}), 400

    try:
        con = sqlite3.connect("events.db")
        cur = con.cursor()

        cur.execute("INSERT INTO event(name, description, location, start, duration, food) VALUES (?, ?, ?, ?, ?, ?)",
        (request_body["name"], request_body["description"], request_body["location"], request_body["start"], request_body["duration"], request_body["food"]))

        con.commit()
        con.close()

        return jsonify({"message": "Event inserted"}), 201

    except Exception as e:
        print(e)
        return jsonify({"message": "Something went wrong while trying to write, try again later"}), 500

@app.route("/retrieve", methods=["GET"])
def retrieve_events():
    try:
        con = sqlite3.connect("events.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM event")
        rows = cur.fetchall()

        con.close()

        return jsonify(rows), 200
    except Exception:
        return jsonify({"msg": "Something went wrong while trying to retrieve, try again later"}), 500

@app.route("/sample-data", methods=["GET"])
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




