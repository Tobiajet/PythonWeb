import os
import socket
import socketserver
from flask import Flask, jsonify, render_template
from redis import Redis
app = Flask(__name__)
redis = Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])
bind_port = int(os.environ['BIND_PORT'])

def fetchDetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname), str(host_ip)
@app.route('/')
def hello():
    redis.incr('hits')
    total_hits = redis.get('hits').decode()
    return f'Hello from Redis! I have been seen {total_hits} times.'
@app.route('/health')
def health():
    return jsonify(
        status='UP'
    )
@app.route('/details')
def details():
    hostname, ip = fetchDetails()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=bind_port)