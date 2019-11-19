class CityObjModel():
    #One class that creates the model
    # pass in dict with Country

    def __init__(self, longitude, latitude, cityName, timeTempDict=None):
        # train model here.
        self.longitude = longitude
        self.latitude = latitude
        self.cityName = cityName
        self.timeTempDict = timeTempDict

        ## TODO: FIGURE OUT how all city classes go into one stateobj

    def getCityName(self):
        return self.cityName


    def getLongLat(self):
        return self.longitude, self.longitude

    #train based on the data inside of this data we have.  This is for future use in case we want each city to have predictions, otherwise it will be generalized in class calling cities
    def trainCityTemp(self, sf6, n2o, co2, ch4):
        #use long/latitude as well.

        #if there is data in our dict, we use it to train, otherwise we must find a location near the long/latitude of this, and use their model with our longitude/latitude.
        pass

    #give a week as datetime, longitude,latitude, predict
    def predictCityTemp(self):
        pass


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


## testing ##
if __name__ == '__main__':
    print(CityObjModel(longitude='40.99N' , latitude='80.95W', cityName='Johns Creek'))
