from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib
import base64
from PIL import Image
import io
import string
import json

try:
    html = urlopen("https://ofertadebienes.com//o_list.asp?g=1&op=0&p=0").read().decode()
    #print(html)
except HTTPError as e:
    print(e)

except URLError:
 
    print("Server down or incorrect domain")

else:

    data = {} 
    data['property'] = []
    data['property'].append({
        'description': ' ',
        'image': ' ',
        'price': ' '
    })
       
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

       #JSON
       data['property'].append({
           'description': description.getText(),
           'image': imagenURL[1],
           'price': price.getText()
       })
           
       #print(imagenURL[0])    #si quieres imprimir el precio por price.getText() dentro del print

print(data['property'])
#with open('data.json', 'w') as json_file:
    #json.dump(data, json_file)
    
    


