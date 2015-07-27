__author__ = 'bill'


class Location(object):
    
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return str(self.latitude) + "," + str(self.longitude)