from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)
time_requests_count = 0

@app.route('/time', methods=['GET'])
def get_time():
    global time_requests_count
    time_requests_count += 1
    response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow')
    if response.status_code == 200:
        return response.json()['datetime']
    else:
        return f"Ошибка при запросе{response.status_code}"

@app.route('/statistics', methods=['GET'])
def get_statistics():
    return jsonify({'time_requests_count': time_requests_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
