import pandas as pd

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('educacion.csv')

# Muestra las primeras 5 filas
print(df.head())

# Muestra la información general del DataFrame
print(df.info())

# Muestra las estadísticas descriptivas de las columnas numéricas
print(df.describe())

print(df['Nivel_Educativo'].value_counts())


print(df['Carrera'].value_counts().idxmax())


print(df['Institución'].value_counts().idxmax())


df_posgrado = df[df['Nivel_Educativo'] == 'Posgrado']
print(df_posgrado)


df_ingenieria_madrid = df[(df['Carrera'] == 'Ingeniería Informática') & 
                          (df['Institución'] == 'Universidad Complutense de Madrid')]
print(df_ingenieria_madrid)


df_honduras_universitario = df[(df['País'] == 'Honduras') & 
                               (df['Nivel_Educativo'] == 'Universitario')]
print(df_honduras_universitario)


print(pd.crosstab(df['País'], df['Nivel_Educativo']))


print(df.groupby('Nivel_Educativo')['Edad'].mean())

df_posgrado.to_csv('posgrado.csv', index=False)
