from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib
import base64
from PIL import Image
import io


try:
    html = urlopen("https://ofertadebienes.com//o_list.asp?g=1&op=0&p=0").read().decode()
    #print(html)
except HTTPError as e:
    print(e)

except URLError:
 
    print("Server down or incorrect domain")

else:
  
    res = BeautifulSoup(html, "html5lib")
    
    itemTags = res.findAll("div" , class_="item")
    
    for tag in itemTags:
       
       imagen = tag.find("img", class_="img-thumbnail")
       description = tag.find("small")
       price = tag.find("h4")
       print(imagen)    #si quieres imprimir el precio por price.getText() dentro del print
    
    


