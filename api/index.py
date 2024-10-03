from flask import Flask, request, jsonify
from g4f.client import Client

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        
        client = Client()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}],
        )
        
        assistant_message = response.choices[0].message.content
        return jsonify({"response": assistant_message}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
