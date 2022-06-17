from flask import Flask, request
import os
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getWeather():
    args = request.args
    
    lat = args['lat']
    lon = args['lon']
    api_key = os.environ['API_KEY']
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}').text
    
    return f"{res}\n"

@app.route('/healthy', methods=['GET'])
def getHealth():
    res = 0
    return f"{res}\n"


if __name__ == "__main__":
    port=8081
    app.run(host="0.0.0.0", port=port)

