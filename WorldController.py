from datetime import datetime
import pandas as pd
import glob
from CityObj import CityObjModel
#change this class to contioulsy run in future.

##MAIN##

## CREATE/PARSE DATA FOR ML MODEL##


##CREATE OBJECTS FOR EACH CITY##
## City obj will handle data passed in through none statements
#CountryObj() # only do UNITED STATES

cityCountryDict = {}
for file in glob.glob("./data/weather/*City*"):
    weatherCityData = pd.read_csv(file, header=0, index_col='dt', infer_datetime_format=True)
    weatherCityData = weatherCityData[weatherCityData['Country'] == 'United States' ]

    weatherGroup = weatherCityData.groupby(['Longitude', 'Latitude'])

    for  key, item in weatherGroup:
        for city in item.City.unique():
            cityCountryDict[city]   =  {'Location': [*item.Longitude.unique(), *item.Latitude.unique()]}
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
    break


#cityCountryDict has City as key, Location : [longitude, latitude], time: [{WEEK TIMESTAMP : weather}...*]. Each child will find data to fit with its parent classes to pass data to it.  (read the csv, etc.)

#TODO: pass each City into a City Class.  There we will store info, and on first instantiation, those classes will call
# once we create the states with all the cities, converge them based on same states.
cityList = []
for city in cityCountryDict.keys():
    cityList.append(CityObjModel(longitude=cityCountryDict[city]['Location'][0],latitude=cityCountryDict[city]['Location'][1], cityName=city, timeTempDict=cityCountryDict[city]['time']))
    break
for city in cityList:
    city.getStateName()
    break

#Once city populated, inf. while loop to get input for a city/state/country day(the next days sf6/co2/ch4/etc
# levels will be calculted and put into the model we have trained to predict #
#given a day, calculate greenhouse level gasses from our formula, and input to city params to be processed with given data