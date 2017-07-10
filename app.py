from flask import Flask, render_template, request
import socket

# Initialize Flask application
app = Flask(__name__)


# Default route, print user's IP
@app.route("/")
def index():
    ip = request.remote_addr
    return "Hello from FLASK. My Hostname is: %s \n My IP address is: %s \n" % (socket.gethostname(), ip)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
