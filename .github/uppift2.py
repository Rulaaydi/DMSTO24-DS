import pandas as pd
import requests
import io
import matplotlib.pyplot as plt
import seaborn as sns

# Extract: Hämta data från API
url = "https://opendata.umea.se/api/v2/catalog/datasets/befolkningsfoeraendringar-helar/exports/csv?use_labels=true"
response = requests.get(url)

# Kontrollera om förfrågan var framgångsrik
if response.status_code == 200:
    # Läs CSV-innehållet direkt i en pandas DataFrame med rätt separator
    data_csv = pd.read_csv(io.StringIO(response.text), sep=";")  # Semikolonseparerad data
    # Ta bort eventuella mellanslag från kolumnnamnen
    data_csv.columns = data_csv.columns.str.strip()

    # Kontrollera de exakta kolumnnamnen
    print("Kolumnnamn:", data_csv.columns)

    # Försök att skapa en ny kolumn 'total_befolkning' om de korrekta kolumnnamnen finns
    if 'folkmängd' in data_csv.columns and 'födelseöverskott' in data_csv.columns:
        data_csv['total_befolkning'] = data_csv['folkmängd'] + data_csv['födelseöverskott']
        print("Data med total befolkning:\n", data_csv.head())
    else:
        print("Kolumnerna 'folkmängd' och 'födelseöverskott' finns inte i datan.")
else:
    print(f"Fel vid hämtning: {response.status_code}")

# ============================
# Load: Exportera till Excel
# ============================
excel_file = 'bearbetad_befolkningsdata.xlsx'
data_csv.to_excel(excel_file, index=False)
print(f"Data exporterad till {excel_file}")

# ============================
# Exploratory Data Analysis (EDA)
# ============================

# 1. Histogram: För att visa fördelningen av folkmängd
plt.figure(figsize=(8, 6))
sns.histplot(data_csv['folkmängd'], bins=20, kde=True, color='skyblue')
plt.title('Histogram för Folkmängd')
plt.xlabel('Folkmängd')
plt.ylabel('Frekvens')
plt.show()

# 2. Linjediagram: För att visa trender över tid för folkmängd
plt.figure(figsize=(10, 6))
sns.lineplot(data=data_csv, x='år', y='folkmängd', marker='o', color='green')
plt.title('Trend av Folkmängd över Tid')
plt.xlabel('År')
plt.ylabel('Folkmängd')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 3. Scatter plot: För att visa relation mellan folkmängd och födelseöverskott
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data_csv, x='folkmängd', y='födelseöverskott', color='red')
plt.title('Scatter plot: Folkmängd vs Födelseöverskott')
plt.xlabel('Folkmängd')
plt.ylabel('Födelseöverskott')
plt.show()

# Slutsatser från EDA
# 1. **Histogram**: Fördelningen av folkmängden visar en viss koncentration kring vissa värden, vilket kan indikera vissa stabila befolkningsområden.
# 2. **Linjediagram**: Folkmängden har haft en ökande trend över tiden, men det finns tydliga variationer som kan förklaras av olika faktorer.
# 3. **Scatter plot**: Det verkar finnas ett positivt samband mellan folkmängd och födelseöverskott, där större folkmängder tenderar att ha högre födelseöverskott.

