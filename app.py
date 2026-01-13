from flask import Flask, render_template

app = Flask(__name__)

import json
from datetime import datetime

@app.route('/')
def index():
    with open('config.json', 'r') as f:
        data = json.load(f)
    data['current_year'] = datetime.now().year
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(debug=True)
