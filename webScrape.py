import urllib.request
import bs4 as bs
news = "https://www.breitbart.com/"

newsFile = urllib.request.urlopen(news).read()
soup = bs.BeautifulSoup(newsFile, 'html.parser')

sauce = soup.find_all(class_="top_article_main")
print(sauce)

