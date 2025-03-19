from flask import Flask, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Define chatbot patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]),
    (r"how are you?", ["I'm good, thanks!", "Doing well, how about you?"]),
    (r"what is your name?", ["I'm a chatbot.", "Call me ChatBot!"]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Take care!"]),
]

chatbot = Chat(pairs, reflections)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")
        response = chatbot.respond(user_input)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Starting chatbot... Visit: http://127.0.0.1:5000/chat")
    app.run(debug=True, port=5000)
