#cantidad de desapariciones por nacionalidad

import pandas as pd

datos = pd.read_csv('desaparecidos.csv')

cantidad_provincia = datos.groupby('NACIONALIDAD')['CANTIDAD'].sum()

print(cantidad_provincia)

