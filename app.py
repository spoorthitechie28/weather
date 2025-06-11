from flask import Flask, render_template, request
import requests
import os

API_KEY = os.getenv('API_KEY')


app = Flask(__name__)

API_KEY = '8e48fa366467b47c97288f76783b203a'  # Replace with real API key

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = {}
    if request.method == 'POST':
        city = request.form['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'icon': data['weather'][0]['icon']  # NEW
            }
        else:
            weather['error'] = 'City not found!'
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
