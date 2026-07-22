# import joblib
# import pandas as pd

# model = joblib.load("models/model.pkl")

# Predicted = pd.DataFrame({
#     "F1": [35],
#     "F2": [45]
# })

# prediction = model.predict(Predicted)

# print(prediction)

import joblib
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

password = quote_plus(os.getenv("DB_PASSWORD"))

from urllib.parse import quote_plus

# password = quote_plus("Deepak@123#")   # replace with your actual password
password = quote_plus(os.getenv("DB_PASSWORD")) 


model = joblib.load("models/model.pkl")

Predicted = pd.DataFrame({
    "F1": [30],
    "F2": [40]
})

prediction = model.predict(Predicted)

# Create output dataframe
result_df = Predicted.copy()
# result_df.columns = ["f1", "f2"]
# result_df["prediction"] = prediction
result_df = result_df.rename(
    columns={
        "F1": "f1",
        "F2": "f2"
    }
)

result_df["prediction"] = prediction

print(result_df)

# PostgreSQL connection
engine = create_engine(
    f"postgresql://postgres:{password}@localhost:5432/master"
)

# Save into predictions table
result_df.to_sql(
    "prediction",
    engine,
    if_exists="append",
    index=False
)

print("Predictions saved to PostgreSQL")