import requests
import json
import pymongo

# Définir les paramètres de recherche
query = 'Manchester United OR Arsenal OR Monaco'
date_since = '2022-09-06'
date_until = '2022-11-02'

# Mettre les clés d'authentification de l'API
consumer_key = "UMu0ZInTt5m8E82QgKHCdJz6X"
consumer_secret = "BxQFZsxwGaJumNUWiIV6meWaxaSoR9Ei530BJf6c058bN5P69d"
access_token = "1137234111783997440-wqlCTqMI2r92Ux7RGdBXU19kwFpqld"
access_token_secret = "kqEp5C4LXK4oXvh5F4FyAa04sZGHosxuoaCagSK382skf"

# Préparer les en-têtes pour l'authentification
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

# Préparer les paramètres pour la requête
params = {
    'q': query,
    'since': date_since,
    'until': date_until,
    'lang': 'fr',
    'count': 100
}

# Effectuer la requête à l'API
response = requests.get('https://api.twitter.com/1.1/search/tweets.json', headers=headers, params=params)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Charger les données de la réponse
    tweets = json.loads(response.content.decode('utf-8'))

    # Connecter à la base de données MongoDB
    client = pymongo.MongoClient("mongodb+srv://Aroune:root@cluster0.cl9j9un.mongodb.net/")
    db = client["Cluster0"]
    collection = db["Tweets-EL-Clubs"]

    # Insérer les tweets dans la collection
    collection.insert_many(tweets['statuses'])
    print('Les tweets ont été stockés avec succès dans la base de données.')
else:
    print('La requête a échoué avec le code d\'erreur {}.'.format(response.status_code))