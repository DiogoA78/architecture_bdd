from pymongo import MongoClient, collection
import pandas as pd
import csv


def get_database():
    CONNECTION_STRING = "mongodb+srv://Aroune:root@cluster0.cl9j9un.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE"
    client = MongoClient(CONNECTION_STRING)
    return client


def create_db_collection_LDC_PLayers(client):
    db = client['Cluster0']
    collections_name = db["LDC-Players"]
    print('Connexion établie')
    return collections_name

def insert_ldc_player(client):
    db = client['Cluster0']
    collections_name = db["LDC-Players"]
    csvfile = open(r'dataset\LDC\ucl_players_attack.csv', 'r')
    reader = csv.DictReader(csvfile)
    insert_tab = []
    for each in reader:
        insert_tab.append(each)
    print(insert_tab)
    collections_name.insert_many(insert_tab)



client = get_database()

collection_name = create_db_collection_LDC_PLayers(client)

insert_data = insert_ldc_player(client)