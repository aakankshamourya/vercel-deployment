from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Working on Vercel 🚀"})

# THIS IS REQUIRED
def handler(request):
    return app(request.environ, lambda status, headers: None)