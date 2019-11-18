#parent class, all states have cities, all countries have states.
class CityObjModel():
    #One class that creates the model
    def __init__(self, longitude = None, latitude=None, cityName=None, countryName=None, stateName = None, parseNa=False ):
         if longitude != None:
            self.longitude = longitude
        self.latitude = latitude
        self.cityName = cityName
