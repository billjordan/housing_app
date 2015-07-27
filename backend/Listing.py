import feedparser
import re
from ListingPage import ListingPage
from HrtModule import *

url = 'https://norfolk.craigslist.org/search/apa?format=rss'
pattern = re.compile("/[0-9]+.html")

class Listing(object):
    
    def __init__(self, rss_entry):
        self.title = rss_entry["title"]
        self.summary = rss_entry["summary"]
        self.published = rss_entry["published_parsed"]
        self.updated = rss_entry["updated_parsed"]
        self.img_location = rss_entry["enc_enclosure"]
        result = pattern.search(rss_entry["id"])
        self.uid = rss_entry["id"][result.start() + 1:result.end()-5]
        self.link = rss_entry["link"]
        self.page = ListingPage(self.link)
        self.latitude = self.page.latitude
        self.longitude = self.page.longitude
        self.price = self.page.price
        self.bus_stop = get_closest_stop(self.latitude, self.longitude)


def main():
    feed = feedparser.parse(url)
    entries = feed.entries
    listings = []
    for entry in entries:
        try:
            listing = Listing(entry)
            listings.append(listing)
        except Exception as e:
            print(e) 
    print(len(listings))
    print(listings)

if __name__=="__main__":
    main()
