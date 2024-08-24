from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/capitalize', methods=['POST'])
def capitalize_string():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    capitalized_text = text.upper()
    return jsonify({'capitalized_text': capitalized_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=True)