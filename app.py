import requests
from bs4 import BeautifulSoup
from collections import Counter
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/word-frequency', methods=['POST'])
def get_word_frequency():
    url = request.json.get('url')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    words = [word.lower() for word in text.split() if word.isalpha()]
    word_counts = dict(Counter(words))
    result = json.dumps(word_counts, indent=2)
    return result, 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)
