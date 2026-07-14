from sklearn.linear_model import LinearRegression
import joblib

def train_model(X_train, y_train):

    print("Training model...")

    model = LinearRegression()

    model.fit(X_train, y_train)

    joblib.dump(model, "models/model.pkl")

    print("Model Build Successfully!")

    return model