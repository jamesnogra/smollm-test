from flask import Flask, jsonify, render_template, request
from model import generate_response

app = Flask(__name__)
PORT = 5001

# API endpoint
@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.get_json()
    prompt = data.get('prompt', '')
    print(f'PROMPT: {prompt}')
    if len(prompt) == 0:
        return jsonify({'response': 'Please provide a question!'})
    response = generate_response(prompt)
    return jsonify({'response': response})

# HTML file serving
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=PORT)