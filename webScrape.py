import pandas as pd
import urllib.request
import bs4 as bs
news = "https://www.breitbart.com/"

newsFile = urllib.request.urlopen(news).read()
soup = bs.BeautifulSoup(newsFile, 'html.parser')

def mainheadline():
    sauce = soup.find(class_="top_article_main")

    headline = sauce.h2.a.text
    desc = sauce.div.p.text
    print(headline)
    print(desc)
    pass

#mainheadline()

def featureheadline():
    sauce2 = soup.find("section", {"class": "featured_side"})
    
    post = sauce2.find_all(class_="post")
    features = [posts.find("h2").text for posts in post]
    
    print(features)
    pass
#featureheadline()

headlines = [(mainheadline, featureheadline)]
labels    = ["Mainheadlines", "Featuredheadlines"]
news_Info = pd.DataFrame(headlines, columns=labels)
    
news_Info.dtypes
# print(news_Info)
# news_Info.to_csv('news_Info.csv')