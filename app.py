import socket
from flask import Flask

app = Flask(__name__)

def get_host_info():
    """
    get hostname and ip info
    """
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address

@app.route('/')
def hello():
    hostname, ip = get_host_info()
    return f"Hello, World<br>Hostname: {hostname}<br>IP Address: {ip}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

