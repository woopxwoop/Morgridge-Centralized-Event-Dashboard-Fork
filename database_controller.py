import sqlite3

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

    def insert_event(self):
        print("")

    def retrieve_events(self):
        print("")

    def retrieve_event(self):
        print("")
