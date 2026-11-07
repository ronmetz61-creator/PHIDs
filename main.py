import sqlite3
from pathlib import Path

# PHIDS - Portable Hunting Intelligence & Data System
# Phase 1: Wildlife Sighting Database

# Store the database inside the PHIDS project folder
DB_PATH = Path(__file__).resolve().parent / "phids.db"

# Connect to SQLite (creates the database if it doesn't exist)
connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# Create the wildlife sightings table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sightings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname TEXT,
    species TEXT NOT NULL,
    sex TEXT,
    sighting_date TEXT NOT NULL,
    sighting_time TEXT,
    location TEXT,
    county TEXT,
    state TEXT,
    notes TEXT
)
""")

# Insert the Bradleytown Bruiser only if not already recorded
cursor.execute("""
SELECT id FROM sightings
WHERE nickname = ? AND sighting_date = ?
""", ("Bradleytown Bruiser", "2026-11-07"))

if cursor.fetchone() is None:
    cursor.execute("""
    INSERT INTO sightings (
        nickname, species, sex, sighting_date,
        sighting_time, location, county, state, notes
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Bradleytown Bruiser",
        "White-tailed Deer",
        "Male",
        "2026-11-07",
        "12:50 PM (approx.)",
        "Bradleytown Road near Jackson Plummer Road",
        "Venango",
        "Pennsylvania",
        "Initial sighting. Identity of future sightings must be verified."
    ))

    connection.commit()
    print("Bradleytown Bruiser added successfully!")

else:
    print("Bradleytown Bruiser already exists in the database.")

# Retrieve and display all sightings
print("\n========== PHIDS WILDLIFE SIGHTINGS ==========\n")

cursor.execute("SELECT * FROM sightings")

for sighting in cursor.fetchall():
    print(f"Record ID: {sighting[0]}")
    print(f"Nickname: {sighting[1]}")
    print(f"Species: {sighting[2]}")
    print(f"Sex: {sighting[3]}")
    print(f"Date: {sighting[4]}")
    print(f"Time: {sighting[5]}")
    print(f"Location: {sighting[6]}")
    print(f"County: {sighting[7]}")
    print(f"State: {sighting[8]}")
    print(f"Notes: {sighting[9]}")
    print("-" * 45)

connection.close()

print("\nPHIDS database operation completed successfully!")