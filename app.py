from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = '8e48fa366467b47c97288f76783b203a'  # Replace with your actual API key

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = {}
    if request.method == 'POST':
        city = request.form['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            main_condition = data['weather'][0]['main'].lower()

            # Decide theme based on weather condition
            if 'rain' in main_condition:
                theme = 'rainy'
            elif 'clear' in main_condition:
                theme = 'sunny'
            elif 'snow' in main_condition:
                theme = 'snow'
            elif 'cloud' in main_condition:
                theme = 'cloudy'
            else:
                theme = 'default'

            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'icon': data['weather'][0]['icon'],
                'theme': theme
            }
        else:
            weather['error'] = 'City not found!'
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
