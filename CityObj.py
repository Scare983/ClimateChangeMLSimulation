from StateObj import StateObj
class CityObjModel(StateObj):
    #One class that creates the model
    # pass in dict with Country

    def __init__(self, longitude, latitude, cityName, timeTempDict=None):
        # train model here.
        self.longitude = longitude
        self.latitude = latitude
        if type(longitude) is not float:
            if  longitude[-1] == 'E' or longitude[-1] == 'W' :
                self.longitude = parseLong(longitude)
            if latitude[-1] == 'N' or latitude[-1] == 'S':
                self.latitude = parseLat(latitude)
        else:
            pass
        self.cityName = cityName
        self.timeTempDict = timeTempDict
        StateObj.__init__(self, self.longitude,self.latitude)

        ## TODO: FIGURE OUT how all city classes go into one stateobj

    def getCityName(self):
        return self.cityName

    def getStateName(self):
        return super().getStateName()


def parseLong( longitude): #east negative
    if 'E' in longitude:
        return   float(longitude.replace('E', ''))
    else:
        return (-1) * float(longitude.replace('W', ''))

def parseLat( latitude): #north south
    if 'S' in latitude:
        return  (-1) *float(latitude.replace('S', ''))
    else:
        return float(latitude.replace('N', ''))
    # create State Obj, Country Obj


## testing ##
if __name__ == '__main__':
    print(CityObjModel(longitude='40.99N' , latitude='80.95W', cityName='Johns Creek').getStateName())