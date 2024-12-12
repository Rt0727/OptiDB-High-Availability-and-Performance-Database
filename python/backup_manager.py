import subprocess
import os
from datetime import datetime

def backup_postgres(db_name, user, backup_dir, password):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = os.path.join(backup_dir, f"{db_name}_backup_{timestamp}.sql")
    os.environ['PGPASSWORD'] = password

    backup_command = f"pg_dump -U {user} -F c {db_name} > {backup_file}"

    try:
        subprocess.run(backup_command, shell=True, check=True)
        print(f"Backup completed successfully. File saved as {backup_file}")
    except subprocess.CalledProcessError as error:
        print(f"Error during backup: {error}")

if __name__ == "__main__":
    backup_postgres("db_name", "admin", "/path/to/backups", "password")