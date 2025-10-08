#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier)


# Mettre dans un commentaire le numéro de la question
# Question 5 afficher 
print(contenu)

# Question 6 Calculer lignes et colonnes
print("Nombre de lignes :", len(contenu))
print("Nombre de colonnes :", len(contenu.columns))

# Question 7 type de chaque colonne
print(contenu.dtypes)

# Question 8 Nom des colonnes
print("Aperçu du tableau:")
print(contenu.head) 

# Question 9 sélection nombre inscrits
print("Nombre des inscrits par département :")
print(contenu.Inscrits) 

# Question 10 Calculer les effectifs des colonnes 
# Créer une liste vide
somme_colonnes = []

# Parcourir chaque colonne
for col in contenu.columns:
    if contenu[col].dtype in ["int64", "float64"]:   # garder uniquement les colonnes numériques int et float
        total = contenu[col].sum()
        somme_colonnes.append((col, total))

# Afficher le résultat
print("Sommes des colonnes aux valeurs quantitatives :")
for col, total in somme_colonnes:
    print(f"- {col} : {total}")

# Question 11 Diagrammes en barres
# Créer le dossier "images", s'il n'existe pas déjà.
import os 
os.makedirs("images", exist_ok=True) 
# Définir les colonnes à tracer
colonnes = ["Inscrits", "Votants"]
# Boucle sur chaque colonne
for col in colonnes:
    plt.figure(figsize=(16,10))
    
    # Tracer le diagramme en barres
    plt.bar(contenu["Libellé du département"], contenu[col], color="skyblue")
    
    # Mise en forme
    plt.xticks(rotation=90)
    plt.title(f"Nombre de {col} par département")
    plt.ylabel("Nombre d'électeurs")
    plt.xlabel("Départements")
    
    # Sauvegarde en PNG
    plt.tight_layout()
    plt.savefig(f"images/{col}.png", dpi=300)
    plt.close()
