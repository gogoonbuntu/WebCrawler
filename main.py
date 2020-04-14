from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://hisnet.handong.edu/myboard/list.php?Board=ONECLICK")  

bsObject = BeautifulSoup(html, "html.parser") 


print(list(bsObject))