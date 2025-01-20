

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Skapa exempeldata
data = {
    'Tid': [1, 2, 3, 4, 5, 6],
    'Värde': [2, 3, 5, 7, 11, 13]
}
# Omvandla till en pandas DataFrame
df = pd.DataFrame(data)
# Skapa en linjediagram med Matplotlib
plt.plot(df['Tid'], df['Värde'], label='Värde över tid')
plt.title('Exempel på linjediagram')
plt.xlabel('Tid')
plt.ylabel('Värde')
plt.legend()
plt.show()
# Skapa en annan visualisering med Seaborn (enkel linjeplot)
sns.lineplot(data=df, x='Tid', y='Värde')
plt.title('Seaborn linjediagram')
plt.show()

import matplotlib.pyplot as plt
# Exempeldata
labels = ['Äpplen', 'Bananer', 'Körsbär', 'Druvor']
sizes = [25, 35, 15, 25]  # Mängden av varje frukt
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Färger för varje kategori
# Skapa ett cirkeldiagram
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
# Skapa en cirkel för att göra diagrammet rundare
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# Lägg till titel
plt.title('Fördelning av frukter')
# Visa diagrammet
plt.axis('equal')  # Gör så att cirkeln är rund (inte oval)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
# Definiera koordinater för triangeln
x = np.array([0, 1, 2])
y = np.array([0, 2, 0])
# Skapa en figur och en axel
fig, ax = plt.subplots()
# Plotta triangeln genom att ansluta punkterna
ax.plot(np.append(x, x[0]), np.append(y, y[0]), 'b-', label="Triangel")
# Plotta punkterna
ax.scatter(x, y, color='red')
# Lägg till etiketter för punkterna
for i, txt in enumerate(['Punkt A', 'Punkt B', 'Punkt C']):
    ax.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')
# Sätt titel och etiketter
ax.set_title('Triangeldiagram')
ax.set_xlabel('X-axel')
ax.set_ylabel('Y-axel')
# Visa diagrammet
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')  # Gör så att triangeln ser korrekt ut
plt.legend()
plt.show()


import pandas as pd
# Steg 1: Läs in data från två olika CSV-filer
sales_df = pd.read_csv('sales_2025.csv')
customers_df = pd.read_csv('customers.csv')
# Steg 2: Hantera saknade värden
# Fyller saknade värden i 'Sales' med 0
sales_df['Sales'].fillna(0, inplace=True)
# Skapa en ny kolumn Total_Sales i sales_df (om den inte finns redan)
sales_df['Total_Sales'] = sales_df['Sales']
# Steg 3: Kombinera data baserat på gemensam kolumn CustomerID
merged_df = pd.merge(sales_df, customers_df, on='CustomerID', how='inner')
# Steg 4: Spara den transformerade datan i en ny CSV-fil
merged_df.to_csv('transformed_sales_customers.csv', index=False)
print("ETL-processen har slutförts och filen 'transformed_sales_customers.csv' har skapats.")



