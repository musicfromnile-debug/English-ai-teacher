from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
import os

app = Flask(__name__)
CORS(app)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

@app.route("/")
def home():
    return "✅ English AI Teacher API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    if not message:
        return jsonify({"reply": "Please type something."})
    
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=f"You are an English teacher. Help the student learn English and IELTS: {message}"
    )
    
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
