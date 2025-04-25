# Deploying a Scalable ML Pipeline with FastAPI

This project demonstrates the deployment of a machine learning model as a production-ready API using FastAPI. The application accepts structured user input via POST requests, performs preprocessing, inference with a trained model, and returns a prediction.

This project was built as part of a Udacity course. The base architecture and starter code were provided. The implementation of key features—including data cleaning, model inference logic, API endpoints, and performance slicing—was completed by **Darion Pride**.

---

## Features

- FastAPI for scalable, high-performance inference
- Logistic Regression model predicting binary income classification
- RESTful endpoints for inference and health checks
- Data preprocessing with one-hot encoding
- Unit tests for model and API
- Model performance reporting on feature "slices"
- CI/CD setup with GitHub Actions
- Version-controlled data and models using DVC

## Project Structure

This project is organized into logical folders for model development, deployment, and testing.

- `ml/`: Machine learning logic including data loading, model training, inference, and performance slicing
- `main.py`: FastAPI application entry point
- `test_main.py`: Unit tests for the API
- `data/`: Raw census data (tracked via DVC)
- `model_card.md`: Full model transparency and evaluation documentation
- `requirements.txt`: Python dependency list
- `environment.yml`: Conda environment configuration
- `.github/workflows/`: GitHub Actions CI/CD configuration

## Model Card

### Model Details

- **Name:** US Census Income Prediction Model (v1.0)
- **Type:** Binary Classification
- **Architecture:** Logistic Regression
- **Created by:** Darion Pride
- **Date Created:** 2/4/2025

### Intended Use

This model predicts whether a U.S. citizen earns more than $50,000 annually, based on demographic and employment attributes. It's designed for use cases such as financial planning, targeted marketing, and basic income segmentation.

### Training Data

- **Source:** U.S. Census dataset
- **Processing:** One-hot encoding for categorical variables, label binarization for the target
- **Categorical Features:** workclass, marital-status, education, occupation, relationship, race, sex

### Evaluation Data

- The dataset was split using an 80/20 training/testing ratio.
- Identical preprocessing was applied to both splits.

### Performance Metrics

- **Precision:** 0.7872  
- **Recall:** 0.1965  
- **F1 Score:** 0.3145  

These metrics provide a balanced view of the model’s ability to correctly identify individuals earning over $50,000.

### Ethical Considerations

- **Transparency:** Logistic regression allows for interpretable outputs and insights into feature influence.
- **Privacy:** No personally identifiable information was used. All data was anonymized and publicly available.
- **Fairness:** The model may reflect biases in the source data. Regular audits and retraining are recommended to mitigate systemic bias.

### Caveats and Recommendations

- The low recall suggests the model may miss many true high-income individuals.
- Future work should focus on addressing data bias, exploring alternate models, and improving recall without sacrificing interpretability.

## Tools and Technologies

- Python
- FastAPI
- scikit-learn
- pandas
- Pydantic
- DVC
- GitHub Actions
- pytest
- Uvicorn

## Contributions

This project was completed as part of a Udacity course.  
All implementation of the following was completed by Darion Pride:
- Model training logic and pipeline integration
- Inference and API endpoint logic
- Test scripts
- Model card documentation
- Project structure cleanup and GitHub integration

## License

This project is licensed under the MIT License.
