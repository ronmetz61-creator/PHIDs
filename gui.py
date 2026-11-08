import tkinter as tk
from tkinter import ttk
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "phids.db"

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
        command=view_observations if index == 1 else None
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