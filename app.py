from flask import Flask, render_template, request, jsonify # type: ignore
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  # Render the main HTML page

@app.route('/count_words_and_characters', methods=['POST'])
def count_words_and_characters():
    text = request.json['text']  # Get the text from the JSON request
    word_count = len(text.split())  # Count the number of words
    char_count = len(text)  # Count the number of characters

    # Simulating a delay for the loading animation
    time.sleep(3)

    # Return the counts as JSON
    return jsonify({'word_count': word_count, 'char_count': char_count})

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
