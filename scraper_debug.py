#!/usr/bin/env python3

import pandas as pd
from requests import get
from bs4 import BeautifulSoup

urllist = ['https://nostarch.com/catalog.htm', 'https://nostarch.com/catalog.htm', 'https://nostarch.com/catalog/art-photography-design', 'https://nostarch.com/catalog/general-computing', 'https://nostarch.com/catalog/security', 'https://nostarch.com/catalog/hardware-and-diy', 'https://nostarch.com/catalog/kids', 'https://nostarch.com/catalog/lego', 'https://nostarch.com/catalog/linux-bsd-unix', 'https://nostarch.com/catalog/manga', 'https://nostarch.com/catalog/programming', 'https://nostarch.com/catalog/python', 'https://nostarch.com/catalog/science-math', 'https://nostarch.com/catalog/scratch', 'https://nostarch.com/catalog/system-administration', 'https://nostarch.com/catalog/early-access']


url = 'https://nostarch.com/catalog/programming'

content = get(url).content
bs_obj = BeautifulSoup(content, "lxml")

# # title
# titles = bs_obj.find_all('div', class_='product-title')
# for title in titles:
#     print(title.text)

# # subtitle
# subtitles = bs_obj.find_all('div', class_='product-subtitle')
# for sub in subtitles:
#     print(sub.text)

# # author
# authors = bs_obj.find_all('div', class_='product-author')
# for author in authors:
#     print(str(author.text).replace('By ', ''))

# # price
# prices = bs_obj.find_all('span', class_='uc-price')
# for price in prices:
#     print(price.text)

# item box
item_box = bs_obj.find_all(
    'div', class_='col-xs-6 col-sm-6 col-md-6 col-lg-6 with-padding-bottom nostrach-views-row')
for item in item_box:
    print(item.text)

booklist = []

for item in item_box:

    try:
        title = item.find('div', class_='product-title').text
        subtitle = item.find('div', class_='product-subtitle').text
        author = item.find('div', class_='product-author').text
        price = item.find('span', class_='uc-price').text

        book_data = [title, subtitle, author, price]
        print(book_data)
        booklist.append(book_data)
    except:
        print('missing item!')
        pass

book_df = pd.DataFrame(booklist)
book_df.to_csv('programming.csv')
