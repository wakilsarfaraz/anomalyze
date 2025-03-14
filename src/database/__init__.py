import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="postgres",
        database="anomalyze_db",
        user="anomalyze",
        password="anomalyze_pass"
    )
    return conn
