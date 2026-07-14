from src.data_ingestion import load_data
from src.data_preprocessing import preprocess_data
from src.model_building import train_model
from src.model_evaluation import evaluate_model

def main():

    data = load_data()

    X_train, X_test, y_train, y_test = preprocess_data(data)

    model = train_model(X_train, y_train)

    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()