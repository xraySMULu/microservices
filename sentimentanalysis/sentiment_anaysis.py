from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text', '')
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return jsonify({
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity
    })

if __name__ == '__main__':
    app.run(debug=True)


# This is a simple Flask application for sentiment analysis sent via a POST request.
# It expects a JSON payload with a list of numbers and returns the sum of those numbers.
# To run the application, use the command: python sentimentanalysis/sentiment_analysis.py
# Ensure you have Flask installed in your environment. You can install it using pip:
# pip install Flask
# To test the application, you can use a tool like Postman or curl to send a POST request with a JSON body.
# POSTMAN
# 1. Open Postman and create a new POST request.
# 2. Set the URL to http://localhost:5000/process.
# 3. In the headers, set Content-Type to application/json.
# 3. In the Body tab, select raw and choose JSON from the dropdown.
# 4. Enter the JSON payload:
# {"text": "I love programming!"} 
# 5. Click Send.  
# 6. You should see the response with the result:
# {
#    "polarity": 0.625,
#    "subjectivity": 0.6
#}
# CURL
# 1. Open your terminal.
# 2. Use the following command to send a POST request:
# curl -X POST -H "Content-Type: application/json" -d '{"text": "I love programming!"}' http://127.0.0.1:5000/analyze
# 3. You should see the response with the result:
# {
#     "result": 15
# }







