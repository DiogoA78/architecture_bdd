import streamlit as st
import pymongo

######################## CNX BDD ########################

# Connexion à la base de données pour la collection LDC CLUBS
client = pymongo.MongoClient("mongodb+srv://Aroune:root@cluster0.cl9j9un.mongodb.net/")
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
collection2 = db["LDC-Players"]

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
collection3 = db["EL-Clubs"]

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
collection4 = db["EL-Players"]

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
onglets = ["Accueil", "LDC Clubs", "LDC Players", "EL Clubs", "EL Players", "Tweets LDC Clubs", "Tweets LDC Players", "Tweets EL Clubs", "Tweets EL Players"]
onglet_actif = st.sidebar.selectbox("Sélectionnez un onglet", onglets)

if onglet_actif == "Accueil":
    col1, col2, col3 = st.columns([7,10,7])
    with col2:
        st.write("Nous avons le plaisir de vous accueillir sur notre Dashboard !")
    
    col1, col2, col3 = st.columns([7,4,7])
    with col2:
        st.image("https://media.tenor.com/ZxrfW_fFgY4AAAAC/messi-que-miras.gif",width=200)

    ######################## LDC CLUBS ########################
    # Utilisation des méthodes CRUD définies précédemment pour la collection LDC CLUBS

    
elif onglet_actif == "LDC Clubs":
    st.write("Ajouter un club")
    # Bouton pour la méthode de création
    Rank = st.number_input("Entrer le rank:")
    Equipe = st.text_input("Entrer l'équipe:")
    Country = st.text_input("Entrer le pays:")
    Attack = st.number_input("Entrer le nombre d'attaque:")
    Assist = st.number_input("Entrer le nombre de passes décisives:")
    Corner_taken = st.number_input("Entrer le nombre de corner:")
    Offside = st.number_input("Entrer le nombre d'hors jeu:")
    Dribble = st.number_input("Entrer le nombre de dribble:")
    Match_played = st.number_input("Entrer le nombre de matchs joués:")
    if st.button("Ajouter un club"):
        data = {"Rank": Rank, "Equipe": Equipe, "Country": Country, "Attack": Attack, "Assist": Assist, "Corner_taken": Corner_taken, "Offside": Offside,
        "Dribble": Dribble, "Match_played": Match_played}
        create_document1(data)
        st.success("Club ajouté avec succès.")

    
    # Bouton pour la méthode de lecture
    st.write("")
    st.write("Lire les données")
    if st.button("Lire les données"):
        query = {}
        documents = list(read_document1(query))
        st.json(documents)    

    # Bouton pour la méthode de mise à jour
    st.write("")
    st.write("Mettre à jour une Equipe")
    query = {"Equipe": st.text_input("Entrer le nom d'un club à mettre à jour:")}
    Rank = st.number_input("Entrer le nouveau rank:")
    Country = st.text_input("Entrer le nouveau pays:")
    Attack = st.number_input("Entrer le nouveau nombre d'attaque:")
    Assist = st.number_input("Entrer le nouveau nombre de passes décisives:")
    Corner_taken = st.number_input("Entrer le nouveau nombre de corner:")
    Offside = st.number_input("Entrer le nouveau nombre d'hors jeu:")
    Dribble = st.number_input("Entrer le nouveau nombre de dribble:")
    Match_played = st.number_input("Entrer le nouveau nombre de matchs joués:")
    nouvelles_valeurs = {"Rank": Rank, "Country": Country, "Attack": Attack, "Assist": Assist, "Corner_taken": Corner_taken, "Offside": Offside,
        "Dribble": Dribble, "Match_played": Match_played}
    if st.button("Mettre à jour une Equipe"):
        update_document1(query, nouvelles_valeurs)
        st.success("Equipe mise à jour avec succès.")

    # Bouton pour la méthode de suppression
    st.write("")
    st.write("Supprimer un club")
    query = {"Equipe": st.text_input("Entrer le nom d'un club à supprimer:")}
    if st.button("Supprimer un club"):
        delete_document1(query)
        st.success("Club supprimé avec succès.")




    ######################## LDC PLAYERS ######################## 

elif onglet_actif == "LDC Players":
    # Utilisation des méthodes CRUD définies précédemment pour la collection LDC PLAYERS


    # Bouton pour la méthode de création
    st.write("Ajouter un joueur")
    Rank = st.number_input("Entrer le rank:")
    Nom = st.text_input("Entrer le nom du joueur:")
    Equipe = st.text_input("Entrer l'equipe:")
    Poste = st.text_input("Entrer le poste:")
    Assist = st.number_input("Entrer le nombre de passes décisives:")
    Corner_taken = st.number_input("Entrer le nombre de corner:")
    Offside = st.number_input("Entrer le nombre d'hors jeu:")
    Dribble= st.number_input("Entrer le nombre de dribble:")
    Match_played = st.number_input("Entrer le nombre de matchs joués:")
    if st.button("Ajouter un joueur"):
        data = {"Rank": Rank, "Nom": Nom, "Equipe": Equipe, "Poste": Poste, "Assist": Assist, "Corner_taken": Corner_taken, "Offside": Offside,"Dribble": Dribble,
        "Match_played": Match_played}
        create_document2(data)
        st.success("Document créé avec succès.")

    # Bouton pour la méthode de lecture
    st.write("")
    st.write("Lire les données")
    if st.button("Lire les données"):
        query = {}
        documents = list(read_document2(query))
        st.json(documents)

    # Bouton pour la méthode de mise à jour
    st.write("")
    st.write("Mettre à jour un joueur")
    query = {"Nom": st.text_input("Entrer le nom du joueur à mettre à jour:")}
    Rank = st.number_input("Entrer le nouveau rank:")
    Equipe = st.text_input("Entrer la nouvelle equipe:")
    Poste = st.text_input("Entrer le nouveau poste:")
    Assist = st.number_input("Entrer le nouveau nombre de passes décisives:")
    Corner_taken = st.number_input("Entrer le nouveau nombre de corner:")
    Offside = st.number_input("Entrer le nouveau nombre d'hors jeu:")
    Dribble= st.number_input("Entrer le nouveau nombre de dribble:")
    Match_played = st.number_input("Entrer le nouveau nombre de matchs joués:")
    if st.button("Mettre à jour un joueur"):
        nouvelles_valeurs = {"Rank": Rank, "Equipe": Equipe, "Poste": Poste, "Assist": Assist, "Corner_taken": Corner_taken, "Offside": Offside,"Dribble": Dribble,
        "Match_played": Match_played}
        update_document2(query, nouvelles_valeurs)
        st.success("Joueur mis à jour avec succès.")

    # Bouton pour la méthode de suppression
    st.write("")
    st.write("Supprimer un joueur")
    query = {"Nom": st.text_input("Entrer le nom d'un joueur à supprimer:")}
    if st.button("Supprimer un joueur"):
        delete_document2(query)
        st.success("Joueur supprimé avec succès.")


######################## EL CLUBS ########################
elif onglet_actif == "EL Clubs":
    # Utilisation des méthodes CRUD définies précédemment pour la collection EL CLUBS


    # Bouton pour la méthode de création
    st.write("Ajouter une équipe")
    Rank = st.number_input("Entrer le rank:")
    Equipe = st.text_input("Entrer l'équipe:")
    Country = st.text_input("Entrer le pays:")
    Attack = st.number_input("Entrer le nombre d'attaque:")
    Assist = st.number_input("Entrer le nombre de passes décisives:")
    Corner_taken = st.number_input("Entrer le nombre de corner:")
    Offside = st.number_input("Entrer le nombre d'hors jeu:")
    Match_played = st.number_input("Entrer le nombre de matchs joués:")
    if st.button("Ajouter une équipe"):
        data = {"Rank": Rank, "Equipe": Equipe, "Country": Country, "Attack": Attack, "Assist": Assist, "Corner_taken": Corner_taken, "Offside": Offside,
        "Match_played": Match_played}
        create_document3(data)
        st.success("Equipe ajouté avec succès.")

    # Bouton pour la méthode de lecture
    st.write("")
    st.write("ALire les données")
    if st.button("Lire les données"):
        query = {}
        documents = list(read_document3(query))
        st.json(documents)

    # Bouton pour la méthode de mise à jour
    st.write("")
    st.write("Mettre à jour une équipe")
    query = {"Equipe": st.text_input("Entrer le nom de l'équipe à mettre à jour:")}
    Rank = st.number_input("Entrer nouveau le rank:")
    Country = st.text_input("Entrer le nouveau pays:")
    Attack = st.number_input("Entrer le nouveau nombre d'attaque:")
    Assist = st.number_input("Entrer le nouveau nombre de passes décisives:")
    Corner_taken = st.number_input("Entrer le nouveau nombre de corner:")
    Offside = st.number_input("Entrer le nouveau nombre d'hors jeu:")
    Match_played = st.number_input("Entrer le nouveau nombre de matchs joués:")
    if st.button("Mettre à jour une Equipe"):
        nouvelles_valeurs = {"Rank": Rank, "Country": Country, "Attack": Attack, "Assist": Assist, "Corner_taken": Corner_taken, "Offside": Offside,
        "Match_played": Match_played}
        update_document3(query, nouvelles_valeurs)
        st.success("Equipe mise à jour avec succès.")

    # Bouton pour la méthode de suppression
    st.write("")
    st.write("Supprimer un joueur")
    query = {"Equipe": st.text_input("Entrer le nom de l'equipe à supprimer:")}
    if st.button("Supprimer une equipe"):
        delete_document3(query)
        st.success("Equipe supprimée avec succès.")


######################## EL PLAYERS ########################
elif onglet_actif == "EL Players":
    # Utilisation des méthodes CRUD définies précédemment pour la collection EL PLAYERS


    # Bouton pour la méthode de création
    st.write("Ajouter un joueur")
    Rank = st.number_input("Entrer le rank:")
    Nom = st.text_input("Entrer le nom du joueur:")
    Equipe = st.text_input("Entrer l'equipe:")
    Poste = st.text_input("Entrer le poste:")
    Assist = st.number_input("Entrer le nombre de passes décisives:")
    Corner_taken = st.number_input("Entrer le nombre de corner:")
    Offside = st.number_input("Entrer le nombre d'hors jeu:")
    Match_played = st.number_input("Entrer le nombre de matchs joués:")
    if st.button("Ajouter un joueur"):
        data = {"Rank": Rank, "Equipe": Equipe, "Poste": Poste, "Assist": Assist, "Corner_taken": Corner_taken, "Offside": Offside,
        "Match_played": Match_played}
        create_document4(data)
        st.success("Joueur ajouté avec succès.")

    # Bouton pour la méthode de lecture
    st.write("")
    st.write("Lire les données")
    if st.button("Lire les données"):
        query = {}
        documents = list(read_document4(query))
        st.json(documents)

    # Bouton pour la méthode de mise à jour
    st.write("")
    st.write("Mettre à jour un joueur")
    query = {"Nom": st.text_input("Entrer le nom du joueur à mettre à jour:")}
    Rank = st.number_input("Entrer le nouveau rank:")
    Equipe = st.text_input("Entrer la nouvelle equipe :")
    Poste = st.text_input("Entrer le nouveau le poste:")
    Assist = st.number_input("Entrer le nouveau nombre de passes décisives:")
    Corner_taken = st.number_input("Entrer le nouveau nombre de corner:")
    Offside = st.number_input("Entrer le nouveau nombre d'hors jeu:")
    Match_played = st.number_input("Entrer le nouveau nombre de matchs joués:")
    if st.button("Mettre à jour un joueur"):
        nouvelles_valeurs = {"Rank": Rank, "Equipe": Equipe, "Poste": Poste, "Assist": Assist, "Corner_taken": Corner_taken, "Offside": Offside,
        "Match_played": Match_played}
        update_document4(query, nouvelles_valeurs)
        st.success("Joueur mis à jour avec succès.")

    # Bouton pour la méthode de suppression
    st.write("")
    st.write("Supprimer un joueur")
    query = {"Nom": st.text_input("Entrer le nom d'un joueur à supprimer:")}
    if st.button("Supprimer un joueur"):
        delete_document4(query)
        st.success("Joueur supprimé avec succès.")

########################################### TWITTER ########################################
######################## CNX BDD ########################

# Connexion à la base de données pour la collection LDC CLUBS
client = pymongo.MongoClient("mongodb+srv://Aroune:root@cluster0.cl9j9un.mongodb.net/")
db = client["Cluster0"]
collection5 = db["Tweets-LDC-Clubs"]

# Méthode de création
def create_document5(data):
    collection5.insert_one(data)
    print("Document créé avec succès.")

# Méthode de lecture
def read_document5(query={}):
    return collection5.find(query)

# Méthode de mise à jour
def update_document5(query, nouvelles_valeurs):
    collection5.update_one(query, {"$set": nouvelles_valeurs})
    print("Document mis à jour avec succès.")

# Méthode de suppression
def delete_document5(query):
    collection5.delete_one(query)
    print("Document supprimé avec succès.")

# Connexion à la base de données pour la collection LDC PLAYERS
collection6 = db["Tweets-LDC-Players"]

# Méthode de création
def create_document6(data):
    collection6.insert_one(data)
    print("Document créé avec succès.")

# Méthode de lecture
def read_document6(query={}):
    return collection6.find(query)

# Méthode de mise à jour
def update_document6(query, nouvelles_valeurs):
    collection6.update_one(query, {"$set": nouvelles_valeurs})
    print("Document mis à jour avec succès.")

# Méthode de suppression
def delete_document6(query):
    collection6.delete_one(query)
    print("Document supprimé avec succès.")

# Connexion à la base de données pour la collection EL CLUBS
collection7 = db["Tweets-EL-Clubs"]

# Méthode de création
def create_document7(data):
    collection7.insert_one(data)
    print("Document créé avec succès.")

# Méthode de lecture
def read_document7(query={}):
    return collection7.find(query)

# Méthode de mise à jour
def update_document7(query, nouvelles_valeurs):
    collection7.update_one(query, {"$set": nouvelles_valeurs})
    print("Document mis à jour avec succès.")

# Méthode de suppression
def delete_document7(query):
    collection7.delete_one(query)
    print("Document supprimé avec succès.")

# Connexion à la base de données pour la collection EL PLAYERS
collection8 = db["Tweets-EL-Players"]

# Méthode de création
def create_document8(data):
    collection8.insert_one(data)
    print("Document créé avec succès.")

# Méthode de lecture
def read_document8(query={}):
    return collection8.find(query)

# Méthode de mise à jour
def update_document8(query, nouvelles_valeurs):
    collection8.update_one(query, {"$set": nouvelles_valeurs})
    print("Document mis à jour avec succès.")

# Méthode de suppression
def delete_document8(query):
    collection8.delete_one(query)
    print("Document supprimé avec succès.")

if onglet_actif == "Tweets LDC Clubs":
    st.write("Ajouter un tweet")
    # Bouton pour la méthode de création
    text = st.text_input("Entrer le tweet:")
    user = st.text_input("Entrer un utilisateur:")
    likes = st.number_input("Entrer le nombre de likes:")
    if st.button("Ajouter un tweet"):
        data = {"text": text, "user": user, "likes": likes}
        create_document1(data)
        st.success("Tweet ajouté avec succès.")

    # Bouton pour la méthode de lecture
    st.write("")
    st.write("Lire les tweets")
    if st.button("Lire les tweets"):
        query = {}
        documents = list(read_document1(query))
        st.json(documents)

        # Bouton pour la méthode de mise à jour
    st.write("")
    st.write("Mettre à jour une tweet")
    query = {"user": st.text_input("Entrer le nom d'un utilisateur à mettre à jour:")}
    text = st.text_input("Entrer le nouveau tweet:")
    likes = st.number_input("Entrer le nouveau nombre de like:")

    nouvelles_valeurs = {"text": text, "likes": likes}
    if st.button("Mettre à jour un tweet"):
        update_document1(query, nouvelles_valeurs)
        st.success("Tweet mise à jour avec succès.")

    # Bouton pour la méthode de suppression
    st.write("")
    st.write("Supprimer un tweet")
    query = {"user": st.text_input("Entrer le nom d'un utilisateur à supprimer:")}
    if st.button("Supprimer un tweet"):
        delete_document1(query)
        st.success("tweet supprimé avec succès.")


elif onglet_actif == "Tweets LDC Players":
    st.write("Ajouter un tweet")
    # Bouton pour la méthode de création
    text = st.text_input("Entrer le tweet:")
    user = st.text_input("Entrer un utilisateur:")
    likes = st.number_input("Entrer le nombre de likes:")
    if st.button("Ajouter un tweet"):
        data = {"text": text, "user": user, "likes": likes}
        create_document1(data)
        st.success("Tweet ajouté avec succès.")

    # Bouton pour la méthode de lecture
    st.write("")
    st.write("Lire les tweets")
    if st.button("Lire les tweets"):
        query = {}
        documents = list(read_document1(query))
        st.json(documents)

        # Bouton pour la méthode de mise à jour
    st.write("")
    st.write("Mettre à jour une tweet")
    query = {"user": st.text_input("Entrer le nom d'un utilisateur à mettre à jour:")}
    text = st.text_input("Entrer le nouveau tweet:")
    likes = st.number_input("Entrer le nouveau nombre de like:")

    nouvelles_valeurs = {"text": text, "likes": likes}
    if st.button("Mettre à jour un tweet"):
        update_document1(query, nouvelles_valeurs)
        st.success("Tweet mise à jour avec succès.")

    # Bouton pour la méthode de suppression
    st.write("")
    st.write("Supprimer un tweet")
    query = {"user": st.text_input("Entrer le nom d'un utilisateur à supprimer:")}
    if st.button("Supprimer un tweet"):
        delete_document1(query)
        st.success("tweet supprimé avec succès.")

elif onglet_actif == "Tweets EL Clubs":
    st.write("Ajouter un tweet")
    # Bouton pour la méthode de création
    text = st.text_input("Entrer le tweet:")
    user = st.text_input("Entrer un utilisateur:")
    likes = st.number_input("Entrer le nombre de likes:")
    if st.button("Ajouter un tweet"):
        data = {"text": text, "user": user, "likes": likes}
        create_document1(data)
        st.success("Tweet ajouté avec succès.")

    # Bouton pour la méthode de lecture
    st.write("")
    st.write("Lire les tweets")
    if st.button("Lire les tweets"):
        query = {}
        documents = list(read_document1(query))
        st.json(documents)

        # Bouton pour la méthode de mise à jour
    st.write("")
    st.write("Mettre à jour une tweet")
    query = {"user": st.text_input("Entrer le nom d'un utilisateur à mettre à jour:")}
    text = st.text_input("Entrer le nouveau tweet:")
    likes = st.number_input("Entrer le nouveau nombre de like:")

    nouvelles_valeurs = {"text": text, "likes": likes}
    if st.button("Mettre à jour un tweet"):
        update_document1(query, nouvelles_valeurs)
        st.success("Tweet mise à jour avec succès.")

    # Bouton pour la méthode de suppression
    st.write("")
    st.write("Supprimer un tweet")
    query = {"user": st.text_input("Entrer le nom d'un utilisateur à supprimer:")}
    if st.button("Supprimer un tweet"):
        delete_document1(query)
        st.success("tweet supprimé avec succès.")


elif onglet_actif == "Tweets EL Players":
    st.write("Ajouter un tweet")
    # Bouton pour la méthode de création
    text = st.text_input("Entrer le tweet:")
    user = st.text_input("Entrer un utilisateur:")
    likes = st.number_input("Entrer le nombre de likes:")
    if st.button("Ajouter un tweet"):
        data = {"text": text, "user": user, "likes": likes}
        create_document1(data)
        st.success("Tweet ajouté avec succès.")

    # Bouton pour la méthode de lecture
    st.write("")
    st.write("Lire les tweets")
    if st.button("Lire les tweets"):
        query = {}
        documents = list(read_document1(query))
        st.json(documents)

        # Bouton pour la méthode de mise à jour
    st.write("")
    st.write("Mettre à jour une tweet")
    query = {"user": st.text_input("Entrer le nom d'un utilisateur à mettre à jour:")}
    text = st.text_input("Entrer le nouveau tweet:")
    likes = st.number_input("Entrer le nouveau nombre de like:")

    nouvelles_valeurs = {"text": text, "likes": likes}
    if st.button("Mettre à jour un tweet"):
        update_document1(query, nouvelles_valeurs)
        st.success("Tweet mise à jour avec succès.")

    # Bouton pour la méthode de suppression
    st.write("")
    st.write("Supprimer un tweet")
    query = {"user": st.text_input("Entrer le nom d'un utilisateur à supprimer:")}
    if st.button("Supprimer un tweet"):
        delete_document1(query)
        st.success("tweet supprimé avec succès.")