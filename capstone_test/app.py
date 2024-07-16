from flask import Flask, request, jsonify
import http.client
import json

app = Flask(__name__)

def ask_question(query):
    conn = http.client.HTTPSConnection("chatgpt-gpt4-ai-chatbot.p.rapidapi.com")
    payload = json.dumps({"query": query})
    headers = {
        'x-rapidapi-key': "24151f6615mshc6617e1401be309p1201d5jsn032cd299a78f",
        'x-rapidapi-host': "chatgpt-gpt4-ai-chatbot.p.rapidapi.com",
        'Content-Type': "application/json"
    }
    conn.request("POST", "/ask", payload, headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    return data.decode("utf-8")

@app.route('/')
def home():
    return "Welcome to the Chatbot API"

@app.route('/ask', methods=['POST'])
def ask():
    query = request.json.get('query')
    response = ask_question(query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
