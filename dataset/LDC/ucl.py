import pandas as pd

df = pd.read_csv(r"dataset\LDC\ucl_clubs_attack.csv")
new_colonnes = df["team"].str.split(" ", expand=True)
new_colonnes.columns = ["Rank", "Equipe", "Country", "Attack", "Assist", "Corner_taken", "Offside", "Dribble", "Match_played"]
new_colonnes.to_csv(r"dataset\LDC\ucl_clubs_attack.csv", index=False)


df2 = pd.read_csv(r"dataset\LDC\ucl_players_attack.csv")
new_colonnes = df2["team"].str.split(" ", expand=True)
new_colonnes.columns = ["Rank", "Nom", "Equipe", "Tiret", "Poste", "Assist", "Corner_taken", "Offside", "Dribble", "Match_played"]
new_colonnes = pd.read_csv(r"dataset\LDC\ucl_players_attack.csv")
new_colonnes.drop("Tiret", axis=1, inplace=True)
new_colonnes.to_csv(r"dataset\LDC\ucl_players_attack.csv", index=False)