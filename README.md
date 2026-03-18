Description du projet
Ce projet met en place un pipeline de traitement de données pour un dataset e-commerce anonymisé.
L’objectif est de construire un flux automatisé de nettoyage et transformation des données en combinant :
Analyse exploratoire dans Jupyter Notebook
Scripts Python pour la transformation
Orchestration du pipeline avec Apache NiFi
Le pipeline lit un fichier CSV contenant des données clients, applique plusieurs transformations, puis génère un fichier nettoyé prêt pour l’analyse ou le stockage.

Architecture du projet
Le projet suit les étapes suivantes :
Exploration des données dans Jupyter
Anonymisation des données sensibles
Création d’un script de nettoyage et transformation
Automatisation du pipeline avec Apache NiFi

Étape 1 – Exploration des données (Jupyter)
Une analyse exploratoire a été réalisée dans Jupyter Notebook afin de :
comprendre la structure du dataset
identifier les valeurs manquantes
analyser les distributions des variables
détecter les anomalies ou incohérences
Cette étape a permis de définir les transformations nécessaires pour le nettoyage des données.
Étape 2 – Anonymisation des données
Un script Python a été créé pour anonymiser les données sensibles.
Fichier :
scripts/anonymisation.py
Ce script permet notamment de :
anonymiser les identifiants clients
masquer les informations personnelles
produire un fichier anonymisé :
dataset_anonymized.csv
Ce fichier est stocké dans :
data/processed/
Étape 3 – Nettoyage et transformation des données
Un second script Python a été développé pour nettoyer et enrichir les données.
Fichier :
scripts/nettoyage_transformation.py
Transformations appliquées :
Gestion des valeurs manquantes
Les colonnes suivantes sont corrigées :
PanierMoyen
MontantTotalAchats
FréquenceAchatMensuel
Les valeurs nulles sont remplacées par la médiane de la colonne.
Conversion des dates
Les colonnes suivantes sont converties au format standard :
DateNaissance
DernierAchat
DateExpirationCarte
Format final :
YYYY-MM-DD
Suppression des doublons
Les lignes dupliquées sont supprimées afin d’éviter les biais analytiques.
Création de nouvelles variables
Plusieurs variables analytiques sont créées :
Revenu moyen par client
RevenuMoyenClient = MontantTotalAchats / NombreAchats
Total dépensé
TotalDepense = NombreAchats * PanierMoyen
Indicateur de client actif
ClientPlusAchat = FréquenceAchatMensuel > 5
Détection d’anomalies
Les transactions anormalement élevées sont détectées avec la règle :
MontantTotalAchats > moyenne + 3 * écart-type
Une colonne est créée :
AnomalieTransaction
Étape 4 – Automatisation avec Apache NiFi
Le pipeline de traitement est automatisé avec Apache NiFi.
Le flux utilise les processors suivants :
GetFile
   ↓
ExecuteStreamCommand
   ↓
UpdateAttribute
   ↓
PutFile
Description des processors
GetFile
Lit les fichiers CSV dans :
data/processed/
Filtre utilisé :
dataset_anonymized.csv
ExecuteStreamCommand
Exécute le script Python :
scripts/nettoyage_transformation.py
Le script lit le fichier anonymisé, applique les transformations et renvoie le dataset nettoyé.
UpdateAttribute
Renomme le fichier généré :
dataset_cleaned.csv
PutFile
Sauvegarde le fichier nettoyé dans :
data/output/
Export du pipeline NiFi
Le pipeline NiFi a été exporté depuis l’interface NiFi avec :
Download Flow Definition
Le fichier exporté est :
nifi/flow-definition.json
Ce fichier permet de recréer le pipeline dans Apache NiFi.

Dashboard Pwer BI

Visuels inclus:
Tendances des achats en fonction du temps (Line Chart): cela montre l'évolution des achats clients en fonction du montant total des achats par mois

Répartition des ventes par produits (Camembert): cela montre la part de chaque produit sur le montant total d'achat des produits
