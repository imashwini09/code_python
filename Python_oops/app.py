from flask import Flask, request, jsonify
import requests
import pandas as pd
import json
import os

app = Flask(__name__)

# URL of the API endpoint
api_url = 'https://example.com/api/endpoint'

@app.route('/')
def index():
    return '''
    <!doctype html>
    <title>Upload JSON File</title>
    <h1>Upload JSON File</h1>
    <form action="/upload" method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        # Save the uploaded file
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        # Process the JSON file
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Extract static data
        static_data = {
            'id': data['id'],
            'channel': data['channel']
        }

        responses = []

        # Extract dynamic data and make API requests
        dynamic_data = {
            'dynamicData1': data['dynamicData1'],
            'dynamicData2': data['dynamicData2']
        }

        # Combine static and dynamic data
        request_data = {**static_data, **dynamic_data}

        # Make the API request
        response = requests.post(api_url, json=request_data)
        
        responses.append({
            'id': data['id'],
            'status_code': response.status_code,
            'response_text': response.text
        })

        return jsonify(responses)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
