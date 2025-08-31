import sqlite3

# connect to the same file app.py is using
conn = sqlite3.connect("cipherkeep_ui.db")
cur = conn.cursor()

print("Tables in this DB:")
for row in cur.execute("SELECT name FROM sqlite_master WHERE type='table';"):
    print(row)

print("\nUsers:")
for row in cur.execute("SELECT id, username, auth_salt_b64, kdf_salt_b64 FROM users;"):
    print(row)

print("\nPII Records:")
for row in cur.execute("SELECT owner_id, field_name, nonce_b64, ciphertext_b64 FROM pii_record;"):
    print(row)

conn.close()
