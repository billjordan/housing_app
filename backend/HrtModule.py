import requests


class Location(object):
    
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class BusStop(object):
    
    def __init__(self, stop_id, location, stop_name): 
        self.stop_id = stop_id
        self.location = location
        self.stop_name = stop_name


def get_closest_stop(latitude, longitude):
    url = "http://www.billjordan.info:15000/api/stops/near/{}/{}/".format(latitude, longitude)
    query_result = requests.get(url).json()[0]
    #print(query_result)
    #print(query_result[0])
    return BusStop(
        stop_id = query_result["stopId"],
        location = Location(query_result["location"][0], query_result["location"][1]), 
        stop_name = query_result["stopName"]
    )

if __name__=="__main__":
    main()
