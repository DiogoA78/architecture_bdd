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

def create_db_collection_LDC_Clubs(client):
    db = client['Cluster0']
    collections_name = db["LDC-Clubs"]
    print('Connexion établie')
    return collections_name

def insert_ldc_club(client):
    db = client['Cluster0']
    collections_name = db["LDC-Clubs"]
    csvfile = open(r'dataset\LDC\ucl_clubs_attack.csv', 'r')
    reader = csv.DictReader(csvfile)
    insert_tab = []
    for each in reader:
        insert_tab.append(each)
    print(insert_tab)
    collections_name.insert_many(insert_tab)

def create_db_collection_EL_Players(client):
    db = client['Cluster0']
    collections_name = db["EL-Players"]
    print('Connexion établie')
    return collections_name

def insert_el_player(client):
    db = client['Cluster0']
    collections_name = db["EL-Players"]
    csvfile = open(r'dataset\EL\el_stats_players_attack.csv', 'r')
    reader = csv.DictReader(csvfile)
    insert_tab = []
    for each in reader:
        insert_tab.append(each)
    print(insert_tab)
    collections_name.insert_many(insert_tab)

def create_db_collection_EL_Clubs(client):
    db = client['Cluster0']
    collections_name = db["EL-Clubs"]
    print('Connexion établie')
    return collections_name

def insert_el_club(client):
    db = client['Cluster0']
    collections_name = db["EL-Clubs"]
    csvfile = open(r'dataset\EL\el_stats_clubs_attack.csv', 'r')
    reader = csv.DictReader(csvfile)
    insert_tab = []
    for each in reader:
        insert_tab.append(each)
    print(insert_tab)
    collections_name.insert_many(insert_tab)


client = get_database()


collection_name4 = create_db_collection_EL_Clubs(client)


insert_data4 = insert_el_club(client)