
# API Flask pour la recherche d'images avec Google Custom Search

Cette API Flask permet d'effectuer des recherches d'images en utilisant l'API Google Custom Search. Elle est déployée sur Vercel et peut être personnalisée en passant des paramètres via l'URL.

## Fonctionnalités

- Recherche d'images via l'API Google Custom Search.
- Personnalisation des paramètres de recherche (requête, type de recherche, restriction de date, langue, localisation).
- Déploiement facile sur Vercel.
Voici ton **README.md** amélioré avec des clarifications et des ajouts utiles :  

- ✅ **Exemple de réponse JSON**  
- ✅ **Explication plus claire de `dateRestrict`**  
- ✅ **Ajout d’une section "Problèmes fréquents"**  
- ✅ **Mise en forme et structure optimisées**  

---

### 📌 API Flask pour la Recherche d'Images avec Google Custom Search  

Cette API Flask permet d'effectuer des recherches d'images en utilisant l'API Google Custom Search. Elle est déployée sur **Vercel** et peut être personnalisée avec des paramètres passés via l'URL.  

---

## 🚀 Fonctionnalités  

- 🔎 Recherche d'images via l'API **Google Custom Search**  
- ⚙️ Personnalisation des paramètres (requête, type, langue, restriction de date, localisation...)  
- ☁️ Déploiement facile sur **Vercel**  

---

## 📋 Prérequis  

- **Python 3.8 ou supérieur**  
- **Un compte Google Cloud** pour obtenir une clé API et un ID de moteur de recherche  
- **Un compte Vercel** pour le déploiement  

---

## ⚙️ Installation et Configuration  

### 1️⃣ **Cloner le dépôt**  

```bash
git clone https://github.com/Schmied07/Google_search.git
cd Google_search
```

### 2️⃣ **Installer les dépendances**  

```bash
pip install -r requirements.txt
```

### 3️⃣ **Configurer les variables d'environnement**  

Créez un fichier `.env` à la racine du projet et ajoutez vos **clés API** :  

```env
API_KEY=votre_clé_api_google
SEARCH_ENGINE_ID=votre_id_moteur_recherche
```

---

## 🖥️ Utilisation en local  

### 1️⃣ **Démarrer l'application Flask**  

```bash
python app.py
```

### 2️⃣ **Faire une requête à l'API**  

Utilisez un navigateur, `curl` ou **Postman** :  

```bash
http://127.0.0.1:5000/search?q=chat&searchType=image
```

---

## 🔍 Paramètres disponibles  

| Paramètre       | Description |
|----------------|-------------|
| `q`           | **Terme de recherche** (par défaut : `reussite`) |
| `searchType`  | Type de recherche (**par défaut : `image`**) |
| `dateRestrict` | Filtrer par date (ex. `d1` pour 24h, `w1` pour 1 semaine) |
| `lr`          | Langue des résultats (**par défaut : `lang_en`**) |
| `gl`          | Localisation (**par défaut : `FR`**) |

📌 **Exemple avancé** :  

```bash
http://127.0.0.1:5000/search?q=chien&searchType=image&dateRestrict=w1&lr=lang_fr&gl=FR
```

---

## 📅 À propos de `dateRestrict`  

Le paramètre `dateRestrict` permet de **limiter la recherche** à une période spécifique. **Formats acceptés :**  

- `d1` → Dernières 24 heures  
- `w1` → Dernière semaine  
- `m1` → Dernier mois  
- `y1` → Dernière année  

**Exemple** :  
```bash
http://127.0.0.1:5000/search?q=voiture&searchType=image&dateRestrict=m6
```
🔹 **Recherche les images des 6 derniers mois**  

---

## 📦 Exemple de réponse JSON  

Réponse typique retournée par l’API :  

```json
{
  "searchInformation": {
    "searchTime": 0.41,
    "formattedTotalResults": "12,500"
  },
  "items": [
    {
      "title": "Image d'un chat mignon",
      "link": "https://example.com/chat.jpg",
      "image": {
        "contextLink": "https://example.com",
        "thumbnailLink": "https://example.com/thumb.jpg"
      }
    }
  ]
}
```

---

## ☁️ Déploiement sur Vercel  

### 1️⃣ **Installer Vercel CLI**  

```bash
npm install -g vercel
```

### 2️⃣ **Se connecter à Vercel**  

```bash
vercel login
```

### 3️⃣ **Déployer l'application**  

```bash
vercel
```

### 4️⃣ **Configurer les variables d’environnement sur Vercel**  

- Rendez-vous sur **Vercel Dashboard**  
- Ajoutez **API_KEY** et **SEARCH_ENGINE_ID**  

📌 **Accéder à l'API déployée**  

```bash
https://votre-app.vercel.app/search?q=chat&searchType=image
```

---

## 📂 Structure du projet  

```
.
├── app.py                # Code principal de l'API Flask
├── requirements.txt      # Dépendances Python
├── .env                  # Variables d'environnement (ignoré par Git)
├── .gitignore            # Fichiers à ignorer
├── vercel.json           # Configuration pour Vercel
└── README.md             # Ce fichier
```

---

## 🛠️ Problèmes fréquents  

❌ **Erreur `dailyLimitExceeded`**  
✅ Vérifiez si votre clé API a atteint sa limite. Passez à un **compte payant** si besoin.  

❌ **Aucune image trouvée**  
✅ Essayez **d'autres termes de recherche** ou modifiez `dateRestrict`.  

❌ **Erreur de déploiement sur Vercel**  
✅ Assurez-vous que **Flask** est bien importé et que `vercel.json` est bien configuré.  

---

## 👨‍💻 Contribuer  

Les contributions sont **les bienvenues** ! 🚀  

1. **Forkez** le projet  
2. **Créez une branche** (`git checkout -b feature/AmazingFeature`)  
3. **Committez vos changements** (`git commit -m 'Ajouter une fonctionnalité'`)  
4. **Poussez la branche** (`git push origin feature/AmazingFeature`)  
5. **Ouvrez une Pull Request**  

---

## 📜 Licence  

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.  

---

### 📌 Exemple de fichier `requirements.txt`  

Si vous n’avez pas encore ce fichier, ajoutez :  

```txt
Flask==2.3.2
requests==2.31.0
python-dotenv==1.0.0
```

---

🔥 **Prêt à l'emploi !** N'hésite pas à me dire si tu veux des ajustements 😉
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

Ce `README.md` fournit toutes les informations nécessaires pour comprendre, utiliser et contribuer à votre projet. Vous pouvez le personnaliser en fonction de vos besoins spécifiques.#   G o o g l e _ s e a r c h 
 
 
