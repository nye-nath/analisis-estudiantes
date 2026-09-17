import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("StudentsPerformance.csv")

# Crear una columna de promedio general
df['promedio'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

print("--- Resumen Estadistico ---")
print(df.describe())

# Generar y guardar un grafico sencillo
plt.figure(figsize=(8, 5))
df['promedio'].hist(bins=10, color='skyblue', edgecolor='black')
plt.title('Distribucion de Promedios')
plt.xlabel('Promedio')
plt.ylabel('Estudiantes')
plt.savefig('distribucion.png')
print("\nGrafico guardado correctamente como distribucion.png")
