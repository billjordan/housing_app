__author__ = 'bill'
from Listing_local import *
import json
import pprint

def json_handler(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    else:
        return obj.__dict__


def main():
    outfile_name = "listings.json"
    outfile = open(outfile_name, "w")
    pp = pprint.PrettyPrinter()

    outfile.write(json.dumps({"listings": get_listings()}, default=json_handler, sort_keys=True))

if __name__ == '__main__':
    main()