import pandas as pd
import hashlib

df = pd.read_csv("../data/raw/dataset_projet_ecommerce.csv")

# Creation de l'id pour chaque client
df['client_id'] = df['ClientID'].astype('category').cat.codes

# Création des pseudos à partir de cet ID
df['Nom'] = 'Client_' + df['client_id'].astype(str)

# On crée le mapping en associant l'id du client a son nom et prenom
client_mapping = df[['client_id', 'ClientID']].drop_duplicates()

# Exporter du fichier mapping
client_mapping.to_csv("../data/processed/client_mapping.csv", index=False)

# Agrégation des âges en tranches
bins = [0, 30, 40, 50, 60, 100]
labels = ['18-30', '31-40', '41-50', '51-60', '60+']
df['age_group'] = pd.cut(df['Âge'], bins=bins, labels=labels)

# Pseudonymisation des emails par hash et suppression de l'email original
df['email_hash'] = df['Email'].apply(lambda x: hashlib.sha256(x.encode()).hexdigest())
df = df.drop(columns=['Email'])

# 4. Supprimer les informations sensibles
df = df.drop(columns=['NuméroCarteCrédit', 'Adresse', 'Téléphone'])

# Vérifier le résultat
print(df.head())

# Export du CSV pour Power BI ou NiFi
df.to_csv("../data/processed/dataset_anonymized.csv", index=False)
