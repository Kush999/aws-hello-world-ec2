from flask import Flask
import requests

app = Flask(__name__)

def get_instance_id():
    try:
        url = "http://169.254.169.254/latest/meta-data/instance-id"
        response = requests.get('url', timeout=1)
        if response.status_code == 200:
            return response.text
        else:
            return "Unknown"
    except requests.RequestException:
        return "Unknown"
    
@app.route('/')
def hello():
    instance_id = get_instance_id()
    return f"Hello, World! Instance ID: {instance_id}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)