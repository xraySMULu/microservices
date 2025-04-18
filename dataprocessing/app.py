
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json
    # Example processing: calculate the sum of numbers in the data
    result = sum(data.get('numbers', []))
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

# This is a simple Flask application that processes data sent to it via a POST request.
# It expects a JSON payload with a list of numbers and returns the sum of those numbers.
# To run the application, use the command: python dataprocessing/app.py
# Ensure you have Flask installed in your environment. You can install it using pip:
# pip install Flask
# To test the application, you can use a tool like Postman or curl to send a POST request with a JSON body.
# POSTMAN
# 1. Open Postman and create a new POST request.
# 2. Set the URL to http://localhost:5000/process.
# 3. In the Body tab, select raw and choose JSON from the dropdown.
# 4. Enter the JSON payload:
# {"numbers": [1, 2, 3, 4, 5]}
# 5. Click Send.  
# 6. You should see the response with the result:
# {
#     "result": 15
# }
# CURL
# 1. Open your terminal.
# 2. Use the following command to send a POST request:
# curl -X POST http://localhost:5000/process -H "Content-Type: application/json" -d '{"numbers": [1, 2, 3, 4, 5]}'
# 3. You should see the response with the result:
# {
#     "result": 15
# }







