__author__ = 'bill'
import pickle
import os
import feedparser

def make_rss_pickle(url, file_name="rss.pickle"):
    rss = feedparser.parse(url)
    # file_name = "rss.pickle"
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file_name)
    file = open(file_path, "wb")
    pickle._dump(rss, file)
    file.close()

if __name__ == '__main__':
    url = 'https://norfolk.craigslist.org/search/apa?format=rss'
    make_rss_pickle(url)
