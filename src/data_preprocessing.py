from sklearn.model_selection import train_test_split

from src.config import load_config


# test_size = config["test_size"]
# random_state = config["random_state"]

def preprocess_data(data):

    print("Preprocessing data...")

    config = load_config()

    X = data[["F1", "F2"]]
    y = data["T"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size = config["test_size"],
        random_state = config["random_state"]
    )

    return X_train, X_test, y_train, y_test