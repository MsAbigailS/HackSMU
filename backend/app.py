from flask import Flask, request
from keras.models import load_model
from twilio.rest import Client
import json
from flask_cors import CORS

secrets = json.load(open("secrets.json", "r"))
model = load_model("predictive_maintenance.h5")
twilio_client = Client(secrets["twilio_sid"], secrets["twilio_token"])

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/predict", methods=["POST"])
def predict():
    args = request.form
    print(args)
    air_temp = float(args["outside_temp"])
    process_temp = float(args["elevator_temp"])
    rot_speed = float(args["elevator_speed"])
    torque = float(args["door_speed"])
    tool_wear = float(args["usage_time"])
    print("Received perdiction request with args: {}".format(args))
    model = load_model("predictive_maintenance.h5")
    prediction = (
        model.predict([[air_temp, process_temp, rot_speed, torque, tool_wear]])[0][1]
        * 100
    )
    if prediction < 20:
        return "Good Condition"
    if prediction < 25:
        return "Maintenance Required"
    else:
        return "Critical Condition"


@app.route("/notify_technicians", methods=["POST"])
def notify_technicians():
    args = request.form
    print("Received notification request with args: {}".format(args))
    for tech in secrets["technicians"]:
        twilio_client.messages.create(
            body="{}".format(args["elevator_id"]),
            from_=secrets["twilio_number"],
            to=tech,
        )
    return "OK"
