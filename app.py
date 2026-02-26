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
        "name": "UPL Research Talk 📚",
        "description": """The UPL is hosting a talk on getting into research as
        an undergrad for the first time! I’ll be sharing what I\’ve personally
        learned about reaching out to labs, finding advisors, and making the
        most of your time once you’re in. Whether you\'re interested in research
        for grad school, industry, or pure curiosity, feel free to stop by.""",
        "location": "Morgridge Hall Rm. 1524",
        "start": "6:00 PM",
        "duration": "1 hour",
        "food": True,
        "media":
        ["https://cdn.discordapp.com/attachments/1423716763711045705/1473462011881848842/flyer.jpg?ex=69a180af&is=69a02f2f&hm=48183abc7d49de6070f133fa6ca6c1f18490fe424c85be3624f3b840ae8c2347&"]
    }
    return jsonify(payload)
