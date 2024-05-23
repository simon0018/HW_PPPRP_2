import requests
import time
import os

def fetch_statistics_and_write_to_file():
    flask_service_url = os.getenv('FLASK_SERVICE_URL', 'http://localhost:5000/statistics')
    while True:
        try:
            response = requests.get(flask_service_url)
            if response.status_code == 200:
                data = response.json()
                with open('/app/statistics.txt', 'a') as file:
                    file.write(f"Time requests count: {data['time_requests_count']} - Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            else:
                print(f"Failed to fetch statistics: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error during request: {e}")
        
        time.sleep(5)

if __name__ == "__main__":
    fetch_statistics_and_write_to_file()
