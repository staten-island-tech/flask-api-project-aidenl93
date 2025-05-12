from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get('https://api.fbi.gov/wanted/v1/list')
    data = response.json()
    return render_template('index.html', items=data['items'])
def wanted():
    response = requests.get('https://api.fbi.gov/wanted/v1/list')
    data = response.json()
    return render_template('wanted.html', items=data['items'])


if __name__ == '__main__':
    app.run(debug=True)