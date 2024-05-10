"""simple flask app to return host info"""
import socket
from datetime import datetime 
from flask import Flask

"""
declare flask app
"""
app = Flask(__name__)

def get_host_info():
    """
    get hostname and ip info
    """
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address

"""declare route for app"""
@app.route('/')
def hello():
    """display system info"""
    hostname, ip = get_host_info()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello, World<br>Hostname: {hostname}<br>IP Address: {ip}<br>Current Time: {current_time}"

"""invoke script"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

