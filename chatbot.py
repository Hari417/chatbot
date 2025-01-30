from flask import Flask, render_template, request, jsonify
import ollama
import re  # Import regex module

app = Flask(__name__)

def chat_with_model(user_input):
    context_history = [
        {
            "role": "system",
            "content": "You are an AI chatbot specialized in answering questions. Provide clear, concise, and direct responses without unnecessary details. If unsure, politely state that you don't have the information."
        },
        {"role": "user", "content": user_input}
    ]
    
    response = ""
    stream = ollama.chat(
        model="deepseek-r1:14b",
        messages=context_history,
        stream=True
    )
    
    for chunk in stream:
        if "message" in chunk and "content" in chunk["message"]:
            response += chunk["message"]["content"]

    # Remove everything inside <think>...</think> including the tags
    response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL)

    return response.strip()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' in request body"}), 400
    
    user_message = data["message"]
    bot_response = chat_with_model(user_message)
    
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
