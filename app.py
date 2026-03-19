from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from langchain_ollama import OllamaLLM

app = Flask(__name__)
CORS(app)

# Initialize the LLM exactly as done in your existing chatbot.py
llm = OllamaLLM(model="llama3")
conversation = ""

# -------------------------------------------------------------
# Integrated Chatbot Function
# This uses the same conversational logic as in your chatbot.py
# -------------------------------------------------------------
def get_response(message):
    global conversation
    # 2. Match the conversation format of chatbot.py
    conversation += f"User: {message}\nBot: "
    
    # 2. Use the existing chatbot function logic to generate response
    response = llm.invoke(conversation)
    
    if response:
        response = response.strip()
        conversation += f"{response}\n"
    
    return response

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # 1. Debug the Flask /chat endpoint: correctly receive JSON input safely
        data = request.get_json(silent=True) or {}
        
        # 1. Extract the message safely
        user_message = data.get('message', '')
        
        # 6. Fix Common Issues: Handle empty input
        if not user_message or user_message.strip() == "":
            print("Debug: Handled empty input.")
            return jsonify({"response": "Error: Empty message received."})
            
        user_message = user_message.strip()
        
        # 5. Logging: Print incoming user message in console
        print(f"User: {user_message}")
        
        # 3. Error Handling: Wrap chatbot call in try-except
        try:
            bot_reply = get_response(user_message)
            
            # 6. Fix Common Issues: Handle None responses
            if bot_reply is None:
                print("Debug: Chatbot logic returned None.")
                # 4. Response Format: Always return valid JSON
                return jsonify({"response": "Error: Bot returned a None response."})
                
            # 4. Response Format: Always return valid JSON
            return jsonify({"response": bot_reply})
            
        except Exception as e:
            error_message = str(e)
            
            # 5. Logging: Print errors in console for debugging
            print(f"Chatbot logic error: {error_message}")
            
            # 3. Error Handling: If error occurs, return {"response": "Error: <actual error message>"}
            return jsonify({"response": f"Error: {error_message}"})
            
    except Exception as e:
        error_message = str(e)
        
        # 5. Logging: Print errors in console for debugging
        print(f"Flask server error: {error_message}")
        
        # 6. Fix Common Issues: Ensure Flask does not crash
        return jsonify({"response": f"Error: {error_message}"})

if __name__ == '__main__':
    print("Starting Flask Backend...")
    app.run(debug=True, port=5000)
