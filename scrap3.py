#MARCA UN ERROR en libreria o direccion chrome

#Paso 1. Buscar URL que se desea "raspar"

#Paso 2. Inspección de la página
#Los datos suelen estar anidados en etiquetas.Clic derecho "inspeccionar"

#Paso 3. Buscar los datos que se desean extraer.
#en este ejemplo se va a extraer: precio, nombre y calificación, encontradas en la etiqueta "div"

#Paso 4. Escribir código Python



#importar bibliotecas necesarias
from selenium import webdriver
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import pandas as pd

##configuracion de webdriver, para usar en Chrome
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

#Código para abrir la URL:
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")

#extraccion de datos en los div

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 

#Paso 5. Ejecutar el codigo

#https://www.edureka.co/blog/web-scraping-with-python/

