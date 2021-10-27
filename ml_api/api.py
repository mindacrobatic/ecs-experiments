import os
import json
import pickle

import flask
from flask import jsonify, request, abort

import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Load the iris dataset to get the target names
iris_dataset = load_iris()
iris_target_names = iris_dataset['target_names']

# Open the ML model
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + "/model.pickle", "rb") as fh:
    clf: RandomForestClassifier = pickle.load(fh)


@app.route('/', methods=['GET'])
def home():
    return jsonify("This is a flower prediction service!")


@app.route('/version', methods=['GET'])
def version():

    return jsonify({"version": 1})


@app.route('/health', methods=['GET'])
def health():
    return jsonify("OK")


@app.route("/predict", methods=["GET"])
def predict():

    # Get the request body as a json string and convert it to a list
    json_body = request.get_json()
    list_body = json.loads(json_body)

    # Health checks of the input
    try:
        assert isinstance(list_body, list)
        for item in list_body:
            assert isinstance(item, list)
    except:
        abort(400, 'Bad request. Wrong input format')
    else:
        # Get the model prediction as class numbers
        prediction: np.array = clf.predict(list_body)

        # Get the names of the predicted flower classes
        flower_results: np.array = iris_target_names[prediction]

        # Convert the prediction to a list to be able to jsonify it
        result = list(flower_results)

        return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
