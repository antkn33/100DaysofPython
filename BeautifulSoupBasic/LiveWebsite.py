from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

"""
# Single Article

article_tag = soup.find(name="span", class_="titleline")
article_text = article_tag.getText()
article_link = article_tag.a.get("href")
article_upvote = soup.find(name="span", class_="score").getText()

print(article_text)
print(article_link)
print(article_upvote)
"""

#####
# Multiple articles

# add find_all
articles = soup.find_all(name="span", class_="titleline")

# create lists 
article_texts = []
article_links = []

# for loop for each article. Append lists
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.a.get("href")
    article_links.append(link)

# same as a for loop but on one line
# add find_all
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

# want to get just the number from the score as an int
# this gets the first article's upvote number as an int
# print(int(article_upvotes[0].split()[0]))

# get the article with the highest number of upvotes
largest = max(article_upvotes)
largest_index = article_upvotes.index(largest)

print(article_texts[largest_index])
print(article_links[largest_index])





