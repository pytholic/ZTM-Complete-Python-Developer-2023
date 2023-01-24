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


# Function to grab data
def get_links_subtexts(url, num_pages):
    all_links = []
    all_subtexts = []

    for i in range(num_pages):
        if i == 0:
            response = requests.get(f"{url}")
        else:
            response = requests.get(f"{url}?p={i+1}")
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.select(".titleline > a")
        subtext = soup.select(".subtext")
        all_links += links
        all_subtexts += subtext

    return all_links, all_subtexts


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


links, subtexts = get_links_subtexts(
    url="https://news.ycombinator.com/news", num_pages=3
)
pprint.pprint(create_custom_hackernews(links, subtexts))
