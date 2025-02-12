from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    # Récupérer les paramètres de l'URL
    search_query = request.args.get('q', default='reussite')  # Valeur par défaut : 'reussite'
    search_type = request.args.get('searchType', default='image')  # Valeur par défaut : 'image'
    dateRestriction = request.args.get('dateRestrict', default='2025-02-11:2025-02-12')  # Valeur par défaut
    language = request.args.get('lr', default='lang_en')  # Valeur par défaut : 'lang_en'
    location = request.args.get('gl', default='FR')  # Valeur par défaut : 'FR'

    # Vos informations d'API Google
    api_key = os.getenv('API_KEY')
    api_id = os.getenv('SEARCH_ENGINE_ID')

    # URL de l'API Google Custom Search
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_query,
        'key': api_key,
        'cx': api_id,
        'searchType': search_type,
        'dateRestrict': dateRestriction,
        'lr': language,
        'gl': location
    }

    # Faire la requête à l'API Google
    response = requests.get(url, params=params)
    results = response.json().get('items', [])  # Gérer le cas où 'items' n'existe pas

    # Extraire les liens des résultats
    links = [item['link'] for item in results]
    return jsonify(links)

if __name__ == '__main__':
    app.run(debug=True)