# app.py
from flask import Flask, render_template, request
import requests
from flask_cors import CORS


app = Flask(__name__, template_folder='templates')

# News API URL with your API key
news_api_url = "https://newsapi.org/v2/everything"
api_key = "e8f1f37b77654c70b5590e4ad93d24cc"

def is_fake_news(verification_text, articles):
    # Check if the verification text is present in any part of the news articles
    for article in articles:
        if verification_text.lower() in article['title'].lower() or verification_text.lower() in article['description'].lower():
            return True
    return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify_text():
    verification_text = request.form.get('verification_text')

    # Fetch news articles from the API with the entered content as keywords
    params = {
        'apiKey': api_key,
        'q': verification_text,
        'sortBy': 'publishedAt',
        'pageSize': 100  # Adjust as needed
    }

    response = requests.get(news_api_url, params=params)
    data = response.json()

    # Extract articles from the response
    articles = data.get('articles', [])

    # Check if the verification text is present in any part of the news articles
    if is_fake_news(verification_text, articles):
        result = "Real News: The news is genuine ."
    else:
        result = "Fake News: The news is not genuine."

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

CORS(app)
