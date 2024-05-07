from fastapi import FastAPI, HTTPException
from typing import Union
import sqlite3
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI()


def get_db_connection():
    
    return sqlite3.connect('Base de donnees Projet DB.db', check_same_thread=False) 

conn = get_db_connection()
cursor = conn.cursor()


@app.get("/visualiser_table/{table_name}")
def visualiser_table(table_name: str):
    try:
       

        query = f'SELECT * FROM "{table_name}"'
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    except Exception as e:
            return {"error": str(e)}
    

@app.post("/create_table/{nom_table}")
def ajouter_table(nom_table: str):

    try:
        cursor = conn.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {nom_table} (
                            id INTEGER PRIMARY KEY
                           )""")
        conn.commit()
        return {"message": f"La table {nom_table} a bien été ajoutée"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/delete_table/{nom_table}")
def supprimer_table(nom_table: str):

    try:
            cursor.execute(f"DROP TABLE IF EXISTS {nom_table}")
            conn.commit()
            return {"message": f"La table {nom_table} a bien été supprimée"}
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))



@app.get("/select_table/{nom_table}")
def selectionner_table(nom_table: str):

    try:
        cursor.execute(f"SELECT * FROM {nom_table}")
        resultats = cursor.fetchall()
        if not resultats:
            return {"message": "Aucune donnée trouvée"}
        return {"data": resultats}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/update_table/{nom_table}")
def modifier_table(nom_table: str, clause_set: str, clause_where: str):

    try:
        cursor.execute(f"UPDATE {nom_table} SET {clause_set} WHERE {clause_where}")
        conn.commit()
        return {"message": f"La table {nom_table} a bien été mise à jour"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#-----------------------------------------------------------------------------------------------------------------------------
#medecin
    
class Medecin(BaseModel):
    Nom: str
    Prenom: str
    Specialite: str
    Diplome: str
    Age: int
    sexe: str
    Experience: int
    Horaire: str
    Poste: str
    ID_Medecin_: str

    
@app.post("/ajouter_medecin/{ID_Medecin_}")
def ajouter_medecin(medecin: Medecin):
    """ Fonction pour ajouter un médecin. """
    try:
            missing = 1
            for  data in medecin :
                    if  data[1] == "string" :
                      missing = 0
                      print("ahhhhhh")
                      return("Missing info")
                        
            if missing == 0:
                print("error")
                conn.rollback()
                return("eh ben nsml")

            else:       
                colonnes = ', '.join(medecin.model_dump().keys())
                placeholders = ', '.join('?' * len(medecin.model_dump()))
                requete = f"INSERT INTO Medecin ({colonnes}) VALUES ({placeholders})"
                cursor.execute(requete, list(medecin.model_dump().values()))
                conn.commit()
                
                return {"message": "Médecin ajouté avec succès."}
    except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))


@app.put("/modifier_medecin/{ID_Medecin_}")
def modifier_medecin(id_medecin: str, medecin: Medecin):
    """ Fonction pour modifier un médecin. """
    try:
        medecin_data = medecin.model_dump()
        del medecin_data['ID_Medecin_']  # Assuming 'ID_Medecin_' should not be updated

        clause_set = ', '.join([f"{key} = :{key}" for key in medecin_data.keys()])
        requete = f"UPDATE Medecin SET {clause_set} WHERE ID_Medecin_ = :ID_Medecin_"
        medecin_data['ID_Medecin_'] = id_medecin

        cursor.execute(requete, medecin_data)
        affected_rows = cursor.rowcount
        conn.commit()

        if affected_rows == 0:
            return {"message": "No rows updated. Check if the ID exists."}
        else:
            return {"message": f"Successfully updated {affected_rows} row(s)."}
    except Exception as e:
        return {"error": str(e)}


@app.put("/visualiser_rdv_medecin/{ID_Medecin_}")
def visualiser_rdv_medecin(id_medecin: str):
    """ Fonction pour visualiser les rendez-vous d'aujourd'hui pour un médecin. """
    try:
        date_aujourd_hui = datetime.now().strftime("%d/%m/%Y")
        requete = "SELECT * FROM RDV WHERE ID_Medecin_ = :id_medecin AND Date_RDV = :date_aujourd_hui"
        cursor.execute(requete, {'id_medecin': id_medecin, 'date_aujourd_hui': date_aujourd_hui})
        fl = cursor.fetchall()
        conn.commit()
        return fl
    
    except Exception as e:
        return {"error": str(e)}

#--------------------------------------------------------------------------------------------------------------------------------------
#patient

class Patient(BaseModel):
    Nom: str
    Prenom: str
    Date_de_naissance: str
    Sexe: str
    Adresse: str
    Numero_de_telephone: int
    Adresse_email: str
    Assurance_medicale: int
    ID_Patient: str
    ID_Compte_: str

class Compte(BaseModel):
    ID_Compte_: str
    Identifiant: str
    Mot_de_passe: str
    date_de_creation: str
    


@app.put("/cree_compte/{ID_Compte_}")
def cree_compte(compte: Compte):
    """ Fonction pour cree un compte. """
    try:
            missing = 1
            for  data in compte :
                    if  data[1] == "string" :
                      missing = 0
                      print("ahhhhhh")
                      return("Missing info")
                        
            if missing == 0:
                print("error")
                conn.rollback()
                return("eh ben nsml")

            else:       
                colonnes = ', '.join(compte.model_dump().keys())
                placeholders = ', '.join('?' * len(compte.model_dump()))
                requete = f"INSERT INTO Compte ({colonnes}) VALUES ({placeholders})"
                cursor.execute(requete, list(compte.model_dump().values()))
                conn.commit()
                
                return {"message": "Compte crée avec succès."}
    except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    

@app.post("/ajouter_patient/{ID_Patient}")
def ajouter_patient(patient: Patient):
    """ Fonction pour ajouter un patient. """
    try:
            missing = 1
            for  data in patient :
                    if  data[1] == "string" :
                      missing = 0
                      print("ahhhhhh")
                      return("Missing info")
                        
            if missing == 0:
                print("error")
                conn.rollback()
                return("eh ben nsml")

            else:       
                colonnes = ', '.join(patient.model_dump().keys())
                placeholders = ', '.join('?' * len(patient.model_dump()))
                requete = f"INSERT INTO Patient ({colonnes}) VALUES ({placeholders})"
                cursor.execute(requete, list(patient.model_dump().values()))
                conn.commit()
                
                return {"message": "Patient ajouté avec succès."}
    except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        
        

@app.put("/modifier_patient/{ID_Patient}")
def modifier_patient(id_patient: str, patient: Patient):
    """ Fonction pour modifier un patient. """
    try:
        patient_data = patient.model_dump()
        del patient_data['ID_Patient']  # Assuming 'ID_Patient' should not be updated

        clause_set = ', '.join([f"{key} = :{key}" for key in patient_data.keys()])
        requete = f"UPDATE Patient SET {clause_set} WHERE ID_Patient = :ID_patient"
        patient_data['ID_patient'] = id_patient

        cursor.execute(requete, patient_data)
        affected_rows = cursor.rowcount
        conn.commit()

        if affected_rows == 0:
            return {"message": "No rows updated. Check if the ID exists."}
        else:
            return {"message": f"Successfully updated {affected_rows} row(s)."}
    except Exception as e:
        return {"error": str(e)}
    
#--------------------------------------------------------------------------------------------------------------------------------------
@app.put("/visualiser_doss_medical_1_consultation/{ID_Patient}/{ID_Rendezvous_}")
def visualiser_doss_medical_1_consultation(id_patient: str, id_rdv: str):
    """ Fonction pour visualiser un rendez-vous et Facturation/Commentaire associés. """
    try:
        # Requête SQL pour récupérer les informations de rendez-vous du patient
        requete_rdv = "SELECT * FROM RDV WHERE ID_Patient = :id_patient AND ID_Rendezvous_ = :id_rdv"
        cursor.execute(requete_rdv, {'id_patient': id_patient, 'id_rdv': id_rdv})
        rdv_info = cursor.fetchall()

        if not rdv_info:
            return JSONResponse(content={"error": "Rendez-vous non trouvé pour le patient spécifié."})

        # Requête SQL pour récupérer les informations d'analyses médicales associées au patient
        requete_analyses = f"""
            SELECT ID_Patient, NULL AS ID_Facture_
            FROM Analyses_d_urine
            WHERE ID_Patient = '{id_patient}'

            UNION ALL

            SELECT ID_Patient, NULL AS ID_Facture_
            FROM Analyses_sanguines
            WHERE ID_Patient = '{id_patient}'

            UNION ALL

            SELECT ID_Patient, NULL AS ID_Facture_
            FROM Tests_allergologiques
            WHERE ID_Patient = '{id_patient}'

            UNION ALL

            SELECT ID_Patient, NULL AS ID_Facture_
            FROM Tests_de_depistage_maladies_infectieuses
            WHERE ID_Patient = '{id_patient}'
        """

        cursor.execute(requete_analyses, {'id_patient': id_patient})
        analyses_info = cursor.fetchall()

        # Requête SQL pour récupérer les informations de facturation associées au rendez-vous
        requete_facturation = "SELECT * FROM Facturation WHERE ID_Facture_ = :id_facture"
        id_facture = rdv_info[0]['ID_Facture_']  # Supposons que l'ID_Facture_ soit présent dans les résultats du rendez-vous
        cursor.execute(requete_facturation, {'id_facture': id_facture})
        facturation_info = cursor.fetchall()

        # Combine les résultats des trois requêtes pour la réponse JSON
        resultats = {
            "Rendez_vous": rdv_info,
            "Analyses_medicales": analyses_info,
            "Facturation": facturation_info
        }

        # Commit des modifications (assurez-vous que cela est approprié pour votre cas d'utilisation)
        conn.commit()

        # Retourne les résultats au format JSON
        return JSONResponse(content=resultats)

    except Exception as e:
        # En cas d'erreur, renvoyer une réponse JSON avec un message d'erreur
        return JSONResponse(content={"error": str(e)})
    

def visualiser_doss_medical(id_patient):
    """ Fonction pour visualiser le dossier d'un patient"""
    pass

#--------------------------------------------------------------------------------------------------------------------------------------
#receptionniste

class Receptionniste(BaseModel):
    ID_Receptionniste_: str
    Nom: str
    Prenom: str
    Horaire: str
    ID_Facture_: str
    

@app.post("/ajouter_receptionniste/{ID_Receptionniste_}")
def ajouter_receptionniste(receptionniste: Receptionniste):
    """ Fonction pour ajouter un réceptionniste. """
    try:
            missing = 1
            for  data in receptionniste :
                    if  data[1] == "string" :
                      missing = 0
                      print("ahhhhhh")
                      return("Missing info")
                        
            if missing == 0:
                print("error")
                conn.rollback()
                return("eh ben nsml")

            else:       
                colonnes = ', '.join(receptionniste.model_dump().keys())
                placeholders = ', '.join('?' * len(receptionniste.model_dump()))
                requete = f"INSERT INTO Receptionniste ({colonnes}) VALUES ({placeholders})"
                cursor.execute(requete, list(receptionniste.model_dump().values()))
                conn.commit()
                
                return {"message": "Receptionniste ajouté avec succès."}
    except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))


@app.put("/modifier_receptionniste/{ID_Receptionniste_}")
def modifier_receptionniste(id_receptionniste: str, receptionniste: Receptionniste):
    """ Fonction pour modifier un réceptionniste. """
    try:
        receptionniste_data = receptionniste.model_dump()
        del receptionniste_data['ID_Receptionniste_']  # Assuming 'ID_Receptionniste_' should not be updated

        clause_set = ', '.join([f"{key} = :{key}" for key in receptionniste_data.keys()])
        requete = f"UPDATE Receptionniste SET {clause_set} WHERE ID_Receptionniste_ = :id_receptionniste_receptionniste"
        receptionniste_data['id_receptionniste'] = id_receptionniste

        cursor.execute(requete, receptionniste_data)
        affected_rows = cursor.rowcount
        conn.commit()

        if affected_rows == 0:
            return {"message": "No rows updated. Check if the ID exists."}
        else:
            return {"message": f"Successfully updated {affected_rows} row(s)."}
    except Exception as e:
        return {"error": str(e)}
    
#--------------------------------------------------------------------------------------------------------------------------------------
def modifier_patient_receptionniste(id_receptionniste, id_patient, donnees):
    """ Fonction pour modifier un patient par un réceptionniste. """
    pass


#--------------------------------------------------------------------------------------------------------------------------------------
# sert à supprimer un médecin / patient / récéptionniste en le cherchant grâce à son id

@app.delete("/supprimer_M_P_R/{id_element}/{table}")
def supprimer_M_P_R(id_element:str, table):
    """ Fonction pour supprimer un Medecin, un Patient, ou une Receptionniste. """
    try:
        tables_autorisees = ['Medecin', 'Patient', 'Receptionniste']
        if table not in tables_autorisees:
            raise ValueError(f"La table spécifiée '{table}' n'est pas autorisée. Choisissez parmi {tables_autorisees}.")
        else : 
            if table == "Medecin":
                requete = f"DELETE FROM {table} WHERE ID_Medecin_ = :id"
                cursor.execute(requete, {'id': id_element})
                return {"message": "Medecin supprimer avec succès."}
                
            elif table == "Patient":
                requete = f"DELETE FROM {table} WHERE ID_Patient = :id"
                cursor.execute(requete, {'id': id_element})
                return {"message": "Patien supprimer avec succès."}
                
            else:
                requete = f"DELETE FROM {table} WHERE ID_Receptionniste_ = :id"
                cursor.execute(requete, {'id': id_element})
                return {"message": "Receptionniste supprimer avec succès."}
            conn.commit()
    except Exception as e:
        return {"error": str(e)}
    
#--------------------------------------------------------------------------------------------------------------------------------------
#rdv

class RDV(BaseModel):
    Date_RDV: str
    Etat: str
    Commentaires: str
    ID_Rendezvous_: str
    ID_Medecin_: str
    ID_Patient: str
    ID_Creneau_: str

class Creneau(BaseModel):
    ID_Creneau_: str
    HeureDebut: str
    HeureFin: str
    Disponibilite: str


@app.post("/ajouter_rdv/{ID_Rendezvous_}")
def ajouter_rdv(rdv: RDV):
    """ Fonction pour ajouter un rendez-vous. """
    try:
        missing = 1
        for  data in rdv :
            if  data[1] == "string" :
                missing = 0
                print("ahhhhhh")
                return("Missing info")
                        
        if missing == 0:
            print("error")
            conn.rollback()
            return("eh ben nsml")

        else:       
            colonnes = ', '.join(rdv.model_dump().keys())
            placeholders = ', '.join('?' * len(rdv.model_dump()))
            requete = f"INSERT INTO RDV ({colonnes}) VALUES ({placeholders})"
            cursor.execute(requete, list(rdv.model_dump().values()))
            conn.commit()
                
            return {"message": "Rendez-vous ajouté avec succès."}
    except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))



@app.post("/ajouter_creneau/{ID_Creneau_}")
def ajouter_creneau(creneau: Creneau):
    """ Fonction pour ajouter un creneau. """
    try:
            missing = 1
            for  data in creneau :
                    if  data[1] == "string" :
                      missing = 0
                      print("ahhhhhh")
                      return("Missing info")
                        
            if missing == 0:
                print("error")
                conn.rollback()
                return("eh ben nsml")

            else:       
                colonnes = ', '.join(creneau.model_dump().keys())
                placeholders = ', '.join('?' * len(creneau.model_dump()))
                requete = f"INSERT INTO Creneau ({colonnes}) VALUES ({placeholders})"
                cursor.execute(requete, list(creneau.model_dump().values()))
                conn.commit()
                
                return {"message": "Creneau ajouté avec succès."}
    except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))


@app.put("/modifier_etat_rdv/{ID_Rendezvous_}")        
def modifier_etat_rdv(id_rdv, nouveau_etat_rdv):
    """ Fonction pour modifier l'état d'un rendez-vous. """
    try:
        requete = "UPDATE RDV SET Etat = :etat WHERE ID_Rendezvous_ = :id_rdv"
        cursor.execute(requete, {'etat': nouveau_etat_rdv, 'id_rdv': id_rdv})
        conn.commit()
        return {"message": "Etat du rendez-vous modifié avec succès."}
    
    except Exception as e:
        return {"error": str(e)}
    
    

@app.delete("/annuler_rdv/{id_rdv}")
def annuler_rdv(id_rdv: str):
    """ Fonction pour annuler (supprimer) un rendez-vous. """
    try:
        requete = "DELETE FROM RDV WHERE ID_Rendezvous_ = :id_rdv"
        cursor.execute(requete, {'id_rdv': id_rdv})
        conn.commit()
        return {"message": "Rendez-vous supprimer avec succès."}

    except Exception as e:
        return {"error": str(e)}


    
@app.put("/visualiser_rdv/{ID_Medecin_}")
def visualiser_rdv(id_medecin):
    """ Fonction pour visualiser les rendez-vous d'un médecin. """
    try:
        requete = "SELECT * FROM RDV WHERE ID_Medecin_ = :id_medecin"
        cursor.execute(requete, {'id_medecin': id_medecin})
        fl= cursor.fetchall()
        conn.commit()
        return fl
    
    except Exception as e:
        return {"error": str(e)}

#--------------------------------------------------------------------------------------------------------------------------------------
#analyses

class Analyses_d_urine(BaseModel):
    ID_Analyses_d_urine: str
    Examen_cytobacteriologique_des_urines: str
    Analyse_de_proteines: str
    DateHeure: str
    Description: str
    Resultats: str
    ID_Medecin_: str
    ID_Patient: str
    ID_Facture_: str
    

class Analyses_sanguines(BaseModel):
    ID_Analyses_sanguines: str
    Numeration_formule_sanguine: str
    Biochimie_sanguine: str
    Test_hormonaux: str
    Marqueurs_tumoraux: str
    DateHeure: str
    Description: str
    Resultats: str
    ID_Medecin_: str
    ID_Patient: str
    ID_Facture_: str
    

class Tests_allergologiques(BaseModel):
    ID_Tests_allergologiques: str
    Tests_cutanes: str
    Tests_intradermiques: str
    Tests_sanguis: str
    Patch_tests: str
    Tests_de_provocation: str
    DateHeure: str
    Description: str
    Resultats: str
    ID_Medecin_: str
    ID_Patient: str
    ID_Facture_: str

class Tests_de_depistage_maladies_infectieuses(BaseModel):
    ID_Tests_de_depistage_maladies_infectieuses: str
    Tests_serologiques: str
    PCR:str
    Cultures: str
    Tests_d_antigenemie: str
    Tests_rapides: str
    Tests_d_immunofluorescence: str
    Tests_d_immunochromatographie: str
    DateHeure: str
    Description: str
    Resultats: str
    ID_Medecin_: str
    ID_Patient: str
    ID_Facture_: str


@app.post("/cree_Analyses_d_urine/{ID_Analyses_d_urine}")
def cree_Analyses_d_urine(urine: Analyses_d_urine):
    """ Fonction pour ajouter une analyse. """
    try:
            missing = 1
            for  data in urine :
                    if  data[1] == "string" :
                      missing = 0
                      print("ahhhhhh")
                      return("Missing info")
                        
            if missing == 0:
                print("error")
                conn.rollback()
                return("eh ben nsml")

            else:       
                colonnes = ', '.join(urine.model_dump().keys())
                placeholders = ', '.join('?' * len(urine.model_dump()))
                requete = f"INSERT INTO Analyses_d_urine ({colonnes}) VALUES ({placeholders})"
                cursor.execute(requete, list(urine.model_dump().values()))
                conn.commit()
                
                return {"message": "Analyses cree avec succès."}
    except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))



@app.post("/cree_Analyses_sanguines/{ID_Analyses_sanguines}")
def cree_Analyses_sanguines(sanguines: Analyses_sanguines):
    """ Fonction pour ajouter une analyse. """
    try:
            missing = 1
            for  data in sanguines :
                    if  data[1] == "string" :
                      missing = 0
                      print("ahhhhhh")
                      return("Missing info")
                        
            if missing == 0:
                print("error")
                conn.rollback()
                return("eh ben nsml")

            else:       
                colonnes = ', '.join(sanguines.model_dump().keys())
                placeholders = ', '.join('?' * len(sanguines.model_dump()))
                requete = f"INSERT INTO Analyses_sanguines ({colonnes}) VALUES ({placeholders})"
                cursor.execute(requete, list(sanguines.model_dump().values()))
                conn.commit()
                
                return {"message": "Analyses cree avec succès."}
    except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))


@app.post("/cree_Analyses_sanguines/{ID_Tests_allergologiques}")
def cree_Tests_allergologiques(allergologiques: Tests_allergologiques):
    """ Fonction pour ajouter une analyse. """
    try:
            missing = 1
            for  data in allergologiques :
                    if  data[1] == "string" :
                      missing = 0
                      print("ahhhhhh")
                      return("Missing info")
                        
            if missing == 0:
                print("error")
                conn.rollback()
                return("eh ben nsml")

            else:       
                colonnes = ', '.join(allergologiques.model_dump().keys())
                placeholders = ', '.join('?' * len(allergologiques.model_dump()))
                requete = f"INSERT INTO Tests_allergologiques ({colonnes}) VALUES ({placeholders})"
                cursor.execute(requete, list(allergologiques.model_dump().values()))
                conn.commit()
                
                return {"message": "Analyses cree avec succès."}
    except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))


@app.post("/cree_Analyses_sanguines/{ID_Tests_allergologiques}")
def cree_Tests_de_depistage_maladies_infectieuses(depistage: Tests_de_depistage_maladies_infectieuses):
    """ Fonction pour ajouter une analyse. """
    try:
            missing = 1
            for  data in depistage :
                    if  data[1] == "string" :
                      missing = 0
                      print("ahhhhhh")
                      return("Missing info")
                        
            if missing == 0:
                print("error")
                conn.rollback()
                return("eh ben nsml")

            else:       
                colonnes = ', '.join(depistage.model_dump().keys())
                placeholders = ', '.join('?' * len(depistage.model_dump()))
                requete = f"INSERT INTO Tests_de_depistage_maladies_infectieusess ({colonnes}) VALUES ({placeholders})"
                cursor.execute(requete, list(depistage.model_dump().values()))
                conn.commit()
                
                return {"message": "Analyses cree avec succès."}
    except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e)) 

#--------------------------------------------------------------------------------------------------------------------------------------
#facture

class Facturation(BaseModel):
    ID_Facture_: str
    Montant: float
    Date_de_facturation: str
    Statut_de_paiement: str
    Moyen_de_payement: str
    ID_Analyses_sanguines: str 
    ID_Analyses_d_urine: str
    ID_Tests_allergologiques: str
    ID_Tests_de_depistage_maladies_infectieuses: str


@app.post("/cree_facture/{ID_Facture_:}")
def cree_facture(facture: Facturation):
    """ Fonction pour cree une facture """
    try:
            missing = 1
            for  data in facture :
                    if  data[1] == "string" :
                      missing = 0
                      print("ahhhhhh")
                      return("Missing info")
                        
            if missing == 0:
                print("error")
                conn.rollback()
                return("eh ben nsml")

            else:       
                colonnes = ', '.join(facture.model_dump().keys())
                placeholders = ', '.join('?' * len(facture.model_dump()))
                requete = f"INSERT INTO Facturation ({colonnes}) VALUES ({placeholders})"
                cursor.execute(requete, list(facture.model_dump().values()))
                conn.commit()
                
                return {"message": "Facture crée avec succès."}
    except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))



@app.put("/modifier_facture/{ID_Facture_}")
def modifier_facture(id_facture: str, facture: Facturation):
    """ Fonction pour modifier un facture. """
    try:
        facture_data = facture.model_dump()
        del facture_data['ID_Facture_']  # Assuming 'ID_Facture_' should not be updated

        clause_set = ', '.join([f"{key} = :{key}" for key in facture_data.keys()])
        requete = f"UPDATE Medecin SET {clause_set} WHERE ID_Facture_ = :ID_facture"
        facture_data['ID_facture'] = id_facture

        cursor.execute(requete, facture_data)
        affected_rows = cursor.rowcount
        conn.commit()

        if affected_rows == 0:
            return {"message": "No rows updated. Check if the ID exists."}
        else:
            return {"message": f"Successfully updated {affected_rows} row(s)."}
    except Exception as e:
        return {"error": str(e)}




@app.delete("/supprimer_A_F_R/{id_element}/{table}")
def supprimer_A_F_R(id_element:str, table):
    """ Fonction pour supprimer une analyse, une facture, ou un rapport. """
    try:
        tables_autorisees = ['Tests_de_depistage_maladies_infectieuses','Analyses_d_urine','Analyses_sanguines','Tests_allergologiques', 'Facturation']
        if table not in tables_autorisees:
            raise ValueError(f"La table spécifiée '{table}' n'est pas autorisée. Choisissez parmi {tables_autorisees}.")
        else : 
            if table == "Tests_de_depistage_maladies_infectieuses":
                requete = f"DELETE FROM {table} WHERE ID_Tests_de_depistage_maladies_infectieuses = :id"
                cursor.execute(requete, {'id': id_element})
            elif table == "Analyses_d_urine":
                requete = f"DELETE FROM {table} WHERE ID_Analyses_d_urine = :id"
                cursor.execute(requete, {'id': id_element})
            elif table == "Analyses_sanguines":
                requete = f"DELETE FROM {table} WHERE ID_Analyses_sanguines = :id"
                cursor.execute(requete, {'id': id_element})
                
            elif table == "Facturation":
                requete = f"DELETE FROM {table} WHERE ID_Facture_ = :id"
                cursor.execute(requete, {'id': id_element})
                
            else:
                requete = f"DELETE FROM {table} WHERE ID_Tests_allergologiques = :id"
                cursor.execute(requete, {'id': id_element})
            conn.commit()
    except Exception as e:
        return {"error": str(e)}



@app.put("/visualiser_rdv_journee/{Date_RDV}")
def visualiser_rdv_journee(date_journee):
    try:
        requete = "SELECT * FROM RDV WHERE Date_RDV = :date_journee"
        cursor.execute(requete, {'date_journee': date_journee})
        f1 = cursor.fetchall()
        conn.commit()
        return f1

    except Exception as e:
        return {"error": str(e)}


@app.put("/reporting/{Date_debut}/{Date_fin}")
def reporting(date_debut, date_fin):
    """ Fonction pour calculer et afficher les statistiques entre deux dates. """
    try:
        requete1 = """
            SELECT COUNT(DISTINCT ID_Patient) as nombre_patients
            FROM Patient;
        """

        cursor.execute(requete1)
        resultats1 = cursor.fetchone()
        nombre_patients = resultats1[0]

        
        requete2 = """
            SELECT SUM(Montant) as recette
            FROM Facturation
            WHERE Date_de_facturation BETWEEN :date_debut AND :date_fin;
        """

        cursor.execute(requete2, {'date_debut': date_debut, 'date_fin': date_fin})
        resultats2 = cursor.fetchone()
        recette = resultats2[0]

        return {"Nombre_patients": nombre_patients, "Recette": recette}
    
    except Exception as e:
        return {"error": str(e)}
    
#--------------------------------------------------------------------------------------------------------------------------------------
#message

class Message(BaseModel):
    ID_Message_: str
    Contenu: str
    ID_Medecin_: str
    ID_Patient: str

class Replique(BaseModel):
    DateHeure: str
    ID_Replique: str
    contenu: str
    ID_Message_: str


@app.post("/ecrire_message/{ID_Message_}")
def ecrire_message(message: Message):
    """ Fonction pour qu'un patient puisse écrire un message à un médecin. """
    try:
            missing = 1
            for  data in message :
                    if  data[1] == "string" :
                      missing = 0
                      print("ahhhhhh")
                      return("Missing info")
                        
            if missing == 0:
                print("error")
                conn.rollback()
                return("eh ben nsml")

            else:       
                colonnes = ', '.join(message.model_dump().keys())
                placeholders = ', '.join('?' * len(message.model_dump()))
                requete = f"INSERT INTO Message ({colonnes}) VALUES ({placeholders})"
                cursor.execute(requete, list(message.model_dump().values()))
                conn.commit()
                
                return {"message": "Nouveau message reçu"}
    except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))



@app.post("/repondre_message/{ID_Replique}")
def repondre_message(replique: Replique):
    """ Fonction pour qu'un médecin puisse répondre à un message d'un patient. """
    try:
            missing = 1
            for  data in replique :
                    if  data[1] == "string" :
                      missing = 0
                      print("ahhhhhh")
                      return("Missing info")
                        
            if missing == 0:
                print("error")
                conn.rollback()
                return("eh ben nsml")

            else:       
                colonnes = ', '.join(replique.model_dump().keys())
                placeholders = ', '.join('?' * len(replique.model_dump()))
                requete = f"INSERT INTO Replique ({colonnes}) VALUES ({placeholders})"
                cursor.execute(requete, list(replique.model_dump().values()))
                conn.commit()
                
                return {"message": "Message envoyé"}
    except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))


@app.post("/lire_message/{ID_Medecin_}")
def lire_message(id_medecin:str):
    """ Fonction pour qu'un médecin puisse lire ses messages. """
    try:
        requete = "SELECT * FROM Message WHERE ID_Medecin_ = :id_medecin"
        cursor.execute(requete, {'id_medecin': id_medecin})
        fl = cursor.fetchall()
        conn.commit()
        return fl
    
    except Exception as e:
         return {"error": str(e)}
#modifier_patient_receptionniste - AUTRE APRES visualiser_doss_medical_1_consultation ET visualiser_doss_medical
#--------------------------------------------------------------------------------------------------------------------------------------
#Test


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


cursor.close()   
conn.close()

