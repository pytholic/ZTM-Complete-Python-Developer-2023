"""
Web scraping project. We will grab data from website and work with it.
For this project, we are only interest in html text, so we will ignore
CSS and Js data.

We will also use CSS selectors, since they make it easy to access
nested html elements.

We will filter the posts that have more than 100 points.
"""

import requests
from bs4 import BeautifulSoup
import pprint

# Grab the data
response = requests.get("https://news.ycombinator.com/news")  # p1
response2 = requests.get("https://news.ycombinator.com/news?p=2")  # p2

# Remove the data that we don't need
soup = BeautifulSoup(response.text, "html.parser")
soup2 = BeautifulSoup(response.text, "html.parser")

links = soup.select(".titleline > a")
subtext = soup.select(".subtext")  # votes are inside this subtext
links2 = soup.select(".titleline > a")
subtext2 = soup.select(".subtext")

merged_links = links + links2
merged_subtexts = subtext + subtext2

# Sanity checks
# vote = subtext[0].select(".score")
# print(vote[0])
# votes = soup.select(".score")
# print(votes[0].getText())
# print(votes[0].get("id"))


def sort_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


def create_custom_hackernews(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)  # default is None
        vote = subtext[idx].select(".score")
        if vote:  # only run if vote list exists
            points = int(
                vote[0].getText().replace(" points", "")
            )  # only grabbing plain text -> points field
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_by_votes(hn)


pprint.pprint(create_custom_hackernews(merged_links, merged_subtexts))
