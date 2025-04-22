#este codigo deberia mostrar los resultados de la clasificacion de 
#equipos de futbol pero marca un error que no he resuelto
from bs4 import BeautifulSoup
import requests
import pandas as pd

#url = 'https://success.recruitmilitary.com/jobs'
url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

#llista de equipos

eq = soup.find_all('span', class_='nombre_equipo')
#print (eq)

equipos = list()

count = 0
for i in eq:
    if count < 20:
        equipos.append(i.text)
    else:
        break
    count += 1

#print (equipos, len(equipos))
#print(equipos)


#list de puntajes

pt = soup.find_all('td', class_='destacado')
#print (eq)

puntos = list()

count = 0
for i in eq:
    if count < 20:
        puntos.append(i.text)
    else:
        break
    count += 1

##print (puntos)

df = pd.DataFrame({'Nombre' :equipos,'Puntos' :puntos}, index = list(range(1,21)))
#print(df)

df.to_csv('Clasificacion.csv', index=False)