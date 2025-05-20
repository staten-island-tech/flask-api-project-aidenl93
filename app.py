from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    page = request.args.get('page', 1, type=int)
    response = requests.get('https://api.fbi.gov/wanted/v1/list', params={
    'race': 'asian',
    'page': page,
    'pagesize': 200
})
    data = response.json()
    return render_template('index.html', items=data['items'], page=page, total=data['total'])
@app.route("/wanted/<uid>")
def wanted(uid):
    response = requests.get('https://api.fbi.gov/wanted/v1/list', params={
    'race': 'asian'
})
    data = response.json()
    # Find the person by uid
    for item in data['items']:
        if item['uid'] == uid:
            return render_template('wanted.html', item=item)

    return "Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)