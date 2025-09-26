import pandas as pd

file = 'Desaparecidas.csv'

df = pd.read_csv(file)

print("TOTAL DE DEPARTAMENTOS")

print(df['DPTO_HECHO'].value_counts())

print("\nMostrar provincias de CUSCO:")
print(df[df['DPTO_HECHO'] == 'CUSCO']) & (df['PROV_HECHO'])


print("TOTAL DE PERSONAS DESAPARECIDAS")


ranking = df['MES'].value_counts()

ranking_top_5 = ranking.head(12)
print(ranking_top_5)