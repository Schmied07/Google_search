from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    # Récupérer les paramètres de l'URL
    search_query = request.args.get('q', default='chien')
    search_type = request.args.get('type', default='web')  # Par défaut, recherche sur le web
    file_type = request.args.get('filetype', default=None)  # Pour PDF, DOCX, etc.
    date_restrict = request.args.get('dateRestrict', default=None)
    language = request.args.get('lr', default='lang_en')
    location = request.args.get('gl', default='FR')

    # Vos informations d'API Google
    api_key = os.getenv('API_KEY')
    api_id = os.getenv('SEARCH_ENGINE_ID')

    # URL de l'API Google Custom Search
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_query,
        'key': api_key,
        'cx': api_id,
        'lr': language,
        'gl': location
    }

    # Ajouter les filtres en fonction du type demandé
    if search_type == 'image':
        params['searchType'] = 'image'  # Recherche d'images
    elif search_type == 'video':
        params['q'] += ' video'  # Ajoute "video" dans la requête pour obtenir plus de vidéos
    elif search_type == 'pdf':
        params['fileType'] = 'pdf'  # Recherche de fichiers PDF
    elif search_type == 'docx':
        params['fileType'] = 'docx'  # Recherche de documents Word
    elif search_type == 'web':
        pass  # Recherche normale (par défaut)

    # Ajouter la restriction de date si précisée
    if date_restrict:
        params['dateRestrict'] = date_restrict

    # Faire la requête à l'API Google
    response = requests.get(url, params=params)
    results = response.json().get('items', [])  # Gérer le cas où 'items' n'existe pas

    # Extraire les résultats en fonction du type
    if search_type == 'image':
        data = [{'title': item['title'], 'link': item['link'], 'image': item.get('image', {}).get('thumbnailLink', '')} for item in results]
    else:
        data = [{'title': item['title'], 'link': item['link']} for item in results]

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
