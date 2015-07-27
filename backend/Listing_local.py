import os
import feedparser
import re
import pickle
from ListingPage import ListingPage
from HrtModule import *
from GoogleMaps import *
import pprint

url = 'http://localhost/cl_pages/rss_feed.xml'
strip_string = "http://norfolk.craigslist.org/apa/"
img_string_cl = "http://images.craigslist.org/"
replace_string = "http://localhost/new_cl_pages/"
pattern = re.compile("/[0-9]+.html")

class Listing(object):
    
    def __init__(self, rss_entry):
        self.title = rss_entry["title"]
        self.summary = rss_entry["summary"]
        self.published = rss_entry["published_parsed"]
        self.updated = rss_entry["updated_parsed"]
        result = pattern.search(rss_entry["id"])
        self.uid = rss_entry["id"][result.start() + 1:result.end()-5]
        self.thubnail_img_location = get_local_img(rss_entry["enc_enclosure"]["resource"], self.uid)
        self.big_img_location = get_big_img(rss_entry["enc_enclosure"]["resource"], self.uid)
        # self.link = rss_entry["link"]
        self.link = get_local_page(rss_entry["link"])
        self.page = ListingPage(self.link)
        self.latitude = self.page.latitude
        self.longitude = self.page.longitude
        self.price = self.page.price
        self.bus_stop = get_closest_stop(self.latitude, self.longitude)
        self.listing_location = Location(self.latitude, self.longitude)
        self.route = WalkingRouteRequest(self.listing_location, self.bus_stop.location).get_route()

    def __str__(self):
        return_str = ""
        return_str += "title: {}\n".format(self.title)
        return_str += "summary: {}\n".format(self.summary)
        return_str += "published: {}\n".format(self.published)
        return_str += "img: {}\n".format(self.img_location)
        return_str += "uid: {}\n".format(self.uid)
        return_str += "listing url: {}\n".format(self.link)
        return_str += "price: {}\n".format(self.price)
        return_str += "transit stop: {}\n".format(self.bus_stop.stop_name)
        return_str += "Distace to transit stop: {}\n".format(self.route.distance.text)
        return_str += "Walking time: {}\n\n\n".format(self.route.duration.text)
        return return_str

def get_local_img(cl_image_url, uid):
    return cl_image_url.replace(img_string_cl, replace_string + "{}_files/".format(uid)).replace("300x300", "50x50c")


def get_big_img(cl_image_url, uid):
    return cl_image_url.replace(img_string_cl, replace_string + "{}_files/".format(uid)).replace("300x300", "600x450")

def get_local_page(cl_page_url):
    return cl_page_url.replace(strip_string, replace_string)




def load_rss(rss_file = "rss.pickle"):
    rss = pickle.load(
            open(
                os.path.join(
                    os.path.dirname(__file__),
                    rss_file
                ),
                "rb"
            )
        )
    return rss


def main():
    pp = pprint.PrettyPrinter()
    feed = load_rss()
    # pp.pprint(feed)
    entries = feed.entries
    print(len(entries))
    # pp.pprint(entries)
    listings = []
    for entry in entries:
        try:
            listing = Listing(entry)
            listings.append(listing)
        except Exception as e:
            print(e)
    print(len(listings))
    pp.pprint(str(listings))

if __name__=="__main__":
    main()
