import re
import flask
import CADOCS
import json
from flask import request

app = flask.Flask(__name__)

prediction_service = CADOCS.PredictionService()


@app.route('/predict', methods=['GET'])
def predict():
    if 'message' in request.args:
        message = str(request.args['message'])
    else:
        return "Error: No message to provide to the model. Please insert a valid message."

    # message = "hello CADOCS, show me the community smells in the repository https://github.com/tensorflow/ranking from 21/05/2020"
    re_equ = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    ck_url = re.findall(re_equ, message)
    entities = {
        "url": "",
        "date": ""
    }
    if ck_url:
        entities.update({"url": [i[0] for i in ck_url][0]})
        message = message.replace([i[0] for i in ck_url][0], "LINK")
    date = re.findall('\d{2}/\d{2}/\d{4}', message)
    if date:
        entities.update({"date": date[0]})

    result = {"intent": prediction_service.predict(
        message), "entities": entities}

    return json.dumps(result)


app.run()
