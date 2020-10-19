from flask import Flask, jsonify, request
from database import cursor
import json

app = Flask(__name__)


@app.route("/")
def index():
    cursor.execute("SELECT * FROM parking")
    result = cursor.fetchall()
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    return jsonify(result)


@app.route("/<pin>")
def show(pin):
    cursor.execute("SELECT * FROM parking WHERE pin = " + pin)
    result = cursor.fetchone()
    return jsonify(result)


@app.route("/<pin>", methods=["PUT"])
def update(pin):
    data = json.loads(request.data)
    cursor.execute("UPDATE parking SET status = " + str(data['status']) +
                   " WHERE pin = " + pin)
    return jsonify('updated')


if __name__ == "__main__":
    app.run(debug=True)
