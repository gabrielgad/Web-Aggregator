import pandas as pd
import urllib.request
import bs4 as bs

news = "https://www.breitbart.com/"
newsFile = urllib.request.urlopen(news).read()
soup = bs.BeautifulSoup(newsFile, 'html.parser')


sauce = soup.find(class_="top_article_main")
headline = sauce.h2.a.text
desc = sauce.div.p.text
mainheadline = (headline + " | " + desc)


sauce2 = soup.find("section", {"class": "featured_side"})
post = sauce2.find_all(class_="post")
features = [posts.find("h2").text for posts in post]


sauce3 = soup.find("section", {"id": "BBTrendNow"})
trend = sauce3.find_all('li')
trending = [trends.find("a").text for trends in trend]


df = pd.DataFrame(
    data=(mainheadline, features, trending)
    )
df.shape
