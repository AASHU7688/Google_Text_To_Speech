from flask import Flask, render_template, request
from gtts import gTTS
import os

app = Flask(__name__)

# Ensure the static directory exists
if not os.path.exists("static"):
    os.makedirs("static")

# Supported languages in gTTS
LANGUAGES = {
    "af": "Afrikaans", "ar": "Arabic", "bn": "Bengali", "zh": "Chinese", "cs": "Czech", "da": "Danish", "nl": "Dutch",
    "en": "English", "fi": "Finnish", "fr": "French", "de": "German", "el": "Greek", "hi": "Hindi", "hu": "Hungarian",
    "id": "Indonesian", "it": "Italian", "ja": "Japanese", "kn": "Kannada", "ko": "Korean", "ml": "Malayalam", "mr": "Marathi",
    "ne": "Nepali", "no": "Norwegian", "pl": "Polish", "pt": "Portuguese", "pa": "Punjabi", "ru": "Russian", "es": "Spanish",
    "sv": "Swedish", "ta": "Tamil", "te": "Telugu", "th": "Thai", "tr": "Turkish", "ur": "Urdu", "vi": "Vietnamese"
}

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES,)

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']
    language = request.form['language']
    
    tts = gTTS(text=text, lang=language, slow=False)
    
    filename = "static/output.mp3"
    tts.save(filename)
    
    return render_template('index.html', audio_file=filename, languages=LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)
