#child class all states have cities, all countries have states.
class CityObjModel(StateObj):
    #One class that creates the model
    # pass in dict with Country


    def __init__(self, longitude, latitude, state, country, dateTempDict ):
        # train model here.
        self.longitude = longitude
        self.latitude = latitude
        StateObj.__init__(self, state, country)
        self.dateTempDict = dateTempDict
    # create State Obj, Country Obj
