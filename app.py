from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    con = sqlite3.connect("events.db")
    cur = con.cursor()
    create_table_query = "CREATE TABLE IF NOT EXISTS event(name, description, location, start, duration, food)"
    cur.execute(create_table_query)
    con.commit()
    con.close()

init_db()

@app.post("/insert")
def insert_event():
    data = request.get_json()

    con = sqlite3.connect("events.db")
    cur = con.cursor()

    cur.execute(
        "INSERT INTO event(name, description, location, start, duration, food) VALUES (?, ?, ?, ?, ?, ?)",
        (data["name"], data["description"], data["location"],
         data["start"], data["duration"], data["food"])
    )

    con.commit()
    con.close()

    return jsonify({"message": "Event inserted"}), 201
  

@app.route("/retrieve", methods=["GET"])
def retrieve_events():
    con = sqlite3.connect("events.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM event")
    rows = cur.fetchall()

    con.close()

    return jsonify(rows)


@app.route("/sample-data", methods=["GET"])
def sample():
    payload={

    }
    return jsonify(payload)
