import tweepy
from pymongo import MongoClient

# clés d'accès
consumer_key = "H8qzKivjZxiGaJIdCxFr3QX49"
consumer_secret = "NKQgoaIFONVeSEwXuE4aNabVuqF3wW5QByPJFFoy9UkoQmtBkV"
access_token = "1588115651989848066-tN1jcTK3lcHFEjVJ99VKOc9zITndRv"
access_token_secret = "Ek58DFJLvJWh6xWNurmH4gZSiKxVEALVL55bZb3wIwMeR"

# Autoriser l'accès à l'API Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Connection à la base de données MongoDB
client = MongoClient("mongodb+srv://Aroune:root@cluster0.cl9j9un.mongodb.net/")
db = client["Cluster0"]
tweets_collection = db["Tweets-LDC-Players"]

# Définir les noms des footballeurs à rechercher
footballeurs = ["Messi", "Mbappé", "Kimmich", "De Bruyne"]

# Récupérer les tweets contenant les noms des footballeurs et les stocker dans la bdd
for footballeur in footballeurs:
    query = footballeur
    tweets = tweepy.Cursor(api.search_tweets,q=query,lang="fr").items(100)
    for tweet in tweets:
        if not tweet.text.startswith("RT"):
            tweets_collection.insert_one(
                {"text": tweet.text, "user": tweet.user.screen_name, "likes": tweet.favorite_count})