
# API Flask pour la recherche d'images avec Google Custom Search

Cette API Flask permet d'effectuer des recherches d'images en utilisant l'API Google Custom Search. Elle est déployée sur Vercel et peut être personnalisée en passant des paramètres via l'URL.

## Fonctionnalités

- Recherche d'images via l'API Google Custom Search.
- Personnalisation des paramètres de recherche (requête, type de recherche, restriction de date, langue, localisation).
- Déploiement facile sur Vercel.

## Prérequis

- Python 3.8 ou supérieur
- Un compte Google Cloud pour obtenir une clé API et un ID de moteur de recherche.
- Un compte Vercel pour le déploiement.

## Configuration

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/Schmied07/Google_search.git
   cd Google_search
   ```

2. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer les variables d'environnement** :
   Créez un fichier `.env` à la racine du projet et ajoutez vos clés API :
   ```env
   API_KEY=votre_clé_api_google
   SEARCH_ENGINE_ID=votre_id_moteur_recherche
   ```

## Utilisation en local

1. **Démarrer l'application Flask** :
   ```bash
   python app.py
   ```

2. **Accéder à l'API** :
   Ouvrez votre navigateur ou utilisez un outil comme `curl` ou Postman pour accéder à l'API :
   ```
   http://127.0.0.1:5000/search?q=chat&searchType=image
   ```

   ### Paramètres disponibles :
   - `q` : Terme de recherche (par défaut : `reussite`).
   - `searchType` : Type de recherche (par défaut : `image`).
   - `dateRestrict` : Restriction de date (format : `YYYY-MM-DD:YYYY-MM-DD`).
   - `lr` : Langue des résultats (par défaut : `lang_en`).
   - `gl` : Localisation (par défaut : `FR`).

   Exemple :
   ```
   http://127.0.0.1:5000/search?q=chien&searchType=image&dateRestrict=2023-01-01:2023-12-31&lr=lang_fr&gl=FR
   ```

## Déploiement sur Vercel

1. **Installer Vercel CLI** :
   ```bash
   npm install -g vercel
   ```

2. **Se connecter à Vercel** :
   ```bash
   vercel login
   ```

3. **Déployer l'application** :
   ```bash
   vercel
   ```

4. **Configurer les variables d'environnement sur Vercel** :
   - Allez dans les paramètres de votre projet sur le tableau de bord Vercel.
   - Ajoutez les variables `API_KEY` et `SEARCH_ENGINE_ID`.

5. **Accéder à l'API déployée** :
   Une fois déployé, vous recevrez une URL comme `https://votre-app.vercel.app`. Utilisez-la pour accéder à l'API :
   ```
   https://votre-app.vercel.app/search?q=chat&searchType=image
   ```

## Structure du projet

```
.
├── app.py                # Fichier principal de l'API Flask
├── requirements.txt      # Dépendances Python
├── .env                  # Fichier de variables d'environnement (ignoré par Git)
├── .gitignore            # Fichier pour ignorer les fichiers inutiles
├── vercel.json           # Configuration pour Vercel
└── README.md             # Ce fichier
```

## Contribuer

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`).
3. Committez vos changements (`git commit -m 'Ajouter une fonctionnalité incroyable'`).
4. Poussez vers la branche (`git push origin feature/AmazingFeature`).
5. Ouvrez une Pull Request.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

### Exemple de fichier `requirements.txt`

Si vous n'avez pas encore de fichier `requirements.txt`, vous pouvez en créer un avec les dépendances nécessaires :

```txt
Flask==2.3.2
requests==2.31.0
python-dotenv==1.0.0
```

---

Ce `README.md` fournit toutes les informations nécessaires pour comprendre, utiliser et contribuer à votre projet. Vous pouvez le personnaliser en fonction de vos besoins spécifiques.#   G o o g l e _ s e a r c h  
 