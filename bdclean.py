#este funciono en Jupyter para seleccionar las columnas "city, occupation", "state"
#guarda la "consulta" en formato csv
import seaborn as sns


from seaborn import load_dataset
#df = load_dataset("tips")
#df.head(10)


import pandas as pd
file = 'bd_clean_1.csv'
data = pd.read_csv(file)
data.head()
#print (data)


data.loc[:, ['city', 'occupation', 'state']] # Columnas city, occupation y state

#guarda el archivo a cvs, el mismo archivo
#data.reset_index().to_csv('bdwork.csv')

data = pd.DataFrame(data.loc[:, ['city', 'occupation', 'state']])
data.reset_index().to_csv('bdwork.csv')