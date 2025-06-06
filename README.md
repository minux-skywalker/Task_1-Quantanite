# FastAPI Model Prediction App

This project implements a FastAPI application that serves a pre-trained machine learning model and exposes a `/predict` endpoint. The endpoint takes a JSON payload with input features and returns the model's prediction.

## Features

- FastAPI-powered REST API.
- Endpoint for making predictions using a pre-trained model.
- Simple POST request to fetch predictions.

## Setup Instructions

### 1. Clone the repository
Clone the repository to your local machine:

```bash
git clone <your-repository-url>
cd <your-repository-directory>

python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt

http://localhost:8000/docs

{
  "feature1": 1.5,
  "feature2": 2.5
}
