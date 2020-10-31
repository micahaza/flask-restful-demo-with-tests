from flask import Flask, jsonify
# import requests


app = Flask(__name__)


@app.route('/')
def users():
    ret = {'asd': 23, 'uuu': 34, 'etc': 349}
    resp = jsonify(ret)
    resp.status_code = 200
    return resp


@app.route('/last')
def last_item():
    return 'last item'


@app.route('/grab_and_save', methods=["POST"])
def grab_and_save():
    return 'hello'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
