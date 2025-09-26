import pandas as pd

file = 'Desaparecidas.csv'

df = pd.read_csv(file)

print("primeras filas del archivo")
print(df.head())