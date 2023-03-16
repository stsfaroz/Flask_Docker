# Article 
[ML model Containerization using Docker and Flask](https://salmanfaroz.medium.com/ml-model-containerization-using-docker-and-flask-b09adf780bd3)

check the above article for better understanding

# Building an ML Model with Flask and Docker

This repository contains an example of building a Machine Learning (ML) model using Flask and Docker.

## Prerequisites

To run this application, you need to have the following software installed on your system:
- Python 3.5+
- Docker

You can install the required Python libraries by running the following command in your terminal:

```
pip install -r requirements.txt

```


## Building the Docker Image

To build the Docker image, navigate to the root directory of the project in your terminal and run the following command:

```
docker build -t mlapp:v1 .

```

This command builds a Docker image with the tag "mlapp" and version "v1" using the Dockerfile in the current directory. The "." at the end of the command indicates the current directory.

## Running the Docker Image

To run the Docker image, run the following command in your terminal:

```
docker run -p 8080:8080 mlapp:v1
```

This command runs the Docker image with the tag "mlapp" and version "v1" and maps port 8080 in the container to port 8080 on your local machine. You can access the application by navigating to http://localhost:8080/ in your web browser.

## Testing the Application

To test the application, run the following command in your terminal:

```
python test.py

```


This command runs a Python script that sends a test request to the application and prints the response.


