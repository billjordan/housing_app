import urllib.request
import re
import requests


latitude_pattern = re.compile("data-latitude=(\"|\')\+*-*[0-9]+.[0-9]+(\"|\')")
longitude_pattern = re.compile("data-longitude=(\"|\')\+*-*[0-9]+.[0-9]+(\"|\')")
#price_pattern = re.compile("\<span[\\s+]class=(\"|\')price(\"|\')\>[$]?\\d+[.d+]?\</span\>")
price_pattern = re.compile("<span\sclass=(\"|\')price(\"|\')>[$]?\d+(\.\d*)?</span>")
amount_pattern = re.compile("[$]?\d+(\.\d*)?")

class ListingPage(object):
    
    def __init__(self, url):
        self.url = url
        self.response = urllib.request.urlopen(url) 
        self.html = str(self.response.read())
        
        #get the latitude from the page
        result = latitude_pattern.search(self.html)
        self.lat_string = self.html[result.start():result.end()]
        lat_val_start = self.lat_string.find('"')
        lat_val_end = self.lat_string.find('"', lat_val_start+1)
        self.latitude = self.lat_string[lat_val_start+1:lat_val_end]
        #print(self.latitude)
        #print("{}::{}".format(lat_val_start, lat_val_end))  

        #get the longitude from the page
        result = longitude_pattern.search(self.html)
        #print(result)
        self.long_string = self.html[result.start():result.end()]
        long_val_start = self.long_string.find('"')
        long_val_end = self.long_string.find('"', long_val_start+1)
        self.longitude = self.long_string[long_val_start+1:long_val_end]
        #print(self.longitude)
        #print("{}::{}".format(long_val_start, long_val_end))  

        #get the price from the page
        result = price_pattern.search(self.html)
        price_html_string = self.html[result.start():result.end()]
        result = amount_pattern.search(price_html_string)
        price_string = price_html_string[result.start():result.end()]
        
        if price_string[0] == "$":
            self.price = price_string[1:]
        else:
            self.price = price_string         
        #print(self.price)
        
def main():
    test_url = "http://norfolk.craigslist.org/apa/5141882255.html"
    page = ListingPage(test_url)
    print(page.longitude)
    print(page.latitude)
    print(page.price)

if __name__=="__main__":
    main()
