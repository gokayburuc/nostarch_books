#!/usr/bin/env python3

import pandas as pd
from requests import get
from bs4 import BeautifulSoup
from time import sleep


urllist = ['https://nostarch.com/catalog/art-photography-design', 'https://nostarch.com/catalog/general-computing', 'https://nostarch.com/catalog/security', 'https://nostarch.com/catalog/hardware-and-diy', 'https://nostarch.com/catalog/kids', 'https://nostarch.com/catalog/lego', 'https://nostarch.com/catalog/linux-bsd-unix', 'https://nostarch.com/catalog/manga', 'https://nostarch.com/catalog/programming', 'https://nostarch.com/catalog/python', 'https://nostarch.com/catalog/science-math', 'https://nostarch.com/catalog/scratch', 'https://nostarch.com/catalog/system-administration', 'https://nostarch.com/catalog/early-access']

class NoStarch:
	"""No Starch Bookname Collector"""
	def __init__(self):
		return

	def get_page_data(url):
		content = get(url).content
		bs_obj = BeautifulSoup(content, "lxml")
		return bs_obj

	def booklist(object_data):
		item_box = object_data.find_all(
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
		return booklist

	def book_save(booknames,filename):
		df = pd.DataFrame(booknames)
		df.to_csv(f'{filename}.csv')
		return


if __name__ == '__main__':
	sayac = 0
	for x in urllist:
		book_data = NoStarch.get_page_data(x)
		booklist = NoStarch.booklist(book_data)
		filename = str(x).replace("https://nostarch.com/catalog/", "booklist ")
		NoStarch.book_save(booklist,filename)