import urllib.request
import bs4 as bs
news = "https://www.breitbart.com/"

newsFile = urllib.request.urlopen(news).read()
souped = bs.BeautifulSoup(newsFile, 'lxml')

print(souped)



