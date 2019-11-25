from datetime import datetime
import pandas as pd
import glob
import numpy as np
from StateObj import StateObj, findState
from matplotlib import pyplot
from DataModifier import DateMod
#change this class to contioulsy run in future.

##MAIN##

## CREATE/PARSE DATA FOR ML MODEL##


##CREATE OBJECTS FOR EACH CITY##
## City obj will handle data passed in through none statements
#CountryObj() # only do UNITED STATES
class WorldController:
    def __init__(self, oo = False):
        if oo:
            cityCountryDict = {}
            for file in glob.glob("./data/weather/*City*"):
                weatherCityData = pd.read_csv(file, header=0, index_col='dt', infer_datetime_format=True)
                weatherCityData = weatherCityData[weatherCityData['Country'] == 'United States' ]

                weatherGroup = weatherCityData.groupby(['Longitude', 'Latitude'])

                for  key, item in weatherGroup:
                    for city in item.City.unique():
                        cityCountryDict[city]   =  {'Location': [*item.Longitude.unique(), *item.Latitude.unique()]}
                # remove break

            allWeatherCityData = pd.DataFrame()
            for file in glob.glob("./data/weather/*City*"):
                weatherCityData = pd.read_csv(file, header=0, index_col='dt')

                weatherCityData = weatherCityData[weatherCityData['Country'] == 'United States']
                weatherCityData.index = pd.to_datetime(weatherCityData.index)
                weatherCityData = weatherCityData[weatherCityData.index.year >= 1960]
                weatherCityData = weatherCityData[weatherCityData.index.year < 2012]
                allWeatherCityData = allWeatherCityData.append(weatherCityData)
                for key in cityCountryDict.keys():
                    #pd.DataFrame(weatherCityData['AverageTemperature'].resample('W').sum(), columns=['AverageTemperature'])
                    weatherDict = weatherCityData[weatherCityData['City'] == key]['AverageTemperature']
                    i = 0
                    cityCountryDict[key]['time'] = []
                    for date in weatherDict.index.to_pydatetime():
                        otherDict = {date.strftime("%Y-%m-%d"): weatherDict.values[i]}
                        cityCountryDict[key]['time'].append(otherDict)
                        i+=1
                # remove break

            #cityCountryDict has City as key, Location : [longitude, latitude], time: [{WEEK TIMESTAMP : weather}...*]. Each child will find data to fit with its parent classes to pass data to it.  (read the csv, etc.)
            allStateData = pd.read_csv('./data/weather/GlobalLandTemperaturesByState.csv')
            allStateData = allStateData[allStateData['Country'] =='United States']
            allStateData.dt = pd.to_datetime(allStateData.dt)
            allStateData = allStateData.set_index(drop=True, keys='dt')

            #get weather data from 1960 and above.
            allStateData = allStateData[allStateData.index.year>=1960]#.resample('W').mean()['AverageTemperature']
            allStateData = allStateData[allStateData.index.year<2012]
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
            self.longLat = weatherCityData






        else:
            weatherCityData = pd.read_csv('./data/weather/unitedStatesTemp.csv', header=0, index_col='dt')
            weatherCityData.index = pd.to_datetime(weatherCityData.index)
            weatherCityData = weatherCityData[weatherCityData.index.year >= 1960]
            weatherCityData = weatherCityData[weatherCityData.index.year <= 2012]
            i = 0
            weatherCityData.Latitude = weatherCityData.Latitude.apply(parseLat)
            weatherCityData.Longitude = weatherCityData.Longitude.apply(parseLong)

            self.monthDict = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None, 11: None, 12:None}
            for name, group in weatherCityData.groupby(by=[weatherCityData.index.month]):

                self.monthDict[group.index[0].month] = group

            #print (monthDict)
            averageMonthDict = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None, 11: None, 12:None}
            for dataFrame in self.monthDict.keys():
                averageMonthDict[dataFrame] = self.monthDict[dataFrame].groupby(by=self.monthDict[dataFrame].index).agg('mean')['AverageTemperature']
            #monthDict[1].to_csv('month1 temperatures')
            self.graphMonthlyChange(averageMonthDict)
            self.calculatePerIncrease(averageMonthDict)




    def getMonthDict(self):
        return self.monthDict

    def calculatePerIncrease(self, aDict):
        for key in aDict.keys():
            print('%increase for month {}  == {}'.format(key, ((aDict[key][-1] - aDict[key][0])/aDict[key][0])*100 ) )


    def graphMonthlyChange(self, aDict):
        for key in aDict.keys():
            pyplot.plot(aDict[key], label=key)
        #pyplot.plot(graphed)
        pyplot.xlabel('Years')
        pyplot.ylabel('Temperature in Celsius')
        pyplot.legend()
        pyplot.savefig('./generatedData/monthDataWithlegend')

        pyplot.figure().clear()

    def getDfToTrain(self,sf6, n2o, co2, ch4):
        sf6 = self.createMonthYear(sf6)
        n2o = self.createMonthYear(n2o)
        co2 = self.createMonthYear(co2)
        ch4 = self.createMonthYear(ch4)
        dfMonthArray = []
        for keys in self.monthDict:
            month1 = pd.DataFrame(self.monthDict[keys][['AverageTemperature', 'Latitude', 'Longitude']])
            month1['sf6'] = np.nan
            month1['n2o'] = np.nan
            month1['co2'] = np.nan
            month1['ch4'] = np.nan
            monthParsed = month1.reset_index()
            i =0
            for index, row in monthParsed.iterrows():
                #print(sf6.loc[index.date()].values[0])
                ymRow = "{}/{}".format(row['dt'].year, row['dt'].month)
                month1['sf6'].iloc[i] = sf6[sf6['index'] == ymRow]['average'].values[0]
                month1['n2o'].iloc[i] = n2o[n2o['index'] == ymRow]['average'].values[0]
                month1['co2'].iloc[i] = co2[co2['index'] == ymRow]['CarbonEmissions'].values[0]
                month1['ch4'].iloc[i] = ch4[ch4['index'] == ymRow]['average'].values[0]
                i+=1
            month1.reset_index(drop=True, inplace=True)
            dfMonthArray.append(month1)
        return dfMonthArray


    def createMonthYear(self, df):
        sf6YearMonth = []
        for i in range(0, len(df.index.year)):
            sf6YearMonth.append('{}/{}'.format(df.index[i].year, df.index[i].month ))
        df = df.reset_index()
        df['index'] = pd.Series(sf6YearMonth)
        return df

    def train_state_models(self):
        stateModel = "" # should be linear/log model
        for state in self.states:
            #get each state name, use it in conjuncation with the greenhouse gasses.
            state.getStateName()
        return stateModel

    def train_city_models(self):
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
## Right here, create ML model.


##


#Once city populated, inf. while loop to get input for a city/state/country day(the next days sf6/co2/ch4/etc
# levels will be calculted and put into the model we have trained to predict #
#given a day, calculate greenhouse level gasses from our formula, and input to city params to be processed with given data
if __name__ == "__main__":
    WorldController()

