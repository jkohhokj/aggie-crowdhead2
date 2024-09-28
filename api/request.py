import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = "https://example.com"  # Replace with the target URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data, for example, all paragraphs
    data = [p.text for p in soup.find_all('p')]
    return jsonify(data)

if __name__ == '__main__':
    app.run()