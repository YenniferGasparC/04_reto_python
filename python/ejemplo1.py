#ranking de edad de edad con mas desapariciones

import pandas as pd

file = 'desaparecidos.csv'
datos = pd.read_csv(file)

ranking = datos['RANGO_EDAD'].value_counts()

ranking_top_5 = ranking.head(5)
print(ranking_top_5)

