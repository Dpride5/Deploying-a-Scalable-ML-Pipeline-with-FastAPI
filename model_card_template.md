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
This model's performance was evaluated on three metrics that highlight a balanced insight in machine learning 

## Ethical Considerations

## Caveats and Recommendations
