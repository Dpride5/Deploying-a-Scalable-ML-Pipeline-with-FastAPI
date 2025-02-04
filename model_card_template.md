# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Name: US Census Income Prediction Model Version 1.0
Type: Binary Classification
Model Architecture: Logistic Regression
Created by: Darion Pride
Date Created: 2/4/2025

## Intended Use
The US Census Income Prediction Model is intended to predict if a US citizen's income surpasses $50,0000 dollars per year. This will be based on demographic and employmeny-related details. The model is designed for use in situations where income prediction is used in decision-making such as financial planning, target marketing as well as many other use cases.

## Training Data
The dataset used comes from the US Census.

Data Processing: The training data was preprocessed with one-hot encoding of categorical features and label binarization. The categorical features used include workclass, marital-status, education, occupation, relationship, race, and sex.

## Evaluation Data
Evaluation Dataset: Test Census Income dataset
This dataset was split for one portion to be used for testing and the other portion used for training. This is a 20:80 split respectively. Testing taking 20% and training taking the other 80% of the dataset. The exact same process was used on the evaluation dataset as with the training data set, which includes one-hot encoding of categorical features and label binarization.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
This model's performance was evaluated on three metrics that highlight a balanced insight into machine learning effectiveness. Precision measures the accuracy of positive predictions, while Recall evaluates the model's ability to capture all true positive instances, reducing false negatives. The F1-Score harmonizes these two metrics, providing a holistic measure of performance. 

Model's Performance: Precision: 0.7872 | Recall: 0.1965 | F1: 0.3145

## Ethical Considerations
Transparency: The model uses Logistic Regression, which is a transparent and interpretable model. Users can see and understand the factors that contribute to predictions.

Privacy: The model uses personal data for prediction. This has been cleared because all personal data has been anonymized and publicly available.

Fairness/Bias: The model may exhibit bias if the training data contains biases in its attributes. 

## Caveats and Recommendations
The model's low recall suggests it struggles to identify a significant portion of individuals earning over $50,000 annually. To improve fairness and accuracy, address potential biases in training data, update the model regularly to reflect evolving societal and economic trends, and implement ongoing performance monitoring to get more reliable outcomes.