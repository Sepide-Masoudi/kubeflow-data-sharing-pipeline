# Import necessary libraries
import pandas as pd
from flask import Flask, jsonify
import os

# Create a Flask app
app = Flask(__name__)


# Define a route to read CSV and return JSON
@app.route('/read_csv', methods=['GET'])
def read_csv():
    # Specify the path to the CSV file
    csv_file_path = 'sample-new.csv'  # Replace with your actual CSV file path

    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        return jsonify({"error": "File not found"}), 404

    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Convert the DataFrame to a JSON response
    return jsonify(df.to_dict(orient='records'))


# Run the app (make sure to set debug=False in production)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)  # Listen on all interfaces
