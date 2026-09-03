# Heart Disease Prediction API

A machine learning-based REST API for predicting the presence of heart disease using FastAPI and a trained machine learning model.

## Project Overview

This project provides a Heart Disease Prediction API built with **FastAPI**. A trained machine learning model is used to predict whether a patient is likely to have heart disease based on input health-related features.

The application is containerized using **Docker** and can be deployed as a web service on **Render**.

## Technologies Used

* Python
* FastAPI
* Scikit-learn
* Joblib
* Pydantic
* Uvicorn
* Docker
* Render

## Project Structure

```text
heart-disease-api/
│
├── app/
│   ├── main.py
│   └── schemas.py
│
├── model/
│   └── heart_model.joblib
│
├── heart.csv
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## API Endpoints

### GET `/`

Returns a simple message to confirm that the API is running.

### POST `/predict`

Accepts patient information and returns a heart disease prediction.

## Running Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the FastAPI application:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at:

```text
http://localhost:8000
```

FastAPI interactive documentation:

```text
http://localhost:8000/docs
```

## Running with Docker

Build the Docker image:

```bash
docker build -t heart-disease-api .
```

Run the container:

```bash
docker run -p 8000:8000 heart-disease-api
```

The API can then be accessed at:

```text
http://localhost:8000
```

## Docker Compose

The application can also be started using:

```bash
docker-compose up --build
```

## Deployment

The project can be deployed on **Render** using a Docker Web Service.

Deployment steps:

1. Push the project to GitHub.
2. Create a new Web Service on Render.
3. Connect the GitHub repository.
4. Select Docker as the environment.
5. Use the repository root as the build context.
6. Deploy the service.
7. Test the deployed API using the `/docs` endpoint or API requests.

## Live Deployment

The API is deployed on Render and is publicly accessible.

**Live API:**  
https://heart-disease-api-t9v7.onrender.com

**Interactive API Documentation:**  
https://heart-disease-api-t9v7.onrender.com/docs

## Model

The trained machine learning model is stored in:

```text
model/heart_model.joblib
```

The model is loaded by the FastAPI application and used to generate predictions from user-provided input data.

## Testing

The API can be tested using:

* FastAPI Swagger UI
* Postman
* cURL

Interactive API documentation is available through:

```text
/docs
```

## Author

Heart Disease Prediction API — Machine Learning Deployment Project
