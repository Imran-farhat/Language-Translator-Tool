from flask import Flask, request, jsonify, render_template
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renders the frontend

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get("text", "")
    target_lang = data.get("targetLang", "")

    if not text or not target_lang:
        return jsonify({"error": "Missing text or target language"}), 400

    try:
        # Translate using deep-translator
        translated_text = GoogleTranslator(target=target_lang).translate(text)
        return jsonify({"translation": translated_text})
    except Exception as e:
        return jsonify({"error": f"Translation error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
