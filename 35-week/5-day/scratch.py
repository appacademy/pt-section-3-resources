import sqlite3

DB_FILE = "dev.db"

with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor()
    try:
        curs.execute(
            """
                CREATE TABLE jokes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                joke_body VARCHAR(250),
                punchline VARCHAR(250),
                rating VARCHAR(15)
                );
                """
        )
    except:
        curs.execute(
            """
                DROP TABLE jokes;
                """
        )
        curs.execute(
            """
                CREATE TABLE jokes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                joke_body VARCHAR(250),
                punchline VARCHAR(250),
                rating VARCHAR(15)
                );
                """
        )


def create_joke(joke_body, punchline, rating):
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            """
            INSERT INTO jokes (joke_body, punchline, rating)
            VALUES(:joke_body, :punchline, :rating)
            """,
            {"joke_body": joke_body, "punchline": punchline, "rating": rating},
        )


create_joke("lol", "haha", 2)
create_joke("lol", "haha", 3)
create_joke("lol", "haha", 4)
create_joke("lol", "haha", 5)
create_joke("lol", "haha", 6)
create_joke("lol", "haha", 7)

def get_all_spots():
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        q = curs.execute(
            """
            SELECT *
            FROM jokes
            LIMIT 1;
            """
        )
        # print("Q", q)
        # for row in q:
        #     print("TEST", row)
        # for row in curs.execute(
        #     """
        #     SELECT *
        #     FROM jokes;
        #     """
        # ):
            # print("HERE", row)
        results = curs.fetchall()
        print(results)

get_all_spots()
