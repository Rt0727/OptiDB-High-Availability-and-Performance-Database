import psycopg2
from psycopg2 import sql

def promote_to_primary(replica_host, db_name, user, password):
    conn = connect_to_db(db_name, user, password, replica_host)
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT pg_promote();")
            conn.commit()
            print(f"Node {replica_host} promoted to primary successfully.")
        except Exception as e:
            print(f"Error promoting node: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    promote_to_primary("replica_host", "db_name", "admin", "password")