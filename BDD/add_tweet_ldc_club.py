import tweepy
from pymongo import MongoClient

# Ajoutez vos clés d'accès
consumer_key = "H8qzKivjZxiGaJIdCxFr3QX49"
consumer_secret = "NKQgoaIFONVeSEwXuE4aNabVuqF3wW5QByPJFFoy9UkoQmtBkV"
access_token = "1588115651989848066-tN1jcTK3lcHFEjVJ99VKOc9zITndRv"
access_token_secret = "Ek58DFJLvJWh6xWNurmH4gZSiKxVEALVL55bZb3wIwMeR"

# Autorisez l'accès à l'API Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Connectez-vous à la base de données MongoDB
client = MongoClient("mongodb+srv://Aroune:root@cluster0.cl9j9un.mongodb.net/")
db = client["Cluster0"]
tweets_collection = db["Tweets-LDC-Clubs"]

# Définissez les noms des footballeurs à rechercher
clubs = ["Paris", "Manchester city", "Réal madrid", "Liverpool"]

# Récupérez les tweets contenant les noms des footballeurs et stockez-les dans la base de données
for club in clubs:
    query = club
    tweets = tweepy.Cursor(api.search,
                  q=query,
                  lang="fr",
                  since="2022-09-06",
                  until="2022-11-02").items(3000)
    for tweet in tweets:
        tweets_collection.insert_one(tweet._json)