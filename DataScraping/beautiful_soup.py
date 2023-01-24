"""
Some useful Beautiful Soup operations.
"""

import requests
from bs4 import BeautifulSoup

# Grab the data
response = requests.get("https://news.ycombinator.com/news")
# print(response.text)

# Remove the data that we don't need
soup = BeautifulSoup(response.text, "html.parser")

# Useful beautiful soup commands
# print(soup)
# print(soup.body)
# print(soup.contents)
# print(soup.find_all("title"))  # find all title tags
# print(soup.find_all("div"))  # find all div tags
# print(soup.find_all("a"))  # find all link tags
# print(soup.a)  # prints first a tag
# print(soup.find("a"))  # finds only first occurrence
# print(soup.find(id="score_34497898"))

# CSS selectors
print(soup.select(".score"))
print(soup.select("#score_34496287"))
