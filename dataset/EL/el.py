import pandas as pd

df = pd.read_csv(r"dataset\EL\el_stats_clubs_attack.csv")
new_colonnes = df["team"].str.split(" ", expand=True)
new_colonnes.columns = ["Rank", "Equipe", "Country", "Attack", "Assist", "Corner_taken", "Offside", "Match_played"]
df.drop("team", axis=1, inplace=True)
new_colonnes.to_csv(r"dataset\EL\el_stats_clubs_attack.csv", index=False)


df2 = pd.read_csv(r"dataset\EL\el_stats_players_attack.csv")
new_colonnes2 = df2["team"].str.split(" ", expand=True)
new_colonnes2.columns = ["Rank", "Nom", "Equipe", "Tiret", "Poste", "Assist", "Corner_taken", "Offside", "Match_played"]
new_colonnes2.drop("Tiret", axis=1, inplace=True)
new_colonnes2.to_csv(r"dataset\EL\el_stats_players_attack.csv", index=False)