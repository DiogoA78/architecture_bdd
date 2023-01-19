from pymongo import MongoClient, collection
import pandas as pd
import csv

def get_database():
    CONNECTION_STRING = "mongodb+srv://diogoalmeida:BwgYhimlAtpzLT45@projetbdd.uzkeroj.mongodb.net/?retryWrites=true&w=majority&ssl=false"
    client = MongoClient(CONNECTION_STRING)
    return client


def create_db_collection(client):
    db = client['Projetbdd']
    collections_name = db["LDC-Players"]
    return collections_name

def insert_csv(client):
    db = client['Projetbdd']
    collections_name = db["LDC-Players"]
    csvfile = open(r'dataset\LDC\ucl_players_attack.csv', 'r')
    reader = csv.DictReader(csvfile)
    insert_tab = []
    for each in reader:
        insert_tab.append(each)
    print(insert_tab)
    collections_name.insert_many(insert_tab)

client = get_database()

collection_name = create_db_collection(client)

insert_data = insert_csv(client)