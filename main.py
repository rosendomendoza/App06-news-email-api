import requests
from my_tools import news_about
from my_tools import send_email

# Define the number of articles to show
MAX = 20
SUBSCRIPTION_LIST = ['profesor.rosendo@gmail.com']

topic = "Python AND Artificial Intelligence"

content = news_about(topic)

# Access the data
news_message = ""
for index, article in enumerate(content["articles"][:MAX]):
    # if article['title'] is not None:
    news_message += ((f"{index + 1}. {article['title']}: " + "\n" +
                      article["description"] + "\n") +
                     article["url"] + 2 * "\n")

message = f"""\
Subject: Today´s News about {topic}:

From: Automatic News

{news_message}
"""
message = message.encode('utf-8')
send_email(SUBSCRIPTION_LIST, message)
