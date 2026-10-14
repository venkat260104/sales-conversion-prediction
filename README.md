# Sales Conversion Prediction Using Machine Learning

## Project Overview

Sales Conversion Prediction is a machine learning web application that predicts the likelihood of a website visitor making a purchase based on their browsing behavior and session information.

The project uses a **Random Forest Classifier** trained on the Online Shoppers Purchasing Intention dataset. A FastAPI backend serves the model, and an interactive web dashboard allows users to explore predictions.

## Objectives

- Predict whether a website visitor is likely to make a purchase.
- Analyze visitor browsing behavior and session characteristics.
- Demonstrate how machine learning can support data-driven marketing decisions.
- Build and serve a trained ML model through a web application.

## Features

- Machine learning-based purchase prediction.
- Random Forest classification model.
- FastAPI backend for serving the application.
- Interactive web dashboard using HTML, CSS, and JavaScript.
- Prediction threshold configurable through the saved model artifact.
- Model information endpoint for viewing required features and threshold.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data handling and preprocessing |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning model |
| Random Forest | Classification algorithm |
| FastAPI | Backend API |
| Uvicorn | Application server |
| Joblib | Saving and loading the trained model |
| HTML, CSS, JavaScript | Web dashboard |
| Git and GitHub | Version control and project hosting |

## Dataset

**Online Shoppers Purchasing Intention Dataset**

The dataset contains website visitor session information, including browsing activity, page duration, visitor type, traffic source, and weekend activity.

- **Target variable:** `Revenue`
- **Task:** Binary classification
- `True` indicates a purchase session.
- `False` indicates a session without a purchase.

The model uses selected session features to estimate purchase likelihood.

## Project Structure

```text
sales-conversion-prediction/
├── main.py
├── sales_conversion_model.pkl
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/venkat260104/sales-conversion-prediction.git
cd sales-conversion-prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

Open the API documentation at:

http://127.0.0.1:8000/docs

Open the web dashboard at:

http://127.0.0.1:8000/dashboard

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Check application status |
| `/model-info` | GET | View model details and required features |
| `/dashboard` | GET | Open the web dashboard |
| `/docs` | GET | Explore the API using Swagger UI |

## Model Information

- **Algorithm:** Random Forest Classifier
- **Problem type:** Binary classification
- **Prediction threshold:** 0.30
- **Model artifact:** `sales_conversion_model.pkl`

The model's estimated purchase probability is compared with the configured threshold to classify a session as a likely conversion or a non-conversion.

## Potential Applications

- Identifying visitors who may be likely to purchase.
- Supporting targeted marketing campaigns.
- Understanding visitor browsing patterns.
- Helping e-commerce teams prioritize engagement strategies.

## Future Improvements

- Deploy the application to a cloud hosting platform.
- Add interactive prediction visualizations.
- Improve model performance through feature engineering and hyperparameter tuning.
- Add model evaluation metrics and explainability.
- Integrate prediction history and analytics.

## Limitations

Predictions are estimates based on patterns learned from historical data. They do not guarantee that a visitor will make a purchase. Model performance may vary across websites, customer groups, and real-world conditions.

## Author

**Peddinti Venkata Naveen**

Machine Learning | Python | FastAPI | Data Science

GitHub: https://github.com/venkat260104

---

*This project was developed for learning and demonstrating the practical application of machine learning in e-commerce analytics.*
