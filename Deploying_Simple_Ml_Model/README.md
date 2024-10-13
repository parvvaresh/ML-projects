# Deploying a Simple Machine Learning Model

This project demonstrates how to deploy a simple machine learning model using Python. The repository includes a pre-processing step, a model for making predictions, and instructions for running the project within a Docker container.

## Project Structure

- **`app.py`**: The main script that runs the machine learning model prediction. It loads a text input, pre-processes it, transforms the text using a TF-IDF vectorizer, and makes a prediction using the trained model.
- **`Dockerfile`**: The Docker configuration file used to create a containerized environment for the application.
- **`requirements.txt`**: A list of Python dependencies required to run the application.
- **`model/`**: This directory contains the trained machine learning model (`model.pkl`) and the TF-IDF vectorizer (`tfidf_vectorizer.pkl`) that are loaded during prediction.

## How to Run the Project

### Prerequisites

Ensure that you have the following installed on your machine:

- Python 3.x
- Docker (if you wish to run the project inside a container)

### Running the Application Locally

1. **Install dependencies**:
   First, you need to install the required Python libraries. You can do this by running:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   You can run the main `app.py` file to execute a test prediction using a sample text.

   ```bash
   python app.py
   ```

   The script will load the pre-trained model and vectorizer from the `model/` directory and print the predicted class for the given text.

### Running with Docker

1. **Build the Docker Image**:
   To run the application inside a Docker container, first build the Docker image:

   ```bash
   docker build -t ml_model_app .
   ```

2. **Run the Docker Container**:
   Once the image is built, you can run the application inside a Docker container:

   ```bash
   docker run ml_model_app
   ```

## Model Details

- The model is stored in the `model.pkl` file inside the `model/` directory.
- The TF-IDF vectorizer used for transforming text inputs is stored in the `tfidf_vectorizer.pkl` file.
- The model is trained to classify text input after pre-processing and transformation.

## Pre-Processing

The `pre_process` function (imported from the `model/pre_process.py` file) is responsible for cleaning and preparing the input text before it is transformed into a vector by the TF-IDF vectorizer.
