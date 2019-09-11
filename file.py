from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib
import re
import string
try:
    html = urlopen("https://ofertadebienes.com//o_list.asp?g=1&op=0&p=0").read().decode()
    #print(html)
except HTTPError as e:
    print(e)

except URLError:
 
    print("Server down or incorrect domain")

else:
  
    res = BeautifulSoup(html, "html5lib")
    
    tags = res.findAll("div" , class_="resum")

    for tag in tags:
       
       rawtxt = re.sub(r'^\s+', '', tag.getText())
       print(rawtxt)
    


