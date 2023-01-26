import tweepy
from pymongo import MongoClient
import matplotlib.pyplot as plt

# Ajoutez vos clés d'accès
consumer_key = "6d4gHuasY9Kfy312WyJsc7Ydf"
consumer_secret = "dQt3YyiMVVXer9uVmTabYA1j4ryBT5d9I4tDBZqkD4Z2G6mxfD"
access_token = "1137234111783997440-wryTsHX4OgIC06RreXnI16xKMAb4YF"
access_token_secret = "Q8BKW3lhQBEhyo9S4laNeP2dKa7JNxSvgi5pxc9qot464"

# Autorisez l'accès à l'API Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Connectez-vous à la base de données MongoDB
client = MongoClient("mongodb+srv://Aroune:root@cluster0.cl9j9un.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE")
db = client["Cluster0"]
tweets_collection = db["Tweets-LDC-Players"]

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