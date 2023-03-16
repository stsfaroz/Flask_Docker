import requests
import json

# Define the input data
input_data = {
    "feature1": 1,
    "feature2": 2,
    "feature3": 3,
    "feature4": 4
}

# Define the URL of the predict endpoint
url = "http://localhost:8080/predict"

# Send a POST request to the predict endpoint with the input data
response = requests.post(url, json=input_data)

# Print the response
print(response.json())

## output 
## {'prediction': ['Iris-virginica']}