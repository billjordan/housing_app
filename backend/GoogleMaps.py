import requests
from Location import Location
import pprint
import time

class Distance(object):

    def __init__(self, distance):
        self.text = distance["text"]
        self.value = distance["value"] # meters

class Duration(object):

    def __init__(self, duration):
        self.text = duration["text"]
        self.value = duration["value"] # seconds

class Route(object):

    def __init__(self, json):
        #take the first route
        self.route = json["routes"][0]
        #there are no waypoints, so there will only be one leg
        self.leg = self.route["legs"][0]
        self.distance = Distance(self.leg["distance"])
        self.duration = Duration(self.leg["duration"])



class WalkingRouteRequest(object):
    
    def __init__(self, origin, destination):
        self.end_point = "https://maps.googleapis.com/maps/api/directions"
        self.response_type = "json"
        self.origin = str(origin)
        self.destination = str(destination)
        self.key = "AIzaSyDOLlm23SiOaL9Q3HY-BlLDrZugDgLP5ts"
        self.mode="walking"
        self.url="{}/{}?key={}&origin={}&destination={}&mode={}".format(
            self.end_point,
            self.response_type,
            self.key,
            self.origin, 
            self.destination,
            self.mode
        )
        
    def get_route_json(self):
        #max 2 requests per second
        time.sleep(.51)
        return requests.get(self.url).json()

    def get_route(self):
        return Route(self.get_route_json())


def main():
    route_request = WalkingRouteRequest(Location("36.855185", "-76.286539"), Location("36.878035","-76.294607"))
    route = route_request.get_route()
    pp = pprint.PrettyPrinter()
    pp.pprint(route.leg)
    print("\n\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n")
    print("distance:\t{}\t{}".format(route.distance.text, route.distance.value))
    print("duration:\t{}\t{}".format(route.duration.text, route.duration.value))


if __name__=="__main__":
    main()
