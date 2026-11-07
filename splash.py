import tkinter as tk
from pathlib import Path

# PHIDS - Portable Hunting Intelligence & Data System
# Graphical startup screen

BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "assets" / "PHIDS_skull.png"

# Create application window
root = tk.Tk()
root.title("PHIDS")
root.geometry("900x700")
root.configure(bg="#101810")

# Load deer skull image
logo = tk.PhotoImage(file=str(LOGO_PATH))

# Resize image if necessary to fit window
scale = max(1, (logo.width() + 499) // 500,
            (logo.height() + 399) // 400)
logo = logo.subsample(scale, scale)

# Display skull
logo_label = tk.Label(
    root,
    image=logo,
    bg="#101810"
)
logo_label.pack(pady=25)

# PHIDS title
tk.Label(
    root,
    text="PHIDS",
    font=("Arial", 40, "bold"),
    fg="#D4AF37",
    bg="#101810"
).pack(pady=10)

# Full application name
tk.Label(
    root,
    text="Portable Hunting Intelligence & Data System",
    font=("Arial", 15),
    fg="white",
    bg="#101810"
).pack()

# Startup message
tk.Label(
    root,
    text="Initializing Wildlife Intelligence...",
    font=("Arial", 12),
    fg="#A0A0A0",
    bg="#101810"
).pack(pady=30)

root.mainloop()