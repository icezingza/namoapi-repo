from flask import Flask, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

# สร้าง client ผูกกับ Project ของพี่
client = genai.Client(
    vertexai=True,
    project="namo-legacy-identity",  # <<== เปลี่ยนเป็น Project ID ของพี่
    location="global"
)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    response = client.models.generate_content(
        model="gpt-4o-mini",  # หรือเปลี่ยนเป็น gpt-4o ได้
        contents=user_input
    )

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)