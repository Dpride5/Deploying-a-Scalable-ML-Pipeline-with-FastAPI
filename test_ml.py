import pytest
import numpy as pd
from ml.data improt process_data
from ml.model import (
    compute_model_metrics,
    train_model,
)
from sklearn.linear_model import LogisticRegression

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    Testing if the train_model function returns a model of the type that is expected.

    """
    data = pd.DataFrame(
        {
            "feature1": [1, 2, 3, 4, 5],
            "feature2": [0, 1, 0, 1, 0],
            "label": [0, 1, 0, 1, 0],
        }
    )

    # Process data
    X_train, y_train, _, _ = process_data(
        data,
        categorical_features=["feature2"],
        label="label",
        training=True,
    )

    #Train Model
    model = train_model(X_train, y_train)

    #Check if model returned train_model is of the expected type
    expected_model_type = LogisticRegression

    assert isinstance(model,expected_model_type)

# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    Test the machine learning model's algorithm.
    """
    data = pd.DataFrame(
        {
            "feature1": [1,2,3,4,5],
            "feature2": [0,1,0,1,0],
            "label": [0,1,0,1,0],
        }
    )
    
    X_train, y_train, _, _ = process_data(
        data,
        categorical_features = ["feature2"],
        label="label",
        training=True,
    )

    model = train_model(X_train, y_train)

    assert isinstance(model, LogisticRegression)


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    Testing if the compute_model_metrics function returns the expected values.
    """
    # Define a test set with controlled values
    y_true = np.array([0,1,0,1,0])
    y_pred = np.array([0,1,1,1,0])
    
    # Compute the metrics
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    # Checking if the computed metrics match the expected values
    expected_precision = 0.6667
    expected_recall = 1.0
    expected_fbeta = 0.8

    assert round(precision, 4) == expected_precision
    assert round(recall, 4) == expected_recall
    assert round(fbeta, 4) == expected_fbeta
