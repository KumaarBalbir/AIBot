from flask import Flask, request, jsonify
from flask_cors import CORS
from inference import Query

app = Flask(__name__)
CORS(app)  # Allow all origins to access the API

# Define a route for handling chatbot requests


@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_text = request.get_json()  # Get data from the frontend

    # Process the data and generate a response

    # debug_response = {"message": "This is a response from the Flask backend."}

    # Process the user_text using the Query function
    response = Query(str(user_text))
    # print(f"\n\n printing backend response...\n\n{response}")

    return jsonify({"message": response})


if __name__ == '__main__':
    app.run(debug=True)
