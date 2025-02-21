## Use the NewsAPI and the requests module to fetch the daily news related to different topics.

#------Code------#
import requests
import json

query = input("What type of news are you interested in? ")
# https://newsapi.org/v2/everything?q=tesla&from=2025-01-20&sortBy=publishedAt&apiKey=b385ba3947234cb0b1f645101f2dcdb7
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-01-20&sortBy=publishedAt&apiKey=b385ba3947234cb0b1f645101f2dcdb7" #api key from NewsAPI
r = requests.get(url)
news = json.loads(r.text)

for article in news["articles"] :
    print(article["title"])  #to print title of the news
    print(article["description"])   #to print description of the news
    print("----------------------")     #to mark that news have ended