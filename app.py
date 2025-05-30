from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    page = request.args.get('page', 1, type=int)
    name = request.args.get('name', '', type=str)
    offices = request.args.get('offices', '', type=str)
    if page > 5:
        return "theres only 5 pages why u tryna hack the system", 404
    params = {
        "page": page,
        "pagesize": 20
    }
    if name:
        params["title"] = name
    if offices:
        params["field_offices"] = offices
    response = requests.get('https://api.fbi.gov/wanted/v1/list', params=params)
    data = response.json()
    return render_template('index.html', items=data['items'], page=page, total=data['total'], name=name)
@app.route("/wanted/<uid>")
def wanted(uid):
    for page in range(1, 52):  
        response = requests.get('https://api.fbi.gov/wanted/v1/list', params={
            'page': page,
            'pagesize': 20
        })
        data = response.json()
        for item in data.get('items', []):
            if item.get('uid') == uid:
                return render_template('wanted.html', item=item)
    
    return "Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)