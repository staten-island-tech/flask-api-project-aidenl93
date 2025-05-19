from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get('https://api.fbi.gov/wanted/v1/list', params={
    "description": "Conspiracy to Commit Computer Hacking"
    
})
    data = response.json()
    return render_template('index.html', items=data['items'])
@app.route("/wanted/<uid>")
def wanted(uid):
    response = requests.get('https://api.fbi.gov/wanted/v1/list', params={
    "description": "Conspiracy to Commit Computer Hacking"
})
    data = response.json()

    # Find the person by uid
    for item in data['items']:
        if item['uid'] == uid:
            return render_template('wanted.html', item=item)

    return "Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)