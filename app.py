from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib
import base64
import io
import json

try:
    html = urlopen("https://ofertadebienes.com/o_list.asp").read().decode()
    #print(html)
except HTTPError as e:
    print(e)

except URLError:
 
    print("Server down or incorrect domain")

else:

    data = {} 
    data['property'] = []
<<<<<<< HEAD:file.py
           
=======
       
>>>>>>> 69bc9dae77364fc4bb4aafeb14d46560471aa6e7:app.py
    res = BeautifulSoup(html, "html5lib")
    
    itemTags = res.findAll("div" , class_="item")
    
    for tag in itemTags:
       
       #Imagen
       imagen = tag.find("img", class_="img-thumbnail")
       imagenString = str(imagen)
       ima = imagenString.rsplit("src=""")
       ima2 = ima[1].split('/>')
       imagenURL = ima2[0].split('"')
       
       #Descripcion       
       description = tag.find("small")

       #Precio
       price = tag.find("h4")

       #Link
       linkRAW = tag.find("a", href_="")
       linkString = str(linkRAW)
<<<<<<< HEAD:file.py
       linkString1 = linkString.rsplit("href=")
       linkString2 = linkString1[1].rsplit(">\n")
       link = linkString2[0].split('"')
=======
       linkString1 = linkString.rsplit("id=")
       linkString2 = linkString1[1].rsplit('">\n')
>>>>>>> 69bc9dae77364fc4bb4aafeb14d46560471aa6e7:app.py

       #JSON
       data['property'].append({
           'ID': linkString2[0],
           'description': description.getText(),
           'image': imagenURL[1],
           'price': price.getText(),
           'link': link[1]

       })
<<<<<<< HEAD:file.py
           
       #print(link)    #si quieres imprimir el precio por price.getText() dentro del print
=======
       print("--------------------------------------")
    #    print(linkString2[0])    #si quieres imprimir el precio por price.getText() dentro del print
>>>>>>> 69bc9dae77364fc4bb4aafeb14d46560471aa6e7:app.py

# print(data['property'])
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)
    
    


