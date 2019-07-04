from bs4 import BeautifulSoup
import requests
import re
url='http://www.imdb.com/chart/top'
r = requests.get(url) 
bs = BeautifulSoup(r.text,'lxml')
for movie in bs.findAll('td','title'):
    title = movie.find('a').contents[0]
    year = movie.find('span','year_type').contents[0]
    imdbID = movie.find('span','rating-cancel').a['href'].split('/')[2]
    print (title, genres,runtime, rating, year, imdbID)
