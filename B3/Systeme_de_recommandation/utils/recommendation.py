from fastapi import FastAPI, HTTPException
import sqlite3
import pandas as pd
import uvicorn
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix , csr_array
import numpy as np


def recommend_items(user_id: int, conn: sqlite3.Connection ,top_n: int = 5):
    def predict_rating(user_index, item_index, user_item_matrix, user_similarity):
        item_ratings = user_item_matrix[:, item_index].toarray().flatten()
        similar_users = user_similarity[user_index]
        numerator = np.sum(similar_users * item_ratings)
        denominator = np.sum(np.abs(similar_users)) + 1e-8

        if denominator == 0:
            return 0
        return numerator / denominator

    cursor = conn.cursor()

    # Récupération des données depuis la base de données
    cursor.execute("SELECT user_id, item_id, rating FROM amazon_table")
    data = cursor.fetchall()
    conn.close()

    # Transformation en matrice creuse
    data = pd.DataFrame(data, columns=['user_id', 'item_id', 'rating'])
    print(data)

    # Re-indexation des utilisateurs et articles pour réduire la taille
    user_mapping = {old_id: new_id for new_id, old_id in enumerate(data['user_id'].unique())}
    item_mapping = {old_id: new_id for new_id, old_id in enumerate(data['item_id'].unique())}

    data['user_id'] = data['user_id'].map(user_mapping)
    data['item_id'] = data['item_id'].map(item_mapping)


    
    user_item_matrix = csr_matrix((data['rating'], (data['user_id'], data['item_id'])))
    print(user_item_matrix)
    sparsity = 1 - (user_item_matrix.nnz / (user_item_matrix.shape[0] * user_item_matrix.shape[1]))
    print(f"Sparsity: {sparsity * 100:.2f}%")

    print(f"Shape: {user_item_matrix.shape}")  # Dimensions
    print(f"Non-zero elements: {user_item_matrix.nnz}")  # Éléments non nuls

    # Filtrage de la matrice
    min_user_interactions = 1
    min_item_interactions = 1
    active_users = np.where(user_item_matrix.getnnz(axis=1) >= min_user_interactions)[0]
    active_items = np.where(user_item_matrix.getnnz(axis=0) >= min_item_interactions)[0]
    user_item_matrix = user_item_matrix[active_users][:, active_items]

    user_similarity = cosine_similarity(user_item_matrix, dense_output=False)
    user_index = user_id

    user_ratings = user_item_matrix[user_index].toarray().flatten()

    recommendations = []
    for item_index in range(user_item_matrix.shape[1]):
        if user_ratings[item_index] == 0:  # Article non évalué
            predicted_rating = predict_rating(user_index, item_index, user_item_matrix, user_similarity)
            recommendations.append((item_index, predicted_rating))

    recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)
    return recommendations[:top_n]




def recommend_based_on_item(user_id: int, conn: sqlite3.Connection, top_n: int = 5):
    def predict_rating(item_index, user_index, matrice_utilisateur_item, similarite_item):
        # Récupère les notes de l'utilisateur pour tous les items
        notes_utilisateur = matrice_utilisateur_item[user_index, :].toarray().flatten()
        # Récupère les items similaires
        items_similaires = similarite_item[item_index]

        # Calcul du numérateur et du dénominateur pour la prédiction
        numerateur = np.sum(items_similaires * notes_utilisateur)
        denominateur = np.sum(np.abs(items_similaires)) + 1e-8  # Petit epsilon pour éviter la division par zéro

        if denominateur == 0:
            return 0
        return numerateur / denominateur

    # Création du curseur pour la connexion à la base de données
    cursor = conn.cursor()

    # Récupération des données depuis la base de données
    cursor.execute("SELECT user_id, item_id, rating FROM amazon_table")
    donnees = cursor.fetchall()
    conn.close()

    # Transformation des données en DataFrame
    donnees = pd.DataFrame(donnees, columns=['user_id', 'item_id', 'rating'])

    # Création des mappings des ID utilisateur et item
    mapping_utilisateur = {old_id: new_id for new_id, old_id in enumerate(donnees['user_id'].unique())}
    mapping_item = {old_id: new_id for new_id, old_id in enumerate(donnees['item_id'].unique())}

    # Mise à jour des IDs avec les nouveaux indices
    donnees['user_id'] = donnees['user_id'].map(mapping_utilisateur)
    donnees['item_id'] = donnees['item_id'].map(mapping_item)

    # Création de la matrice utilisateur-item
    matrice_utilisateur_item = csr_matrix((donnees['rating'], (donnees['user_id'], donnees['item_id'])))

    # Filtrage de la matrice : sélectionner les utilisateurs et items ayant suffisamment d'interactions
    interactions_min_utilisateur = 2
    interactions_min_item = 2
    utilisateurs_actifs = np.where(matrice_utilisateur_item.getnnz(axis=1) >= interactions_min_utilisateur)[0]
    items_actifs = np.where(matrice_utilisateur_item.getnnz(axis=0) >= interactions_min_item)[0]
    matrice_utilisateur_item = matrice_utilisateur_item[utilisateurs_actifs][:, items_actifs]

    # Calcul de la similarité entre les items
    similarite_item = cosine_similarity(matrice_utilisateur_item.T, dense_output=False)

    # Récupérer les items déjà notés par l'utilisateur
    items_notes_utilisateur = matrice_utilisateur_item[user_id, :].toarray().flatten()
    
    # Trouver les items non notés par l'utilisateur
    items_non_notes = np.where(items_notes_utilisateur == 0)[0]

    # Liste des recommandations basées sur les items similaires
    recommandations = []
    
    # Parcourir les items non notés par l'utilisateur
    for item_index in items_non_notes:
        # Calculer la note prédite pour l'utilisateur sur cet item
        note_predite = 0
        for item_interagi in np.where(items_notes_utilisateur > 0)[0]:
            note_predite += predict_rating(item_index, user_id, matrice_utilisateur_item, similarite_item)
        
        recommandations.append((int(item_index), float(note_predite)))

    # Trier les recommandations par note prédite (plus élevée en premier)
    recommandations = sorted(recommandations, key=lambda x: x[1], reverse=True)

    # Retourner les meilleures recommandations
    return recommandations[:top_n]