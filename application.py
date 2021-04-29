from flask import Flask
app = Flask(__name__)

import test

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/")
def home():
    return jsonify({'tasks': tasks})

# @app.route("/")
# def hello():
#     data = request.get_json()
#     return "Olá, moneynow ! "
