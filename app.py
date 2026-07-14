from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("models/model.pkl")

@app.route("/")
def home():
    return "ML Model API Running"

@app.route("/predictt", methods=["POST"])
def predict():

    data = request.get_json()

    F1 = data["F1"]
    F2 = data["F2"]

    input_data = pd.DataFrame({
        "F1": [F1],
        "F2": [F2]
    })

    prediction = model.predict(input_data)

    return jsonify({
        "prediction": float(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)