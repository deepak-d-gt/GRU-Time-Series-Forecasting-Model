import joblib
import pandas as pd

model = joblib.load("models/model.pkl")

Predicted = pd.DataFrame({
    "F1": [35],
    "F2": [45]
})

prediction = model.predict(Predicted)

print(prediction)