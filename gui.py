import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "phids.db"

def add_observation():
    """Open the graphical wildlife observation entry form."""

    window = tk.Toplevel(root)
    window.title("PHIDS - Add Wildlife Observation")
    window.geometry("600x650")
    window.configure(bg="#14281D")

    heading = tk.Label(
        window,
        text="ADD WILDLIFE OBSERVATION",
        font=("Arial", 20, "bold"),
        fg="#D4AF37",
        bg="#14281D"
    )
    heading.pack(pady=20)

    fields = [
        "Nickname",
        "Species",
        "Sex",
        "Date (YYYY-MM-DD)",
        "Time",
        "Location",
        "County",
        "State",
        "Notes"
    ]

    entries = {}

    for field in fields:
        label = tk.Label(
            window,
            text=field,
            font=("Arial", 11),
            fg="white",
            bg="#14281D"
        )
        label.pack()

        entry = tk.Entry(
            window,
            font=("Arial", 11),
            width=40
        )
        entry.pack(pady=(0, 8))
        entries[field] = entry

    def save_observation():
        """Save the observation to the PHIDS database."""

        nickname = entries["Nickname"].get().strip()
        species = entries["Species"].get().strip()
        sex = entries["Sex"].get().strip()
        date = entries["Date (YYYY-MM-DD)"].get().strip()
        time = entries["Time"].get().strip()
        location = entries["Location"].get().strip()
        county = entries["County"].get().strip()
        state = entries["State"].get().strip()
        notes = entries["Notes"].get().strip()

        # Check required fields
        if not species or not date:
            messagebox.showwarning(
                "Missing Information",
                "Species and Date are required."
            )
            return

        # Save to SQLite
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO sightings (
                    nickname,
                    species,
                    sex,
                    sighting_date,
                    sighting_time,
                    location,
                    county,
                    state,
                    notes
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                nickname,
                species,
                sex,
                date,
                time,
                location,
                county,
                state,
                notes
            ))

            connection.commit()

        messagebox.showinfo(
            "PHIDS",
            "Wildlife observation saved successfully!"
        )

        window.destroy()

    # Save button for the observation form
    save_button = tk.Button(
        window,
        text="SAVE OBSERVATION",
        font=("Arial", 12, "bold"),
        bg="#D4AF37",
        fg="black",
        activebackground="#FF8C00",
        width=25,
        height=2,
        command=save_observation
    )
    save_button.pack(pady=15)


def view_observations():
    """Display saved wildlife observations in a graphical window."""

    # Create a new window
    window = tk.Toplevel(root)
    window.title("PHIDS - Wildlife Observations")
    window.geometry("1100x500")
    window.configure(bg="#14281D")

    # Window heading
    heading = tk.Label(
        window,
        text="WILDLIFE OBSERVATIONS",
        font=("Arial", 20, "bold"),
        fg="#D4AF37",
        bg="#14281D"
    )
    heading.pack(pady=20)

    # Create observation table
    columns = (
        "ID",
        "Nickname",
        "Species",
        "Sex",
        "Date",
        "Time",
        "Location",
        "County",
        "State"
    )

    table = ttk.Treeview(
        window,
        columns=columns,
        show="headings"
    )

    for column in columns:
        table.heading(column, text=column)
        table.column(column, width=120)

    table.pack(fill="both", expand=True, padx=20, pady=10)

    # Retrieve existing observations
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                id,
                nickname,
                species,
                sex,
                sighting_date,
                sighting_time,
                location,
                county,
                state
            FROM sightings
            ORDER BY id DESC
        """)

        observations = cursor.fetchall()

    # Add records to the table
    for observation in observations:
        table.insert("", "end", values=observation)


import subprocess
import sys

subprocess.run(
    [sys.executable, str(Path(__file__).resolve().parent / "splash.py")],
    check=True
)

# PHIDS Main Application Window
root = tk.Tk()
root.title("PHIDS - Portable Hunting Intelligence & Data System")
root.geometry("1000x650")
root.configure(bg="#14281D")

# Application Header
header = tk.Frame(root, bg="#203B2B", height=90)
header.pack(fill="x")

title = tk.Label(
    header,
    text="PHIDS",
    font=("Arial", 32, "bold"),
    fg="#D4AF37",
    bg="#203B2B"
)
title.pack(pady=(10, 0))

subtitle = tk.Label(
    header,
    text="Portable Hunting Intelligence & Data System",
    font=("Arial", 11),
    fg="white",
    bg="#203B2B"
)
subtitle.pack()

# Dashboard Heading
dashboard_label = tk.Label(
    root,
    text="WILDLIFE INTELLIGENCE DASHBOARD",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#14281D"
)
dashboard_label.pack(pady=30)

# Navigation Buttons
button_frame = tk.Frame(root, bg="#14281D")
button_frame.pack(pady=20)

buttons = [
    "Add Observation",
    "View Observations",
    "Wildlife Map",
    "Hunting Intelligence"
]

for index, button_text in enumerate(buttons):
    button = tk.Button(
        button_frame,
        text=button_text,
        font=("Arial", 12, "bold"),
        width=22,
        height=3,
        bg="#2E5038",
        fg="white",
        activebackground="#D4AF37",
        activeforeground="black",
        relief="flat",
        state="normal" if index < 2 else "disabled",
        command=add_observation if index == 0 else view_observations if index == 1 else None
    )
    button.grid(
        row=index // 2,
        column=index % 2,
        padx=15,
        pady=15
    )

# Footer
footer = tk.Label(
    root,
    text="METZ FORGE | PHIDS DEVELOPMENT",
    font=("Arial", 10),
    fg="#D4AF37",
    bg="#14281D"
)
footer.pack(side="bottom", pady=15)

root.mainloop()