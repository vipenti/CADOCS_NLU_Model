import re
import flask
import CADOCS
import json
from flask import request

app = flask.Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    if 'message' in request.args:
        message = str(request.args['message'])
    else:
        return "Error: No message to provide to the model. Please insert a valid message."

    # message = "hello CADOCS, show me the community smells in the repository https://github.com/tensorflow/ranking from 21/05/2020"
    re_equ = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    ck_url = re.findall(re_equ, message)
    if ck_url:
        message = message.replace([i[0] for i in ck_url][0], "LINK")

    model = CADOCS.CADOCSModel()
    result = {"intent": model.give_prediction(message), "entities": ck_url}

    return json.dumps(result)

# Gets a new message with the corresponding intent, and add it as a new row to the existing dataset
# If enough items have been added, the model re-trains
@app.route('/update_dataset', methods=['GET'])
def update_dataset():
    if 'message' in request.args and 'intent' in request.args:
        message = str(request.args['message'])
        intent = str(request.args['intent'])
    else:
        return "Error: The past message or intent is incorrect. Please provide the right parameters."

    model = CADOCS.CADOCSModel()
    model.update_dataset(message, intent)

    return

app.run()