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
    # add description for the second test
    """
    # Your code here
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
