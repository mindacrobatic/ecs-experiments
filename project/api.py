import sys

import flask
import numpy as np
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

mem = list()


@app.route('/', methods=['GET'])
def home():
    return jsonify("Distant Reading Archive. This site is a "
                   "prototype API for distant reading of science fiction novels.")


@app.route('/health', methods=['GET'])
def health():
    return jsonify("OK")


@app.route('/cpu', methods=['GET'])
def cpu():

    k = 0
    for i in range(1000000):
        k += np.sqrt(i)

    return jsonify(k)


@app.route('/memory', methods=['GET'])
def memory():

    global mem

    a = "Hello Wooooooooooooooooooooooooooooooooooooooooooooooooooooorld" * 10000000

    mem.append(a)

    return jsonify("Done")


@app.route("/length", methods=["GET"])
def mem_get():

    global mem

    return jsonify(sys.getsizeof(mem))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
