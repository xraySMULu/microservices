
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
