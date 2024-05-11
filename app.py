# Author: Ryan Tiffany
# Copyright (c) 2024
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

__author__ = 'ryantiffany'

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

