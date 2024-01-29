from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_ip():
    # Return the private IP address of the EC2 instance
    ip_address = socket.gethostbyname(socket.gethostname())
    return jsonify(ip=ip_address)

@app.route('/', methods=['POST'])
def stress_cpu():
    # Run the stress CPU script as a separate process
    subprocess.Popen(["python3", "stress_cpu.py"])
    return jsonify(status="CPU stress test started")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # Adjust the port if necessary
