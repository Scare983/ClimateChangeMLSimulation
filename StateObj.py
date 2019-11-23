#from CountryObj import CountryObjModel
from CityObj import CityObjModel
import pandas as pd
import numpy as np
class StateObj():
    # example:  GA: {cities : [], stateTemp:{date: temperature}}
    def __init__(self,stateName, dataFrame=None):
        #we want to use data about the state, not
        self.stateDict = {stateName: {'CityObj': [], 'time':{}}}
        if  isinstance(dataFrame, pd.DataFrame):
            if not dataFrame.empty:
                self.createStateDataWithData(dataFrame.copy())
        #for each state, create it's history, children will have this inherinently.

        else:
            self.createStateDataWithoutData(self.getStateName())

    #pass in a week of data by days.
    def createStateDataWithData(self, allStateData):
        #add it to dict, and create timstamp data.
        self.stateDict[self.getStateName()]['time'] = allStateData.resample('M').mean()['AverageTemperature'].to_dict()

    # do nothing.
    def createStateDataWithoutData(self, stateName):
        pass

    def addStateTempDay(self, day, temp):
        pass

    def createCity(self,data,longitude=None,latitude=None,  cityName=None):
        newCity = CityObjModel(longitude,latitude, cityName, data)
        self.stateDict[self.getStateName()]['CityObj'].append(newCity)

    def getStateName(self):
        for key in self.stateDict.keys():
            return key

    def getStateTempData(self):



        return self.stateDict[self.getStateName()]['time']

    def getCitieNames(self):
        # return city names
        cityNames = []
        for city in self.stateDict[self.getStateName()]['CityObj']:
            cityNames.append(city.getCityName())
        return cityNames
    # returns list of long/lat of cities in state

    def getCitiesObj(self):
        return self.stateDict[self.getStateName()]['CityObj']

    #return formatted dataframe,
    def getCityTempData(self):
        monthsDf = pd.DataFrame()
        monthDict = {'01': [], '02': [], '03': [], '04': [], '05': [], '06': [], '07': [], '08': [], '09': [], '10': [], '11': [], '12':[], 'Longitude': [], 'Latitude': []}

        for city in self.getCitiesObj():
            long, lat = city.getLongLat()
            citySize = {'01':0}
            for keys in city.timeTempDict:

                for aKey in keys:

                    month = aKey.split('-')[1]

                    if keys[aKey]:
                        if month == '01':
                            citySize[month]+=1
                        monthDict[month].append(keys[aKey])
                    else:
                        monthDict[month].append(np.nan)

            for i in range(citySize['01']):
                monthDict['Longitude'].append(long)
                monthDict['Latitude'].append(lat)
            #print(len(monthDict['Longitude']))
            #print(len(monthDict['01']))
            #print(len(monthDict['03']))
            #print(len(monthDict['Longitude']))
            #monthsDf = pd.concat(monthsDf, newDf)
        return monthDict
    def getCitiesLongLat(self):
        cityLongLat = []
        for city in self.getCitieNames():
            print(cityLongLat)
        return cityLongLat



    def trainStateModel(self, sf6, n2o, co2, ch4):
    # use this statename for model.
        pass
    #
    def predictState(self, date, daysf6, dayn2o, dayco2, daych4):
        pass




def findState(longitude, latitude):
    if type(longitude) is not float:
        if  longitude[-1] == 'E' or longitude[-1] == 'W' :
            longitude = parseLong(longitude)
        if latitude[-1] == 'N' or latitude[-1] == 'S':
            latitude = parseLat(latitude)
    else:
        pass
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent='my-app')

    #using geoPY API to find state for long/lat.
    try:
        location = geolocator.reverse("{}, {}".format(latitude, longitude))
        stateName = location.raw['address']['state']#.split(', ')[3]
    except:
        stateName = "StateNA"
    return stateName

    #give it a list of sf6, no2, ch4, etc..



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


#print(StateObj(stateName='Georgia'))
