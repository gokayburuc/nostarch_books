#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs
from requests import get 
from pprint import pprint
from urllib.parse import urljoin

url ='https://nostarch.com/catalog/programming'

content = get(url).content
bs_obj = bs(content,'lxml')

#catalog links 
catalog_links = [urljoin(url,a['href']) for a in bs_obj.find_all('a', href =True) if str(a).find('catalog') != -1 ]

pprint(catalog_links)

import csv
import json 

with open('weblinks.csv','w') as wf:
	for i in catalog_links:
		print(i, file = wf)