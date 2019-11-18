
import pandas as pd
import glob

#change this class to contioulsy run in future.

##MAIN##

## CREATE/PARSE DATA FOR ML MODEL##


##CREATE OBJECTS FOR EACH CITY##
## City obj will handle data passed in through none statements
#CountryObj() # only do UNITED STATES

cityCountryDict = {}
for file in glob.glob("./data/weather/*City*"):
    print(file)
    weatherCityData = pd.read_csv(file, header=0, index_col='dt', infer_datetime_format=True)
    weatherCityData = weatherCityData[weatherCityData['Country'] == 'United States' ]
    weatherGroup = weatherCityData.groupby(['Longitude', 'Latitude'])
    for  key, item in weatherGroup:
        for city in item.City.unique():
            cityCountryDict[city]   =  [*item.Longitude.unique(), *item.Latitude.unique()]
    break

for file in glob.glob("./data/weather/*City*"):
    weatherCityData = pd.read_csv(file, header=0, index_col='dt')

    weatherCityData = weatherCityData[weatherCityData['Country'] == 'United States']
    weatherCityData.index = pd.to_datetime(weatherCityData.index)
    for key in cityCountryDict.keys():
        #pd.DataFrame(weatherCityData['AverageTemperature'].resample('W').sum(), columns=['AverageTemperature'])
        weatherDict = weatherCityData[weatherCityData['City'] == key].resample('W').mean()['AverageTemperature']
        #weatherDictIndex = weatherDict.index
        #weatherDictValue = weatherDict.AverageTemperature
        #cityCountryDict[key] =  weatherDict
        print(pd.DataFrame(weatherDict).index)

    break
print(cityCountryDict)
#Once city populated, inf. while loop to get input for a city/state/country day(the next days sf6/co2/ch4/etc
# levels will be calculted and put into the model we have trained to predict #
#given a day, calculate greenhouse level gasses from our formula, and input to city params to be processed with given data