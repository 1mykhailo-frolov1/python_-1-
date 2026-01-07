import sqlite3
from datetime import datetime


conn = sqlite3.connect("security_events.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")



cursor.execute("""
CREATE TABLE IF NOT EXISTS EventSources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    location TEXT,
    type TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS EventTypes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT UNIQUE,
    severity TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS SecurityEvents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME,
    source_id INTEGER,
    event_type_id INTEGER,
    message TEXT,
    ip_address TEXT,
    username TEXT,
    FOREIGN KEY (source_id) REFERENCES EventSources(id),
    FOREIGN KEY (event_type_id) REFERENCES EventTypes(id)
)
""")

conn.commit()


event_types = [
    ("Login Success", "Informational"),
    ("Login Failed", "Warning"),
    ("Port Scan Detected", "Warning"),
    ("Malware Alert", "Critical")
]

cursor.executemany("""
INSERT OR IGNORE INTO EventTypes (type_name, severity)
VALUES (?, ?)
""", event_types)


sources = [
    ("Firewall_A", "192.168.1.1", "Firewall"),
    ("Web_Server", "192.168.1.10", "Web Server"),
    ("IDS_Sensor", "192.168.1.20", "IDS")
]

cursor.executemany("""
INSERT OR IGNORE INTO EventSources (name, location, type)
VALUES (?, ?, ?)
""", sources)

conn.commit()


def add_security_event(source_id, event_type_id, message, ip=None, user=None):
    cursor.execute("""
    INSERT INTO SecurityEvents
    (timestamp, source_id, event_type_id, message, ip_address, username)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (datetime.now(), source_id, event_type_id, message, ip, user))
    conn.commit()


for i in range(10):
    add_security_event(
        source_id=2,
        event_type_id=2,
        message="Login failed for user",
        ip="192.168.1.100",
        user="Frolov_Mykhailo"
    )


print("Login Failed за 24 часа:")
cursor.execute("""
SELECT * FROM SecurityEvents
WHERE event_type_id = (
    SELECT id FROM EventTypes WHERE type_name = 'Login Failed'
)
AND timestamp >= datetime('now', '-1 day')
""")
print(cursor.fetchall())

conn.close()