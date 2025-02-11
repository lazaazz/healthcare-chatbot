from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load disease data
with open("disease_data.json", "r") as f:
    disease_db = json.load(f)

@app.route('/chat', methods=['POST'])
def chatbot():
    user_query = request.json.get("query", "").lower()
    for disease, details in disease_db.items():
        if disease.lower() in user_query:
            return jsonify(details)
    return jsonify({"response": "I don't have information on that disease."})

if __name__ == '__main__':
    app.run(debug=True)
