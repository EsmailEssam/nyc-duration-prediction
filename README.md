# Taxi Trip Duration Prediction
This project aims to deploy a simple machine learning model using Flask, and containerize the application using Docker to deploy it on Render Web Service. The machine learning model predicts the duration of a taxi trip based on the Taxi & Limousine Commission Trip Record Data.


## Introduction
This project demonstrates a complete workflow for deploying a machine learning model as a web application. It uses Flask for the web framework and Docker for containerization. The model predicts taxi trip duration using historical trip data.

## Dataset
The dataset used in this project is the Taxi & Limousine Commission Trip Record Data. This dataset contains information about individual trips, including pickup and dropoff locations, times, passenger counts, and more.

## Model
The machine learning model is trained to predict the duration of a taxi trip based on features extracted from the trip record data. The key features used in the model include:
- Passenger Count
- Pick-Up Location
- Drop-Off Location
- Trip Distance
- Total Amount

## Installation
To get started with the project, follow these steps:

1. Clone the repository:
```sh
git clone https://github.com/EsmailEssam/nyc-duration-prediction.git
cd nyc-duration-prediction
```
2. Set up a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
```
3. Install the required packages:
```sh
pip install -r requirements.txt
```

## Usage
1. Start the Flask application:
```sh
flask run
```
2. Use the web interface to input trip details and get the predicted trip duration.

## Deployment
### Docker
1. Build the Docker image:
```sh
docker build -t duration-prediction .
```
2. Run the Docker container:
```sh
docker run -p 5000:5000 duration-prediction
```
### Render Web Service
1. Push the Docker image to a container registry (e.g., Docker Hub).

2. Follow Render's documentation to deploy a Docker-based web service:
  - Create a new web service on Render.
  - Use the Docker image from your container registry.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to create a pull request or open an issue.
