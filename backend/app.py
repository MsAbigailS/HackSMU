from flask import Flask, request
from keras.models import load_model

app = Flask(__name__)

model = load_model("predictive_maintenance.h5")


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/predict", methods=["POST"])
def predict():
    args = request.form
    air_temp = args["outside_temp"]
    process_temp = args["elevator_temp"]
    rot_speed = args["elevator_speed"]
    torque = args["door_speed"]
    tool_wear = args["usage_time"]
    print("Received perdiction request with args: {}".format(args))
    model = load_model("predictive_maintenance.h5")
    return str(model.predict([[air_temp, process_temp, rot_speed, torque, tool_wear]]))
