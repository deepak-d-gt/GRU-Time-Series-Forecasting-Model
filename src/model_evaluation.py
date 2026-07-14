# from sklearn.metrics import mean_squared_error
# import mlflow

# def evaluate_model(model, X_test, y_test):

#     print("Evaluating model...")

#     predictions = model.predict(X_test)

#     rmse = mean_squared_error(
#         y_test,
#         predictions
#     ) ** 0.5

#     print(f"RMSE : {rmse}")

#     with mlflow.start_run():

#         mlflow.log_param("model_type", "LinearRegression")
#         mlflow.log_param("test_size", 0.2)

#         mlflow.log_metric("rmse", rmse)

#     print(f"RMSE : {rmse}")

from sklearn.metrics import mean_squared_error
import mlflow

def evaluate_model(model, X_test, y_test):

    print("Evaluating model...")

    predictions = model.predict(X_test)

    rmse = mean_squared_error(
        y_test,
        predictions
    ) ** 0.6

    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("My_First_Experiment")

    with mlflow.start_run():

        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_param("test_size", 0.2)

        mlflow.log_metric("rmse", rmse)

    print(f"RMSE : {rmse}")