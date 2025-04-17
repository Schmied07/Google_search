from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    # Récupérer les paramètres
    search_query = request.args.get('q', default='chien')
    search_type = request.args.get('type', default='web')
    file_type = request.args.get('filetype', default=None)
    date_restrict = request.args.get('dateRestrict', default=None)
    language = request.args.get('lr', default='lang_en')
    location = request.args.get('gl', default='FR')

    # Clés API
    api_key = os.getenv('API_KEY')
    api_id = os.getenv('SEARCH_ENGINE_ID')

    # URL de l'API
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_query,
        'key': api_key,
        'cx': api_id,
        'lr': language,
        'gl': location,
        'num': 5  # Récupère plusieurs résultats pour pouvoir filtrer
    }

    # Gérer les types de recherche
    if search_type == 'image':
        params['searchType'] = 'image'
        if file_type:
            params['fileType'] = file_type
    elif search_type == 'video':
        params['q'] += ' video'
    elif search_type == 'pdf':
        params['fileType'] = 'pdf'
    elif search_type == 'docx':
        params['fileType'] = 'docx'

    if date_restrict:
        params['dateRestrict'] = date_restrict

    # Requête à l'API Google
    response = requests.get(url, params=params)
    results = response.json().get('items', [])

    image_link = None

    # 1. Chercher une image en .webp sans "encrypted" dans l'URL
    for item in results:
        link = item.get('link', '')
        if 'encrypted' not in link and link.endswith('.webp'):
            image_link = link
            break

    # 2. Sinon, chercher une autre image sans "encrypted"
    if not image_link:
        for item in results:
            link = item.get('link', '')
            if 'encrypted' not in link:
                image_link = link
                break

    # 3. Fallback : première image disponible
    if not image_link and results:
        image_link = results[0].get('link')

    return jsonify({'image': image_link})

if __name__ == '__main__':
    app.run(debug=True)
