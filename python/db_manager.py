import psycopg2
from psycopg2 import sql
import os

def connect_to_db(db_name, user, password, host='localhost', port='5432'):
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Connection to database established successfully.")
        return connection
    except Exception as error:
        print(f"Error: {error}")
        return None

def create_replica(db_name, user, password, primary_host, replica_host):
    conn = connect_to_db(db_name, user, password, primary_host)
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT pg_create_physical_replication_slot('{replica_host}');")
            conn.commit()
            print(f"Replication slot created for replica: {replica_host}")
        except Exception as e:
            print(f"Error creating replica: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    create_replica("db_name", "admin", "password", "primary_host", "replica_host")