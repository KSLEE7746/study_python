import string
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import Series, DataFrame
import pandas_datareader.data as web
import datetime
import sqlite3

#------------------------ NAVER Movie Crawling and DB Storing using pandas DataFrame
def spider():
	url='http://movie.naver.com/movie/running/current.nhn'	
	soup = parsingCode(url)

	title = soup.find_all('dl', attrs = { 'class' : 'lst_dsc'})

	for link in title:

		print(link.find('a').get_text() + ' - point : ' +
			link.find('span', attrs = { 'class' : 'num'}).get_text()) 
		#+ ' / ' + link.find('span').get_text())
		#href_url = link.get('href')
		#print(link.a['title'])
		#if (href_url.find('http') == -1) and (href_url.find('/movie/bi/mi/basic.nhn?code') == -1):
		#	title_url = 'http://movie.naver.com' + href_url
		#	print(title_url)
		#else: 
		#	continue		

		#getTitle(title_url)

def parsingCode(url):
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, 'lxml')

	return soup

def getTitle(url):
	soup = parsingCode(url)
	#"div", { "class" : "content"}
	#title = soup.find("h_movie")
	for title in soup.find():
		print(title.string)

spider()



