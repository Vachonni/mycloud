from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capitalize', methods=['POST'])
def capitalize_string():
    if request.is_json:
        data = request.get_json()
        if 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
        text = data['text']
    else:
        text = request.form['text']
    
    capitalized_text = text.upper()
    
    if request.is_json:
        return jsonify({'capitalized_text': capitalized_text})
    else:
        return render_template('index.html', capitalized_text=capitalized_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=True)