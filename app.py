from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Please set GEMINI_API_KEY in .env file")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
# Use gemini-1.5-flash if available, else fallback to gemini-pro
try:
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception:
    model = genai.GenerativeModel("gemini-pro")


# Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get("message", "")
        if not user_message:
            return jsonify({"reply": "Please type a message."})
        
        prompt = f"""
        You are a friendly, structured chatbot. 
        Answer clearly and conversationally but return information-rich responses.
        User: {user_message}
        """

        response = model.generate_content(prompt)
        ai_reply = response.text.strip() if response and response.text else "No response."

        return jsonify({"reply": ai_reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
