from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/camera_microphone', methods=['POST'])
def camera_microphone():
    allow_access = request.form.get('allow_access')
    if allow_access == 'yes':
        # Implementimi i kodit për të aktivizuar kamerën dhe mikrofonin

        # Shfaqja e informacionit të pajisjes në terminal
        device_info = os.popen('some_command_to_get_device_info').read()
        return f"Access granted. Device information:\n{device_info}"
    else:
        return "Access denied."

@app.route('/stop_camera_microphone', methods=['POST'])
def stop_camera_microphone():
    stop_access = request.form.get('stop_access')
    if stop_access == 'yes':
        # Implementimi i kodit për të ndaluar kamerën dhe mikrofonin

        return "Camera and microphone access stopped."
    else:
        return "Continuing camera and microphone access."

if __name__ == '__main__':
    server_method = input("Choose server method (localhost/cloudfare/ngrok): ")
    if server_method == 'localhost':
        app.run()
    elif server_method == 'cloudfare':
        app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
    elif server_method == 'ngrok':
        app.run(host='0.0.0.0', port=80)
    else:
        print("Invalid server method. Please choose either localhost, cloudfare, or ngrok.")
