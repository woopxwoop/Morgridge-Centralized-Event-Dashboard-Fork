from flask import Flask
import sqlite3

app = Flask(__name__)

con = sqlite3.connect("events.db")
cur = con.cursor()
create_table_query = "CREATE TABLE event(name, description, location, start, duration, food)"
cur.execute(create_table_query)


@app.post("/insert")
def insert_event():
  

@app.route("/retrieve", methods=["GET", "POST"])
def retrieve_events():