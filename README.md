# Expense Prediction Web Application (AWS Deployment)

## Project Overview

This project is a **Machine Learning web application** that predicts a person's **expense based on Income and Age**.
The model is developed using **Scikit-learn (Linear Regression)** and deployed as a **Flask web application**.
The application is hosted on an **AWS EC2 instance** and served using **Gunicorn**, enabling real-time predictions through a web interface.

---

## Features

* Predicts expenses based on **Income and Age**
* Simple and interactive **web interface**
* Machine learning model trained using **Scikit-learn**
* Web application built with **Flask**
* Deployed on **AWS EC2 cloud infrastructure**
* Production-ready serving using **Gunicorn**

---

## Tech Stack

* **Python**
* **Flask**
* **Scikit-learn**
* **Gunicorn**
* **HTML / CSS**
* **AWS EC2**
* **Git & GitHub**

---

## Project Structure

```
expense_prediction_project/
│
├── app.py                 # Flask application
├── train_model.py         # Model training script
├── model.pkl              # Saved machine learning model
├── requirements.txt       # Project dependencies
│
├── templates/
│     └── index.html       # Web interface
│
└── static/
      └── style.css        # Styling
```

---

## How It Works

1. User enters **Income and Age** on the web interface.
2. The request is sent to the **Flask backend**.
3. Flask loads the **trained ML model** (`model.pkl`).
4. The model predicts the **expected expense**.
5. The result is returned and displayed to the user.

---

## Deployment Architecture

```
User Browser
     ↓
AWS EC2 Instance
     ↓
Gunicorn Server
     ↓
Flask Application
     ↓
Machine Learning Model
```

The application is accessible through the **public EC2 IP address**.

---

## Author

**Alka Singh**
Data Scientist | Machine Learning Engineer | Generative AI & NLP Enthusiast | AWS Cloud & ML Deployment | Python | Statistical Modeling
