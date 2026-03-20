from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Flask app running on Vercel 🚀"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    return jsonify({
        "received_data": data,
        "prediction": "demo_result"
    })

# Vercel expects this variable
handler = app