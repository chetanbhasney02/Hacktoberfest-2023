from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    api_key = 'API-KEY'
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp_kelvin = data['main']['temp']
        temp_celsius = round(temp_kelvin - 273.15, 2)
        desc = data['weather'][0]['description']
        return render_template('result.html', temp=temp_celsius, desc=desc)
    else:
        return 'Error fetching weather data'

if __name__ == '__main__':
    app.run(debug=True)
