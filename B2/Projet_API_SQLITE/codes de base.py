import sqlite3
import datetime

from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI , HTTPException

app = FastAPI()

def ajouter_table(nom_table):
    curseur.execute(f"""CREATE TABLE IF NOT EXISTS {nom_table} (
                        id INTEGER PRIMARY KEY
                       )""")
    print(f"La table {nom_table} a bien ete ajouter")
    conn.commit()
    curseur.close()

def supprimer_table(nom_table):
    curseur.execute(f"DROP TABLE IF EXISTS {nom_table}")
    print(f"La table {nom_table} a bien ete supprimer")
    conn.commit()
    curseur.close()


def selectionner_table(nom_table):
    curseur.execute(f"SELECT * FROM {nom_table}")
    resultats = curseur.fetchall()
    conn.commit()
    curseur.close()
    if len(resultats) == 0:
        print("None")
        return []
    else:
        return resultats


def modifier_table(nom_table, clause_set, clause_where):
    curseur.execute(f"UPDATE {nom_table} SET {clause_set} WHERE {clause_where}")
    conn.commit()
    curseur.close()


#--------------------------------------------------------------------------------------------------------------------------------------

def visualiser_table(table):
    """ Fonction pour visualiser une table. """
    query = f"SELECT * FROM {table}"
    curseur.execute(query)
    fl = curseur.fetchall()
    conn.commit()
    curseur.close()
    return fl

#--------------------------------------------------------------------------------------------------------------------------------------
#medecin


def creer_medecin(donnees= dict):
    """ Fonction pour ajouter un médecin. """
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO Medecin ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()
    


def modifier_medecin(id_medecin, donnees):
    """ Fonction pour modifier un médecin. """
    clause_set = ', '.join([f"{cle} = :{cle}" for cle in donnees])
    requete = f"UPDATE Medecin SET {clause_set} WHERE ID_Medecin_ = :id_medecin"
    donnees['id_medecin'] = id_medecin
    curseur.execute(requete, donnees)
    conn.commit()
    

def visualiser_rdv_medecin(id_medecin):
    """ Fonction pour visualiser les rendez-vous d'aujourd'hui pour un médecin. """
    date_aujourd_hui = datetime.now().strftime("%Y-%m-%d")
    requete = "SELECT * FROM RDV WHERE ID_Medecin_ = :id_medecin AND Date_RDV = :date_aujourd_hui"
    curseur.execute(requete, {'id_medecin': id_medecin, 'date_aujourd_hui': date_aujourd_hui})
    fl = curseur.fetchall()
    conn.commit()
    return fl


#--------------------------------------------------------------------------------------------------------------------------------------
#patient
def creer_patient(donnees):
    """ Fonction pour ajouter un patient. """
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO Patient ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()

def creer_compte(donnees):
    """ Fonction pour ajouter un patient. """
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO Compte ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()
    


def modifier_patient(id_patient, donnees):
    """ Fonction pour modifier un patient. """
    clause_set = ', '.join([f"{cle} = :{cle}" for cle in donnees])
    requete = f"UPDATE Patient SET {clause_set} WHERE ID_Patient = :id_patient"
    donnees['id_patient'] = id_patient
    curseur.execute(requete, donnees)
    conn.commit()

#--------------------------------------------------------------------------------------------------------------------------------------

def visualiser_doss_medical_1_consultation(id_patient, id_consultation):
    """ Fonction pour visualiser une consultation et ses factures/rapports médicaux associés. """
    requete = """
        SELECT *
        FROM consultation c
        LEFT JOIN facture f ON c.id_consultation = f.id_consultation
        LEFT JOIN rapport_analyse ra ON c.id_consultation = ra.id_consultation
        WHERE c.ID_Patient = :id_patient AND c.id_consultation = :id_consultation
    """
    curseur.execute(requete, {'id_patient': id_patient, 'id_consultation': id_consultation})
    fl = curseur.fetchall()
    conn.commit()
    return fl

def visualiser_doss_medical(id_patient):
    requete = """
        SELECT *
        FROM consultation c
        LEFT JOIN facture f ON c.id_consultation = f.id_consultation
        LEFT JOIN rapport_analyse ra ON c.id_consultation = ra.id_consultation
        WHERE c.ID_Patient = :id_patient
    """
    curseur.execute(requete, {'id_patient': id_patient})
    fl = curseur.fetchall()
    conn.commit()
    return fl


#--------------------------------------------------------------------------------------------------------------------------------------
#receptionniste

def creer_receptionniste(donnees):
    """ Fonction pour ajouter un réceptionniste. """
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO Receptionniste ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()
    


def modifier_receptionniste(id_receptionniste, donnees):
    """ Fonction pour modifier un réceptionniste. """
    clause_set = ', '.join([f"{cle} = :{cle}" for cle in donnees])
    requete = f"UPDATE Receptionniste SET {clause_set} WHERE ID_Receptionniste_ = :id_receptionniste"
    donnees['id_receptionniste'] = id_receptionniste
    curseur.execute(requete, donnees)
    conn.commit()

#--------------------------------------------------------------------------------------------------------------------------------------

def modifier_patient_receptionniste(id_receptionniste, id_patient, donnees):
    """ Fonction pour modifier un patient par un réceptionniste. """
    clause_set = ', '.join([f"{cle} = :{cle}" for cle in donnees])
    requete = f"UPDATE Patient SET {clause_set} WHERE ID_Patient = :id_patient AND ID_Receptionniste = :id_receptionniste)"
    donnees['id_patient'] = id_patient
    donnees['id_receptionniste'] = id_receptionniste
    curseur.execute(requete, donnees)
    conn.commit()



#--------------------------------------------------------------------------------------------------------------------------------------
# sert à supprimer un médecin / patient / récéptionniste en le cherchant grâce à son id

def supprimer_M_P_R(id_element, table):
    """ Fonction pour supprimer un Medecin, un Patient, ou une Receptionniste. """
    tables_autorisees = ['Medecin', 'Patient', 'Receptionniste']
    if table not in tables_autorisees:
        raise ValueError(f"La table spécifiée '{table}' n'est pas autorisée. Choisissez parmi {tables_autorisees}.")
    requete = f"DELETE FROM {table} WHERE id = :id"
    curseur.execute(requete, {'id': id_element})
    conn.commit()



#--------------------------------------------------------------------------------------------------------------------------------------
#rdv

def creer_rdv(donnees):
    """ Fonction pour ajouter un rendez-vous. """
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO RDV ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()

def creer_creneau(donnees):
    """ Fonction pour creneau . """
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO Creneau ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()
    


def modifier_etat_rdv(id_rdv, nouveau_etat_rdv):
    """ Fonction pour modifier l'état d'un rendez-vous. """
    requete = "UPDATE RDV SET Etat = :etat WHERE ID_Rendezvous_ = :id_rdv"
    curseur.execute(requete, {'etat': nouveau_etat_rdv, 'id_rdv': id_rdv})
    conn.commit()
    

def annuler_rdv(id_rdv):
    """ Fonction pour annuler (supprimer) un rendez-vous. """
    requete = "DELETE FROM RDV WHERE ID_Rendezvous_ = :id_rdv"
    curseur.execute(requete, {'id_rdv': id_rdv})
    conn.commit()
    


def visualiser_rdv(id_medecin, criteres):
    """ Fonction pour visualiser les rendez-vous d'un médecin. """
    requete = "SELECT * FROM RDV WHERE ID_Medecin_ = :id_medecin"
    for key, value in criteres.items():
        requete += f" AND {key} = :{value}"
    curseur.execute(requete, {'id_medecin': id_medecin, **criteres})
    fl= curseur.fetchall()
    conn.commit()
    return fl

#--------------------------------------------------------------------------------------------------------------------------------------
#analyses

def creer_analyses_urine(donnees):
    """ Fonction pour ajouter une analyse. """
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO Analyses_d_urine ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()

def creer_analyses_sanguines(donnees):
    """ Fonction pour ajouter une analyse. """
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO Analyses_sanguines ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()

def creer_Tests_allergologiques(donnees):
    """ Fonction pour ajouter une analyse. """
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO Tests_allergologiques ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()
    
def creer_Tests_de_depistage_maladies_infectieuses(donnees):
    """ Fonction pour ajouter une analyse. """
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO Tests_de_depistage_maladies_infectieuses ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()



def creer_rapport_analyse(donnees):
    """ Fonction pour ajouter un rapport d'analyse. """
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO Rapport_analyse ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()




#--------------------------------------------------------------------------------------------------------------------------------------
#facture

def creer_facture(donnees):
    """ Fonction pour ajouter une analyse. """
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO Facturation ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()
    

def modifier_facture(id_facture, donnees):
    """ Fonction pour modifier un facture. """
    clause_set = ', '.join([f"{cle} = :{cle}" for cle in donnees])
    requete = f"UPDATE Facturation SET {clause_set} WHERE ID_Facture_ = :id_facture"
    donnees['id_facture'] = id_facture
    curseur.execute(requete, donnees)
    conn.commit()


def supprimer_A_F_R(id_element, table):
    """ Fonction pour supprimer une analyse, une facture, ou un rapport. """
    tables_autorisees = ['Analyse', 'Facturation', 'Rapport']
    if table not in tables_autorisees:
        raise ValueError(f"La table spécifiée '{table}' n'est pas autorisée. Choisissez parmi {tables_autorisees}.")
    requete = f"DELETE FROM {table} WHERE id = :id"
    curseur.execute(requete, {'id': id_element})
    conn.commit()


def visualiser_rdv_journee(date_journee):
    """ Fonction pour visualiser les rendez-vous d'une journée spécifique. """
    requete = "SELECT * FROM RDV WHERE Date_RDV = :date_journee"
    curseur.execute(requete, {'date_journee': date_journee})
    fl = curseur.fetchall()
    conn.commit()
    return fl


def reporting(date_debut, date_fin):
    """ Fonction pour calculer et afficher les statistiques entre deux dates. """
    requete = """
        SELECT COUNT(DISTINCT ID_Patient) as nombre_patients, SUM(montant) as recette
        FROM Facturation
        WHERE Date_de_facturation BETWEEN :date_debut AND :date_fin
    """
    curseur.execute(requete, {'date_debut': date_debut, 'date_fin': date_fin})
    resultats = curseur.fetchone()
    print(f"Nombre de patients : {resultats['nombre_patients']}")
    print(f"Recette totale : {resultats['recette']}")
    conn.commit()

#--------------------------------------------------------------------------------------------------------------------------------------
#message


def ecrire_message(donnees):
    """ Fonction pour qu'un patient puisse écrire un message à un médecin. """
    # Supposons que la table des messages a des colonnes comme 'id_medecin', 'id_patient', 'message', 'date_envoi'
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO Message ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()


def repondre_message(donnees):
    """ Fonction pour qu'un médecin puisse répondre à un message d'un patient. """
    # Supposons que la table des messages a des colonnes comme 'id_medecin', 'id_patient', 'message', 'date_envoi'
    colonnes = ', '.join(donnees.keys())
    placeholders = ':' + ', :'.join(donnees.keys())
    requete = f"INSERT INTO Replique ({colonnes}) VALUES ({placeholders})"
    curseur.execute(requete, donnees)
    conn.commit()

def lire_message(id_medecin):
    """ Fonction pour qu'un médecin puisse lire ses messages. """
    # Supposons que la table des messages a des colonnes comme 'id_medecin', 'id_patient', 'message', 'date_envoi'
    requete = "SELECT * FROM Message WHERE ID_Medecin_ = :id_medecin"
    curseur.execute(requete, {'id_medecin': id_medecin})
    fl = curseur.fetchall()
    conn.commit()
    return fl


#--------------------------------------------------------------------------------------------------------------------------------------
#Test

with sqlite3.connect('Base de donnees Projet DB.db') as conn:
    curseur = conn.cursor()


medecin_info = {
    'Nom': 'Dupont',
    'Prenom': 'isabele',
    'Specialite': 'Medecin génerale',
    'Diplome': 'Doctorat en Médecine',
    'Age': 65,
    'sexe': 'F',
    'Experience': 40,
    'Horaire': '8h-17h',
    'Poste': 'Chef de service',
    'ID_Medecin_': 'M11'
}

patient_exemple = {
    "Nom": "Dupont",
    "Prenom": "Jean",
    "Date_de_naissance": "01/01/1980",
    "Sexe": "M",
    "Adresse": "123 Rue Exemple, Ville, Pays",
    "Numero_de_telephone": "0123456789",
    "Adresse_email": "jean.dupont@example.com",
    "Assurance_medicale": 1234567890,
    "ID_Patient": "P11",
    "ID_Compte_": "C57",
}

receptionniste_exemple = {
    "ID_Receptionniste_": "R4",
    "Nom": "Fox",
    "Prenom": "Charlotte",
    'Horaire': '8h-17h',
    "ID_Facture_": "F4",
}


rdv_exemple = {
    "Date_RDV": "01/01/1980",
    "Etat": "Reserver",
    "Commentaires": "ce rdv est vraiment urgent ",
    "ID_Rendezvous_": "R55",
    'ID_Medecin_': 'M45',
    "ID_Patient": "P56",
    "ID_Creneau_": "C15",
}

facture_exemple = {
    'ID_Facture_': 'F1',
    'Montant': 30,
    "Date_de_facturation": "28/11/2023",
    "Statut_de_paiement": "payer",
    "Moyen_de_payement":"CB",
    "ID_Analyses_sanguines": "AS1",
    'ID_Analyses_d_urine': 'AU1',
    "ID_Tests_allergologiques": "A1",
    "ID_Tests_de_depistage_maladies_infectieuses": "DMI1",
}


medecin_modif = {
    'Specialite': 'Cardiologie',
}

Message_exemple={
    "ID_Message_":"MES1",
    "Contenu":"Bonjour Mr notre RDV est toujour prévu à l'heure",
    'ID_Medecin_': 'M12',
    "ID_Patient": "P11",
}

resep_patient_modif = {
    "Numero_de_telephone": "0634424634",
}



#Fonction qui marche:
"""
creer_medecin(medecin_info)
creer_patient(patient_exemple)
creer_receptionniste(receptionniste_exemple)
creer_rdv(rdv_exemple)
creer_compte(compte_info)
creer_creneau(donnees)
creer_analyses_urine(donnees)
creer_analyses_sanguines(donnees)
creer_Tests_allergologiques(donnees)
creer_Tests_de_depistage_maladies_infectieuses(donnees)
creer_facture(facture_exemple)
modifier_medecin("M12", medecin_modif)
modifier_patient(id_patient, donnees)
modifier_receptionniste(id_receptionniste, donnees)
modifier_facture(id_facture, donnees)
modifier_etat_rdv("R55", "Valider")
annuler_rdv("R55")
ecrire_message(Message_exemple)
lire_message("M12")

"""


#Pas encore test pas de valeur:
"""
visualiser_rdv_medecin(id_medecin)
visualiser_doss_medical_1_consultation(id_patient, id_consultation)
visualiser_doss_medical(id_patient)
visualiser_rdv(id_medecin, criteres)
visualiser_rdv_journee(date_journee)
reporting(date_debut, date_fin)
"""



#Problème:
"""
1)
modifier_patient_receptionniste("R1", "P2", resep_patient_modif)

5)
repondre_message(donnees)
"""



curseur.close()
conn.commit()
conn.close()
