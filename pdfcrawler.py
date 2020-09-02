from urllib.request import urlopen
import re
import pdfkit
from bs4 import BeautifulSoup
import sys



site=urlopen("https://www.deeplearningbook.org/")
soup=BeautifulSoup(site)

links=[]

for link in soup.find_all('a'):
    if link.get('href').find('content')==0:
        links.append("https://www.deeplearningbook.org/" + link.get('href'))


for page in links:
    pdfkit.from_url(page, 'test.pdf')
