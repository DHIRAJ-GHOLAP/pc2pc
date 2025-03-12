# Desktop RAT Project (Portfolio Only)

A Remote Access Tool (RAT) designed strictly for ethical purposes and educational demonstrations. This tool showcases capabilities in browser automation, remote screenshot capture, and discreet keylogging.

## 🚀 Features

- **Browser Automation**
  - Open websites remotely.
  - Click buttons and elements.
  - Input text automatically.

- **Remote Surveillance**
  - Capture and remotely download screenshots.
  - Collect keystrokes (keylogging).

- **Remote Control**
  - Control victim PC activities remotely using a user-friendly GUI.

---

## 🛠️ Setup Guide

### 📌 Server Setup (Flask App - Render.com)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DHIRAJ-GHOLAP/pc2pc.git
   cd pc2pc/server
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Deploy to Render.com**:
   - Connect GitHub repository.
   - Set `app.py` as the startup file.

### 📌 Victim PC Setup

1. **Navigate to the victim directory**:
   ```bash
   cd RAT-Project/victim
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the victim script**:
   ```bash
   python victim.py
   ```

(Optional: Package as `.exe` with PyInstaller)

### 📌 Attacker GUI Setup

1. **Navigate to GUI directory**:
   ```bash
   cd RAT-Project/attacker_gui
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch GUI**:
   ```bash
   python gui.py
   ```

---

## 📖 Usage Instructions

- **Remote Command Execution**:
  - Use GUI to send commands to victim's PC.

- **Screenshots**:
  - Captured screenshots automatically upload to the server.

- **Keylogging**:
  - Keylogs captured from the victim PC can be downloaded via the `/download_log` endpoint.

---

## 📌 Project Structure
```
RAT-Project/
├── server/
│   ├── app.py
│   └── requirements.txt
│
├── victim/
│   ├── victim.py
│   └── requirements.txt
│
├── attacker_gui/
│   ├── gui.py
│   └── requirements.txt
│
└── README.md
```

---

## ⚙️ Dependencies

- **Server** (`requirements.txt`):
```
flask
```

- **Victim** (`requirements.txt`):
```
helium
selenium
requests
keyboard
```

- **Attacker GUI** (`requirements.txt`):
```
tkinter
requests
```

---

## ⚠️ Disclaimer

This project is intended solely for educational and ethical purposes. Unauthorized or malicious use is strictly prohibited and may lead to legal consequences.

