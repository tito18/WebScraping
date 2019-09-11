from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib

try:
    html = urlopen("https://ofertadebienes.com/?utm_source=bgeneral&utm_medium=link-footer/").read().decode()
    #print(html)
except HTTPError as e:
    print(e)
else:
  
    res = BeautifulSoup(html, "html5lib")
    
    tags = res.findAll("div", {"class": "resum"})
        
    for tag in tags:
        print(tag.getText())
    #print(res.href)


