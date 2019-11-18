
class StateObj():
    def __init__(self, longitude,latitude, stateName=None):
        #we want to use data about the state, not
        if stateName:
            self.stateName = stateName
        else:
            from geopy.geocoders import Nominatim
            geolocator = Nominatim(user_agent='my-app')

            print(longitude)
            print(latitude)
            #using geoPY API to find state for long/lat.
            location = geolocator.reverse("{}, {}".format(longitude, latitude))
            self.stateName = location.raw['address']['state']#.split(', ')[3]


    def getStateName(self):
        return self.stateName


#print(StateObj(52.509669, 13.376294).getStateName())
