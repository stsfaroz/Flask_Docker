# Import the Flask module
from flask import Flask, request
import numpy as np
import pickle

# Load the random forest model
with open('random_forest_IrisModel.pickle', 'rb') as f:
    loaded_model = pickle.load(f)

# Create the Flask application
app = Flask(__name__)

# Define the predict endpoint
@app.route("/predict", methods=["POST"])
def predict():
    # Get the input data as a dictionary
    input_data = request.get_json()

    # Convert the input data into a numpy array
    input_array = np.array(list(input_data.values())).reshape(1, -1)

    # Make the prediction using the loaded model
    prediction = loaded_model.predict(input_array)

    # Return the prediction as a JSON response
    return {"prediction": prediction.tolist()}

if __name__ == "__main__":
    # Start the Flask application
    app.run(host='0.0.0.0', port=8080)
