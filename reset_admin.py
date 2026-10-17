import os
import getpass
import psycopg
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

load_dotenv()

password = getpass.getpass("Enter new admin password: ")

if not password:
    raise SystemExit("Password cannot be empty")

with psycopg.connect(os.environ["DATABASE_URL"]) as con:
    with con.cursor() as cur:
        cur.execute(
            """
            UPDATE users
            SET password = %s, is_admin = %s
            WHERE username = %s
            RETURNING id
            """,
            (generate_password_hash(password), 1, "admin")
        )
        row = cur.fetchone()

if row:
    print("Admin password updated successfully!")
else:
    print("Admin account not found. No changes made.")