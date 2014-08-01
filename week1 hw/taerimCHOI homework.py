# -*- coding:utf-8 -*-
import urllib
from bs4 import BeautifulSoup
   

htmltext = urllib.urlopen("https://developers.google.com/appengine/").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")

authors = []

for item in soup.select(".gc-toc"):
   authors.append(item.get_text())

for author in authors:
   print author.encode('utf-8')