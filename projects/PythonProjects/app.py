from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <form method='POST' action='/chat'>
        <input name='question'>
        <button>Send</button>
    </form>
    """

@app.route("/chat", methods=["POST"])
def chat():
    question = request.form["question"]

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen3:8b",
            "prompt": question,
            "stream": False
        }
    )

    return response.json()["response"]

app.run(debug=True)