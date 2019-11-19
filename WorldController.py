from datetime import datetime
import pandas as pd
import glob
from StateObj import StateObj, findState
#change this class to contioulsy run in future.

##MAIN##

## CREATE/PARSE DATA FOR ML MODEL##


##CREATE OBJECTS FOR EACH CITY##
## City obj will handle data passed in through none statements
#CountryObj() # only do UNITED STATES
class WorldController:
    def __init__(self):
        cityCountryDict = {}
        for file in glob.glob("./data/weather/*City*"):
            weatherCityData = pd.read_csv(file, header=0, index_col='dt', infer_datetime_format=True)
            weatherCityData = weatherCityData[weatherCityData['Country'] == 'United States' ]

            weatherGroup = weatherCityData.groupby(['Longitude', 'Latitude'])

            for  key, item in weatherGroup:
                for city in item.City.unique():
                    cityCountryDict[city]   =  {'Location': [*item.Longitude.unique(), *item.Latitude.unique()]}
            # remove break
            break

        for file in glob.glob("./data/weather/*City*"):
            weatherCityData = pd.read_csv(file, header=0, index_col='dt')

            weatherCityData = weatherCityData[weatherCityData['Country'] == 'United States']
            weatherCityData.index = pd.to_datetime(weatherCityData.index)
            for key in cityCountryDict.keys():
                #pd.DataFrame(weatherCityData['AverageTemperature'].resample('W').sum(), columns=['AverageTemperature'])
                weatherDict = weatherCityData[weatherCityData['City'] == key].resample('W').mean()['AverageTemperature']
                i = 0
                cityCountryDict[key]['time'] = []
                for date in weatherDict.index.to_pydatetime():
                    otherDict = {date.strftime("%Y-%M-%W"): weatherDict.values[i]}
                    cityCountryDict[key]['time'].append(otherDict)
                    i+=1
            # remove break
            break
        #cityCountryDict has City as key, Location : [longitude, latitude], time: [{WEEK TIMESTAMP : weather}...*]. Each child will find data to fit with its parent classes to pass data to it.  (read the csv, etc.)
        allStateData = pd.read_csv('./data/weather/GlobalLandTemperaturesByState.csv')
        allStateData = allStateData[allStateData['Country'] =='United States']
        allStateData.dt = pd.to_datetime(allStateData.dt)
        allStateData = allStateData.set_index(drop=True, keys='dt')

        #get weather data from 1960 and above.
        allStateData = allStateData[allStateData.index.year>=1960]#.resample('W').mean()['AverageTemperature']
        allStates = []
        for state in allStateData['State'].unique():
            otherData = allStateData[allStateData['State'] == state]
            allStates.append(StateObj(state, otherData))


        for city in cityCountryDict.keys():
             cityStateName = findState(longitude=cityCountryDict[city]['Location'][0], latitude=cityCountryDict[city]['Location'][1])
             for state in allStates:
                 if cityStateName == state.getStateName():
                     state.createCity(longitude=cityCountryDict[city]['Location'][0], latitude=cityCountryDict[city]['Location'][1], cityName=city, data=cityCountryDict[city]['time'])
                     #need this break.  Found the state.
                     break
                 if cityStateName == 'StateNA':
                     state.createCity(longitude=cityCountryDict[city]['Location'][0], latitude=cityCountryDict[city]['Location'][1], cityName=city, data=cityCountryDict[city]['time'])
                     break


        # this is only class attribute that will be used
        self.states = allStates

    def train_long_lat_model(self,sf6, n2o, co2, ch4):
        longLatDF = pd.DataFrame()
        i = 1
        for state in self.states:

            for city in state.getCitiesObj():
                print(f'{i}  {state.getStateName()}  {city.getCityName()} {city.getLongLat()}')


            i+=1
    def train_state_models(self):
        stateModel = "" # should be linear/log model
        for state in self.states:
            #get each state name, use it in conjuncation with the greenhouse gasses.
            state.getStateName()
        return stateModel

    def train_city_models(self):
        pass
## Right here, create ML model.


##


#Once city populated, inf. while loop to get input for a city/state/country day(the next days sf6/co2/ch4/etc
# levels will be calculted and put into the model we have trained to predict #
#given a day, calculate greenhouse level gasses from our formula, and input to city params to be processed with given data