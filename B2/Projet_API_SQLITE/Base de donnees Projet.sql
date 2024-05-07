create table Analyses_d_urine (
     ID_Analyses_d_urine not null,
     Examen_cytobacteriologique_des_urines varchar(50) not null,
     Analyse_de_proteines varchar(50) not null,
     DateHeure date not null,
     Description varchar(50) not null,
     Resultats varchar(50) not null,
     ID_Medecin_ numeric(10,0) not null,
     ID_Patient varchar(20) not null,
     ID_Facture_ varchar(20) not null,
	 foreign key (ID_Medecin_) references Medecin,
	 foreign key (ID_Patient) references Patient,
	 foreign key (ID_Facture_) references Facturation,
     constraint ID_Analyses_d_urine_ID primary key (ID_Analyses_d_urine));
	 

create table Analyses_sanguines (
     ID_Analyses_sanguines numeric(10,0) not null,
     Numeration_formule_sanguine varchar(50) not null,
     Biochimie_sanguine varchar(50) not null,
     Tests_hormonaux varchar(50) not null,
     Marqueurs_tumoraux varchar(50) not null,
     DateHeure date not null,
     Description varchar(50) not null,
     Resultats varchar(50) not null,
     ID_Medecin_ numeric(10,0) not null,
     ID_Patient varchar(50) not null,
     ID_Facture_ varchar(50) not null,
	 foreign key (ID_Medecin_) references Medecin,
	 foreign key (ID_Patient) references Patient,
	 foreign key (ID_Facture_) references Facturation,
     constraint ID_Analyses_sanguines_ID primary key (ID_Analyses_sanguines));
	 
	 
create table Compte (
     ID_Compte_ varchar(50) not null,
     Identifiant varchar(50) not null,
     Mot_de_passe varchar(20) not null,
     Date_de_creation date not null,
     constraint ID_Compte_ID primary key (ID_Compte_));

create table Creneau (
     ID_Creneau_ not null,
     HeureDebut date not null,
     HeureFin date not null,
     Disponibilite date not null,
     constraint ID_Creneau_ID primary key (ID_Creneau_));

create table Facturation (
     ID_Facture_ varchar(20) not null,
     Montant numeric(10,0) not null,
     Date_de_facturation date not null,
     Statut_de_paiement varchar(20) not null,
     Moyen_de_payement varchar(20) not null,
     ID_Analyses_sanguines numeric(10,0),
     ID_Analyses_d_urine numeric(10,0),
     ID_Tests_allergologiques numeric(10,0),
     ID_Tests_de_depistage_maladies_infectieuses numeric(10,0),
     constraint ID_Facturation_ID primary key (ID_Facture_),
     foreign key (ID_Analyses_sanguines) references Analyses_sanguines(ID_Analyses_sanguines),
     foreign key (ID_Analyses_d_urine) references Analyses_d_urine(ID_Analyses_d_urine),
     foreign key (ID_Tests_allergologiques) references Tests_allergologiques(ID_Tests_allergologiques),
     foreign key (ID_Tests_de_depistage_maladies_infectieuses) references Tests_de_depistage_maladies_infectieuses(ID_Tests_de_depistage_maladies_infectieuses)
);

	 

create table Gere_et_Aide (
     ID_Compte_ varchar(20) not null,
     ID_Receptionniste_ varchar(20) not null,
     Traitement__regle_usage varchar(20) not null,
     Date_GA date not null,
	 foreign key (ID_Receptionniste_) references Receptionniste,
     foreign key (ID_Compte_) references Compte,
     constraint ID_Gere_et_Aide_ID primary key (ID_Receptionniste_, ID_Compte_));
	 

create table Message (
     ID_Message_ numeric(10,0) not null,
     Contenu varchar(255) not null,
     ID_Medecin_ numeric(10,0) not null,
     ID_Patient varchar(20) not null,
	 foreign key (ID_Medecin_) references Medecin,
     foreign key (ID_Patient) references Patient,
     constraint ID_Message_ID primary key (ID_Message_));
	 

create table Medecin (
     Nom varchar(50) not null,
     Prenom varchar(50) not null,
     Specialite varchar(50) not null,
     Diplome varchar(50) not null,
     Age numeric(5,0) not null,
     sexe varchar(50) not null,
     Experience varchar(50) not null,
     Horaire date not null,
     Poste varchar(50) not null,
     ID_Medecin_ numeric(10,0) not null,
     constraint ID_Medecin_ID primary key (ID_Medecin_));

create table Organiser_ (
     ID_Rendezvous_ numeric(10,0) not null,
     ID_Receptionniste_ varchar(20) not null,
     Traitement__regle_usage varchar(20) not null,
     Date date not null,
	 foreign key (ID_Receptionniste_) references Receptionniste,
     foreign key (ID_Rendezvous_) references RDV,
     constraint ID_Organiser__ID primary key (ID_Receptionniste_, ID_Rendezvous_));
	 

create table Patient (
     Nom varchar(50) not null,
     Prenom varchar(50) not null,
     Date_de_naissance date not null,
     Sexe varchar(1) not null,
     Adresse varchar(50) not null,
     Numero_de_telephone varchar(20) not null,
     Adresse_email varchar(50) not null,
     Assurance_medicale numeric(10,0) not null,
     ID_Patient varchar(20) not null,
     ID_Compte_ varchar(20) not null,
	 foreign key (ID_Compte_) references Compte,
     constraint ID_Patient_ID primary key (ID_Patient));
	 

create table RDV (
     Date_RDV date not null,
     Etat varchar(20) not null,
     Commentaires varchar(255) not null,
     ID_Rendezvous_ numeric(10,0) not null,
     ID_Medecin_ numeric(10,0) not null,
     ID_Patient varchar(20) not null,
     ID_Creneau_ numeric(10,0) not null,
	 foreign key (ID_Medecin_) references Medecin,
     foreign key (ID_Patient) references Patient,
     foreign key (ID_Creneau_) references Creneau,
     constraint ID_RDV_ID primary key (ID_Rendezvous_));
	 

create table Replique (
     DateHeure date not null,
     ID_Replique numeric(10,0) not null,
     Contenu varchar(255) not null,
     ID_Message_ numeric(10,0) not null,
	 foreign key (ID_Message_) references Message,
     constraint ID_Replique_ID primary key (ID_Replique));
	 

create table Receptionniste (
     ID_Receptionniste_ varchar(20) not null,
     Nom varchar(20) not null,
     Prenom varchar(20) not null,
     Horaire date not null,
     ID_Facture_ varchar(20) not null,
	 foreign key (ID_Facture_) references Facturation,
     constraint ID_Receptionniste_ID primary key (ID_Receptionniste_));
	 

create table Tests_allergologiques (
     ID_Tests_allergologiques numeric(10,0) not null,
     Tests_cutanes varchar(50) not null,
     Tests_intradermiques varchar(50) not null,
     Tests_sanguins varchar(50) not null,
     Patch_tests varchar(50) not null,
     Tests_de_provocation varchar(50) not null,
     DateHeure date not null,
     Description varchar(50) not null,
     Resultats varchar(50) not null,
     ID_Medecin_ numeric(10,0) not null,
     ID_Patient varchar(50) not null,
     ID_Facture_ varchar(50) not null,
	 foreign key (ID_Medecin_) references Medecin,
     foreign key (ID_Patient) references Patient,
     foreign key (ID_Facture_) references Facturation,
     constraint ID_Tests_allergologiques_ID primary key (ID_Tests_allergologiques));
	 

create table Tests_de_depistage_maladies_infectieuses (
     ID_Tests_de_depistage_maladies_infectieuses numeric(10,0) not null,
     Tests_serologiques varchar(50) not null,
     PCR varchar(50) not null,
     Cultures varchar(50) not null,
     Tests_d_antigenemie varchar(50) not null,
     Tests_rapides varchar(50) not null,
     Tests_d_immunofluorescence varchar(50) not null,
     Tests_d_immunochromatographie varchar(50) not null,
     DateHeure date not null,
     Description varchar(50) not null,
     Resultats varchar(50) not null,
     ID_Medecin_ numeric(10,0) not null,
     ID_Patient varchar(50) not null,
     ID_Facture_ varchar(50) not null,
	 foreign key (ID_Medecin_) references Medecin,
     foreign key (ID_Patient) references Patient,
     foreign key (ID_Facture_) references Facturation,
     constraint ID_Tests_de_depistage_maladies_infectieuses_ID primary key (ID_Tests_de_depistage_maladies_infectieuses));
	 
 
	 
create unique index ID_Analyses_d_urine_IND
     on Analyses_d_urine (ID_Analyses_d_urine);

create index REF_Analy_Medec_1_IND
     on Analyses_d_urine (ID_Medecin_);

create index REF_Analy_Patie_1_IND
     on Analyses_d_urine (ID_Patient);

create index EQU_Analy_Factu_1_IND
     on Analyses_d_urine (ID_Facture_);

create unique index ID_Analyses_sanguines_IND
     on Analyses_sanguines (ID_Analyses_sanguines);

create index REF_Analy_Medec_IND
     on Analyses_sanguines (ID_Medecin_);

create index REF_Analy_Patie_IND
     on Analyses_sanguines (ID_Patient);

create index EQU_Analy_Factu_IND
     on Analyses_sanguines (ID_Facture_);

create unique index ID_Compte_IND
     on Compte (ID_Compte_);

create unique index ID_Creneau_IND
     on Creneau (ID_Creneau_);

create unique index ID_Facturation_IND
     on Facturation (ID_Facture_);

create unique index ID_Gere_et_Aide_IND
     on Gere_et_Aide (ID_Receptionniste_, ID_Compte_);

create index REF_Gere__Compt_IND
     on Gere_et_Aide (ID_Compte_);

create unique index ID_Message_IND
     on Message (ID_Message_);

create index REF_Messa_Medec_IND
     on Message (ID_Medecin_);

create index REF_Messa_Patie_IND
     on Message (ID_Patient);

create unique index ID_Medecin_IND
     on Medecin (ID_Medecin_);

create unique index ID_Organiser__IND
     on Organiser_ (ID_Receptionniste_, ID_Rendezvous_);

create index REF_Organ_RDV_IND
     on Organiser_ (ID_Rendezvous_);

create unique index ID_Patient_IND
     on Patient (ID_Patient);

create index REF_Patie_Compt_IND
     on Patient (ID_Compte_);

create unique index ID_RDV_IND
     on RDV (ID_Rendezvous_);

create index REF_RDV_Medec_IND
     on RDV (ID_Medecin_);

create index REF_RDV_Patie_IND
     on RDV (ID_Patient);

create index REF_RDV_Crene_IND
     on RDV (ID_Creneau_);

create unique index ID_Replique_IND
     on Replique (ID_Replique);

create index REF_Repli_Messa_IND
     on Replique (ID_Message_);

create unique index ID_Receptionniste_IND
     on Receptionniste (ID_Receptionniste_);

create index REF_Recep_Factu_IND
     on Receptionniste (ID_Facture_);

create unique index ID_Tests_allergologiques_IND
     on Tests_allergologiques (ID_Tests_allergologiques);

create index REF_Tests_Medec_1_IND
     on Tests_allergologiques (ID_Medecin_);

create index REF_Tests_Patie_1_IND
     on Tests_allergologiques (ID_Patient);

create index EQU_Tests_Factu_1_IND
     on Tests_allergologiques (ID_Facture_);

create unique index ID_Tests_de_depistage_maladies_infectieuses_IND
     on Tests_de_depistage_maladies_infectieuses (ID_Tests_de_depistage_maladies_infectieuses);

create index REF_Tests_Medec_IND
     on Tests_de_depistage_maladies_infectieuses (ID_Medecin_);

create index REF_Tests_Patie_IND
     on Tests_de_depistage_maladies_infectieuses (ID_Patient);

create index EQU_Tests_Factu_IND
     on Tests_de_depistage_maladies_infectieuses (ID_Facture_);

