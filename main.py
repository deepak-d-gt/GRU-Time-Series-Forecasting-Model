# from src.data_ingestion import load_data
# from src.data_preprocessing import preprocess_data
# from src.model_building import train_model
# from src.model_evaluation import evaluate_model

# def main():

#     data = load_data()

#     X_train, X_test, y_train, y_test = preprocess_data(data)

#     model = train_model(X_train, y_train)

#     evaluate_model(model, X_test, y_test)



# if __name__ == "__main__":
#     main()


from prefect import flow, task

from src.data_ingestion import load_data
from src.data_preprocessing import preprocess_data
from src.model_building import train_model
from src.model_evaluation import evaluate_model


@task
def load():
    return load_data()


@task
def preprocess(data):
    return preprocess_data(data)


@task
def train(X_train, y_train):
    return train_model(X_train, y_train)


@task
def evaluate(model, X_test, y_test):
    return evaluate_model(model, X_test, y_test)


@flow(name="GRU Forecasting Pipeline")
def gru_pipeline():
    data = load()

    X_train, X_test, y_train, y_test = preprocess(data)

    model = train(X_train, y_train)

    evaluate(model, X_test, y_test)


if __name__ == "__main__":
    gru_pipeline()