#ranking de los 5 paises con mas desapariciones

import pandas as pd

file = 'desaparecidos.csv'
datos = pd.read_csv(file)

ranking = datos['NACIONALIDAD'].value_counts()

ranking_top_5 = ranking.head(5)
print(ranking_top_5)
