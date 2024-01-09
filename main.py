import pandas as pd
import tkinter as tk
from tkinter import filedialog
import pyautogui as pg
import time
import webbrowser

def searchCon(contact, message):
    pg.hotkey('ctrl', 'n')
    time.sleep(1)
    pg.write(contact)
    time.sleep(1)
    pg.press("tab")
    time.sleep(1)
    pg.press("enter")
    time.sleep(1)
    pg.write(message)
    pg.press("enter")

def send_messages(csv_path, contact_column, message_entry):
    try:
        data = pd.read_csv(csv_path)
        msg = message_entry.get()

        if contact_column not in data.columns:
            raise ValueError(f"Column '{contact_column}' not found in the CSV file.")

        for x in data.index:
            searchCon(str(data[contact_column][x]), msg)
            time.sleep(1)

    except Exception as e:
        print(f"Error: {e}")
        # Handle the error (e.g., show a messagebox to the user)

def browse_csv_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def open_website():
    webbrowser.open("https://omkarkamat.web.app")

def create_gui():
    root = tk.Tk()
    root.title("WhatsApp Message Sender")

    csv_label = tk.Label(root, text="Select CSV File:")
    csv_label.pack()

    csv_entry = tk.Entry(root, width=50)
    csv_entry.pack()

    browse_button = tk.Button(root, text="Browse", command=lambda: browse_csv_file(csv_entry))
    browse_button.pack()

    contact_column_label = tk.Label(root, text="Enter Contact Column Name:")
    contact_column_label.pack()

    contact_column_entry = tk.Entry(root, width=50)
    contact_column_entry.pack()

    message_label = tk.Label(root, text="Enter Message:")
    message_label.pack()

    message_entry = tk.Entry(root, width=50)
    message_entry.pack()

    send_button = tk.Button(root, text="Send Messages", command=lambda: send_messages(csv_entry.get(), contact_column_entry.get(), message_entry))
    send_button.pack()

    website_label = tk.Label(root, text="Developed By ")
    website_label.pack()

    website_link = tk.Label(root, text="Omkar Kamat", fg="blue", cursor="hand2")
    website_link.pack()
    website_link.bind("<Button-1>", lambda event: open_website())

    root.mainloop()

if __name__ == "__main__":
    create_gui()
