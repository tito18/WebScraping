from urllib.request import urlopen
from bs4 import BeautifulSoup
import motor.motor_asyncio
import html5lib
import base64
import io
import json
import asyncio
import aiohttp

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://test:test@cyberia-wexns.mongodb.net/test?retryWrites=true&w=majority")
db = client.webscraping_db
collection = db.oferta


# n_count = collection.find().count()
# print(n_count)

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
       linkString1 = linkString.rsplit("id=")
       linkString2 = linkString1[1].rsplit('">\n')

       #JSON
       data['property'].append({
           'ID_link': linkString2[0],
           'description': description.getText(),
           'image': imagenURL[1],
           'price': price.getText()
       })
    #    print("--------------------------------------")
    #    print(linkString2[0])    #si quieres imprimir el precio por price.getText() dentro del print

# counter = 1
async def pushData():
    result = await collection.insert_many(
        [item for item in data['property']])
    print('inserted %d docs' % (len(result.inserted_ids),))
    

loop = asyncio.get_event_loop()
loop.run_until_complete(pushData())
# loop.close()


# for i in data['property']:
#     print(i)


# with open('data.json', 'w') as json_file:
#     json.dump(data, json_file)


