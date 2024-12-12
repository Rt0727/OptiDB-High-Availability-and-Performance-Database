import psycopg2

def check_db_health(host, db_name, user, password):
    conn = connect_to_db(db_name, user, password, host)
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT pg_is_in_recovery();")
            recovery_status = cursor.fetchone()[0]
            if recovery_status:
                print(f"Node {host} is in recovery mode (replica).")
            else:
                print(f"Node {host} is primary.")
        except Exception as e:
            print(f"Error checking health: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    check_db_health("primary_host", "db_name", "admin", "password")
    check_db_health("replica_host", "db_name", "admin", "password")