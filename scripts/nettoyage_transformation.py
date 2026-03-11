import pandas as pd

df = pd.read_csv("../data/processed/dataset_anonymized.csv")

# Remplacement des valeurs manquantes(valeurs nulles) par la médiane
colonnes_a_corriger = ['PanierMoyen', 'MontantTotalAchats', 'FréquenceAchatMensuel']

for col in colonnes_a_corriger:
    
    # remplace les valeurs nulles si et seulement si nombre d achats n est pas nul
    df.loc[(df['NombreAchats'] > 0) & (df[col] == 0), col] = pd.NA
    
    # remplace par la médiane
    df[col] = df[col].fillna(df[col].median())

# Conversion en format datetime
df['DateNaissance'] = pd.to_datetime(df['DateNaissance'], errors='coerce')
df['DernierAchat'] = pd.to_datetime(df['DernierAchat'], errors='coerce')
df['DateExpirationCarte'] = pd.to_datetime(
    df['DateExpirationCarte'], 
    format='%m/%y',         
    errors='coerce'
)

# Format YYYY-MM-DD
df['DateNaissance'] = df['DateNaissance'].dt.strftime('%Y-%m-%d')
df['DernierAchat'] = df['DernierAchat'].dt.strftime('%Y-%m-%d')
df['DateExpirationCarte'] = df['DateExpirationCarte'] + pd.offsets.MonthEnd(0)


# Suppression des doublons
df = df.drop_duplicates()


# Création colonne revenu moyen par client
df['RevenuMoyenClient'] = df['MontantTotalAchats'] / df['NombreAchats'].replace(0, 1)

# Montant total dépensé par client
df['TotalDepense'] = df['NombreAchats'] * df['PanierMoyen']

# Client actif (>5 achats par mois)
df['ClientPlusAchat'] = df['FréquenceAchatMensuel'] > 5


# Supression des valeurs aberrantes
mean = df['MontantTotalAchats'].mean()
std = df['MontantTotalAchats'].std()

df['AnomalieTransaction'] = df['MontantTotalAchats'] > (mean + 3 * std)


# Vérification finale
print("\nDataset après nettoyage :")
print(df.info())

print("\nAperçu des données :")
print(df.head())


