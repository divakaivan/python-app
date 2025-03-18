import socket
import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return jsonify({
        'time': datetime.datetime.now().strftime('%I:%M:%S%p on %B %d, %Y'),
        'hostname': socket.gethostname(),
        'deployed_on': 'Kubernetes',
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
