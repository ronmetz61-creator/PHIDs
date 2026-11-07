import sqlite3
from pathlib import Path

# PHIDS - Portable Hunting Intelligence & Data System
# Phase 2: Interactive Wildlife Database

DB_PATH = Path(__file__).resolve().parent / "phids.db"


def view_sightings():
    """Display wildlife sightings stored in SQLite."""

    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sightings ORDER BY id")
        sightings = cursor.fetchall()

    if not sightings:
        print("\nNo wildlife sightings recorded yet.")
        return

    print("\n========== PHIDS WILDLIFE SIGHTINGS ==========")

    for sighting in sightings:
        print(f"\nRecord ID: {sighting[0]}")
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


def main():
    while True:
        print("\n========== PHIDS ==========")
        print("1. View Wildlife Sightings")
        print("2. Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            view_sightings()

        elif choice == "2":
            print("\nClosing PHIDS. Happy hunting!")
            break

        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    import subprocess
    import sys

    # Display PHIDS splash screen before luanching the main menu
    subprocess.run(
        [sys.executable, str(Path(__file__).resolve().parent / "splash.py")],
        check=True
    )

    # Launch the interactive PHIDS menu
    main()