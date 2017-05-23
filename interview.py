from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route('/')
def index():
    data = None
    with open('housebuying.csv', 'r') as f:
        data = f.readlines()

    stripped_data = []
    for d in data:
        stripped_data.append(d.strip())

    return render_template('index.html', data=stripped_data)

@app.route('/savedata', methods=['post'])
def save_data():
    data = request.get_data()

    try:
        datalist = json.loads(data)
    except:
        raise Exception("Invalid Data. Are you sure it's JSON encoded?")

    with open('housebuying1.csv', 'w') as f:
        for d in datalist:
            f.write("%s\r\n"%d)

    f.close()
    return 'OK'
