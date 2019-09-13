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
    data['item'] = []      #guardara los datos de las imagenes y mas descripcion cuando entras al link
           
    res = BeautifulSoup(html, "html5lib")
    
    itemsTags = res.findAll("div" , class_="item")
    
    for tag in itemsTags:
       
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
       linkID = linkString1[1].rsplit('">\n')

       #
       if(linkID[0]!= '2868'):
            print(linkID[0])
            urlRAW = "https://ofertadebienes.com/o_detail.asp?id={}"
            urlItem = urlRAW.format(linkID[0])      
            htmlItem = urlopen(urlItem).read().decode()
                            
            res2 = BeautifulSoup(htmlItem, "html5lib")
            itemTags = res2.findAll("div", id="detalle_bienes")
            
            for taki in itemTags:
                
                raw = taki.find("div", class_="descripcion")
                rawString = str(raw)

                #No de Finca
                noFin0 = rawString.rsplit('</strong>')
                noFin1 = noFin0[1].rsplit(': ')
                
                #Direccion
                dir0 = rawString.rsplit('Dirección:</strong> ')
                dir1 = dir0[1].rsplit(' <br/>')
                
                #Area de Construccion
                ac0 = rawString.rsplit('de:</strong> ')
                ac1 = ac0[1].rsplit('<sup>')
                
                #Tipo
                tipo0 = rawString.rsplit('<h5><strong>\n\t\t\t\t\t\t\t')
                tipo1 = tipo0[1].rsplit('\n')

                #Dimencion del Terreno
                if(tipo1[0] == 'Apartamento'):
                    dim1[0] = ' '
                else: 
                    dim0 = rawString.rsplit('Terreno:</strong> ')
                    dim1 = dim0[1].rsplit('<sup>')
                
                #Detalles
                deta0 = rawString.rsplit('Detalles:</strong> ')
                deta1 = deta0[1].rsplit('\n')
                
                #Otras Imagenes
                iraw = taki.find("ol", class_="carousel-indicators mCustomScrollbar")
                irawString = str(iraw)
                imas0 = irawString.rsplit('src="')
                i = 0
                imas2 = []
                for x in imas0:
                    imas1 = x.rsplit('"/></li>')
                    #print(imas1)
                    if (i==0):
                        print('impar')
                    else:
                        imas2.append(imas1[0])
                    i=i+1
                
                #Financiamiento Maximo
                #fm0 = rawString.rsplit('ximo: <strong>')
                #fm1 = fm0[1].rsplit('</strong>')
                                        
       #JSON
       data['property'].append({
           'ID_link':               linkID[0],
           'Description':           description.getText(),
           'Image':                 imas2,
           'Price':                 price.getText(),
           'Typo':                  tipo1[0],
           #'Financiamiento Maximo': fm1[0],
           'Details':               deta1[0],
           'Dimension':             dim1[0],
           'Area':                  ac1[0],
           'Address':               dir1[0],
           'NoFinca':               noFin1[1]
           
           
       })
           
       #print(linkID[0])    #si quieres imprimir el precio por price.getText() dentro del print

# print(data['property'])
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)
    
    


