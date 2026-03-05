import sqlite3

# class is not complete just tried to start something that will need to change
class database_controller:
    def __init__(self):
        print("database_controller initialized")

    def init_event_db(self):
        con = sqlite3.connect("events.db")
        cur = con.cursor()
        create_event_table_query = "CREATE TABLE IF NOT EXISTS events(name, description, location, start, duration, food, media)"
        cur.execute(create_event_table_query)
        con.commit()
        con.close()

    def init_source_db():
        con = sqlite3.connect("sources.db")
        cur = con.cursor()

        create_discord_table_query = "CREATE TABLE IF NOT EXISTS discord(...)"
        create_email_table_query = "CREATE TABLE IF NOT EXISTS mail(...)"

        cur.execute(create_discord_table_query)
        cur.execute(create_email_table_query)
        con.commit()
        con.close()

    def insert_event(self, request_body):
        con = sqlite3.connect("events.db")
        cur = con.cursor()

        cur.execute("INSERT INTO event(name, description, location, start, duration, food, media) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (request_body["name"], request_body["description"],
         request_body["location"], request_body["start"],
         request_body["duration"], request_body["food"],
         request_body["media"]))

        con.commit()
        con.close()

    def insert_discord(self, request_body):
        con = sqlite3.connect("events.db")
        cur = con.cursor()

        cur.execute("INSERT INTO event(server_id, channel_ids) VALUES (?, ?)",
        (request_body["server_id"], request_body["channel_ids"]))

        con.commit()
        con.close()

    def retrieve_events(self):
        con = sqlite3.connect("events.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM event")
        rows = cur.fetchall()

        con.close()

        return rows

    def retrieve_event(self):
        return None
