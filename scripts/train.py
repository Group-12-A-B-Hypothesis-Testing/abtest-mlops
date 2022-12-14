import os
import warnings
import sys

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.linear_model import LogisticRegression

from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn

import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# Get url from DVC
import dvc.api

# path = 'dvc_data/AdSmartABdata.csv'
# #FIXME: We will have to change the path  according to the path of our local machines
# repo = 'C:/Users/Kamuzinzi N. Egide/Documents/Ten_academy/week 2/Ad-campaign-performance'
# version = 'v1'

# data_url = dvc.api.get_url(
#     path = path,
#     repo = repo,
#     rev = version
# )
mlflow.set_experiment('Linear Regression model ')


def encode_labels(df):
    date_encoder = preprocessing.LabelEncoder()
    device_encoder = preprocessing.LabelEncoder()
    browser_encoder = preprocessing.LabelEncoder()
    experiment_encoder = preprocessing.LabelEncoder()
    aware_encoder = preprocessing.LabelEncoder()
    
    df['date'] = date_encoder.fit_transform(df['date'])
    df['device_make'] = device_encoder.fit_transform(df['device_make'])
    df['browser'] = browser_encoder.fit_transform(df['browser'])
    df['experiment'] = experiment_encoder.fit_transform(df['experiment'])
    df['browser'] = aware_encoder.fit_transform(df['browser'])
    df['yes'] = aware_encoder.fit_transform(df['yes'])
    
    return df    


def feature_data(df):
    
    browser_feature_df = df[["experiment", "hour", "date", 'device_make', 'browser', 'yes']] 
    platform_feature_df = df[["experiment", "hour", "date", 'device_make', 'platform_os', 'yes']] 

    return browser_feature_df, platform_feature_df

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)


    # data = pd.read_csv(data_url, sep=";")
    # print(data.columns)
    data = pd.read_csv("data/encoded_data.csv")   
    data = data[data.columns.tolist()[2:]]
    print(data.columns)


    # cleaned_data = encode_labels(df)

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)

    # FIXME: change the predicted column to the column of our target in the dataset
    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["yes"], axis=1)
    test_x = test.drop(["yes"], axis=1)
    train_y = train[["yes"]]
    test_y = test[["yes"]]

    alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

    # TODO: This will be changed to our model
    with mlflow.start_run():
        lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        predicted_qualities = lr.predict(test_x)

        (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)


        print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)
        print(predicted_qualities)
        # print("  Accuracy: %s" % metrics.accuracy_score(test_y,predicted_qualities))

        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Model registry does not work with file store
        if tracking_url_type_store != "file":

            # Register the model
            # There are other ways to use the Model Registry, which depends on the use case,
            # please refer to the doc for more information:
            # https://mlflow.org/docs/latest/model-registry.html#api-workflow
            mlflow.sklearn.log_model(lr, "model", registered_model_name="ElasticnetWineModel")
        else:
            mlflow.sklearn.log_model(lr, "model")