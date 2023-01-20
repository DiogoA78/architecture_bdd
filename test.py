import streamlit as st
import pymongo


######################## CNX BDD ########################

# Connexion à la base de données pour la collection LDC CLUBS
client = pymongo.MongoClient("mongodb+srv://Aroune:root@cluster0.cl9j9un.mongodb.net/?ssl=false&ssl_cert_reqs=CERT_NONE")
db = client["Cluster0"]
collection1 = db["LDC-Clubs"]

# Méthode de création
def create_document1(data):
    collection1.insert_one(data)
    print("Document créé avec succès.")

# Méthode de lecture
def read_document1(query={}):
    return collection1.find(query)

# Méthode de mise à jour
def update_document1(query, nouvelles_valeurs):
    collection1.update_one(query, {"$set": nouvelles_valeurs})
    print("Document mis à jour avec succès.")

# Méthode de suppression
def delete_document1(query):
    collection1.delete_one(query)
    print("Document supprimé avec succès.")

# Connexion à la base de données pour la collection LDC PLAYERS
collection2 = db["nom_de_votre_collection"]

# Méthode de création
def create_document2(data):
    collection2.insert_one(data)
    print("Document créé avec succès.")

# Méthode de lecture
def read_document2(query={}):
    return collection2.find(query)

# Méthode de mise à jour
def update_document2(query, nouvelles_valeurs):
    collection2.update_one(query, {"$set": nouvelles_valeurs})
    print("Document mis à jour avec succès.")

# Méthode de suppression
def delete_document2(query):
    collection2.delete_one(query)
    print("Document supprimé avec succès.")

# Connexion à la base de données pour la collection EL CLUBS
collection3 = db["nom_de_votre_collection"]

# Méthode de création
def create_document3(data):
    collection3.insert_one(data)
    print("Document créé avec succès.")

# Méthode de lecture
def read_document3(query={}):
    return collection3.find(query)

# Méthode de mise à jour
def update_document3(query, nouvelles_valeurs):
    collection3.update_one(query, {"$set": nouvelles_valeurs})
    print("Document mis à jour avec succès.")

# Méthode de suppression
def delete_document3(query):
    collection3.delete_one(query)
    print("Document supprimé avec succès.")

# Connexion à la base de données pour la collection EL PLAYERS
collection4 = db["nom_de_votre_collection"]

# Méthode de création
def create_document4(data):
    collection4.insert_one(data)
    print("Document créé avec succès.")

# Méthode de lecture
def read_document4(query={}):
    return collection4.find(query)

# Méthode de mise à jour
def update_document4(query, nouvelles_valeurs):
    collection4.update_one(query, {"$set": nouvelles_valeurs})
    print("Document mis à jour avec succès.")

# Méthode de suppression
def delete_document4(query):
    collection4.delete_one(query)
    print("Document supprimé avec succès.")



######################## DASHBOARD ########################

st.set_page_config(page_title="Dashboard Football", page_icon=":guardsman:", layout="wide")

st.title("Gestion des équipes et joueurs de football avec Streamlit")

# Utilisation des onglets
onglets = ["Accueil", "LDC Clubs", "LDC Players", "EL Clubs", "EL Players"]
onglet_actif = st.sidebar.selectbox("Sélectionnez un onglet", onglets)

if onglet_actif == "Accueil":
    col1, col2, col3 = st.columns([7,10,7])
    with col2:
        st.write("Nous avons le plaisir de vous accueillir sur notre Dashboard !")
        st.write("Sélectionnez l'une des trois meilleurs compétitions de football :soccer:  pour avoir accès à l'historique des rencontres des groupes mais aussi avoir accès \
                aux différentes stats des joueurs et des clubs.")
    
    col1, col2, col3 = st.columns([7,4,7])
    with col2:
        st.image("https://media.tenor.com/ZxrfW_fFgY4AAAAC/messi-que-miras.gif",width=200)

    ######################## LDC CLUBS ########################
    # Utilisation des méthodes CRUD définies précédemment pour la collection LDC CLUBS

    
elif onglet_actif == "LDC Clubs":
    # Bouton pour la méthode de création
    nom = st.text_input("Entrer le nom:")
    age = st.number_input("Entrer l'âge:")
    if st.button("Créer un document"):
        data = {"nom": nom, "age": age}
        create_document1(data)
        st.success("Document créé avec succès.")

    # Bouton pour la méthode de lecture
    if st.button("Lire les documents"):
        query = {}
        documents = list(read_document1(query))
        st.json(documents)

    # Bouton pour la méthode de mise à jour
    query = {"nom": st.text_input("Entrer le nom du document à mettre à jour:")}
    age = st.number_input("Entrer la nouvelle age:")
    nouvelles_valeurs = {"age": age}
    if st.button("Mettre à jour un document"):
        update_document1(query, nouvelles_valeurs)
        st.success("Document mis à jour avec succès.")

    # Bouton pour la méthode de suppression
    query = {"nom": st.text_input("Entrer le nom du document à supprimer:")}
    if st.button("Supprimer un document"):
        delete_document1(query)
        st.success("Document supprimé avec succès.")




    ######################## LDC PLAYERS ######################## 

elif onglet_actif == "LDC Players":
    # Utilisation des méthodes CRUD définies précédemment pour la collection LDC PLAYERS


    # Bouton pour la méthode de création
    nom = st.text_input("Entrer le nom:")
    age = st.number_input("Entrer l'âge:")
    if st.button("Créer un document"):
        data = {"nom": nom, "age": age}
        create_document2(data)
        st.success("Document créé avec succès.")

    # Bouton pour la méthode de lecture
    if st.button("Lire les documents"):
        query = {}
        documents = list(read_document2(query))
        st.json(documents)

    # Bouton pour la méthode de mise à jour
    query = {"nom": st.text_input("Entrer le nom du document à mettre à jour:")}
    age = st.number_input("Entrer la nouvelle age:")
    if st.button("Mettre à jour un document"):
        nouvelles_valeurs = {"age": age}
        update_document2(query, nouvelles_valeurs)
        st.success("Document mis à jour avec succès.")

    # Bouton pour la méthode de suppression
    query = {"nom": st.text_input("Entrer le nom du document à supprimer:")}
    if st.button("Supprimer un document"):
        delete_document2(query)
        st.success("Document supprimé avec succès.")


######################## EL CLUBS ########################
elif onglet_actif == "EL Clubs":
    


    # Utilisation des méthodes CRUD définies précédemment pour la collection EL CLUBS

    st.title("CRUD MongoDB avec Streamlit")

    # Bouton pour la méthode de création
    if st.button("Créer un document"):
        nom = st.text_input("Entrer le nom:")
        age = st.number_input("Entrer l'âge:")
        data = {"nom": nom, "age": age}
        create_document3(data)
        st.success("Document créé avec succès.")

    # Bouton pour la méthode de lecture
    if st.button("Lire les documents"):
        query = {}
        documents = list(read_document3(query))
        st.json(documents)

    # Bouton pour la méthode de mise à jour
    if st.button("Mettre à jour un document"):
        query = {"nom": st.text_input("Entrer le nom du document à mettre à jour:")}
        age = st.number_input("Entrer la nouvelle age:")
        nouvelles_valeurs = {"age": age}
        update_document3(query, nouvelles_valeurs)
        st.success("Document mis à jour avec succès.")

    # Bouton pour la méthode de suppression
    if st.button("Supprimer un document"):
        query = {"nom": st.text_input("Entrer le nom du document à supprimer:")}
        delete_document3(query)
        st.success("Document supprimé avec succès.")


######################## EL PLAYERS ########################
elif onglet_actif == "EL Players":
    



    # Utilisation des méthodes CRUD définies précédemment pour la collection EL PLAYERS

    st.title("CRUD MongoDB avec Streamlit")

    # Bouton pour la méthode de création
    if st.button("Créer un document"):
        nom = st.text_input("Entrer le nom:")
        age = st.number_input("Entrer l'âge:")
        data = {"nom": nom, "age": age}
        create_document4(data)
        st.success("Document créé avec succès.")

    # Bouton pour la méthode de lecture
    if st.button("Lire les documents"):
        query = {}
        documents = list(read_document4(query))
        st.json(documents)

    # Bouton pour la méthode de mise à jour
    if st.button("Mettre à jour un document"):
        query = {"nom": st.text_input("Entrer le nom du document à mettre à jour:")}
        age = st.number_input("Entrer la nouvelle age:")
        nouvelles_valeurs = {"age": age}
        update_document4(query, nouvelles_valeurs)
        st.success("Document mis à jour avec succès.")

    # Bouton pour la méthode de suppression
    if st.button("Supprimer un document"):
        query = {"nom": st.text_input("Entrer le nom du document à supprimer:")}
        delete_document4(query)
        st.success("Document supprimé avec succès.")