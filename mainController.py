from WorldController import WorldController
from DataModifier import DateMod, IPA
import pandas as pd
import glob
# worldController takes care of temperature/longitude
#datamodifer is used to modify other data




sf6_data = pd.read_csv('./data/Sf6/sf6_mm_gl.csv', header=0)
sf6_obj = DateMod(sf6_data, 'average')
#print(sf6_obj.dayDataFrame)

sf6_obj.monthDataFrame.to_csv('sf6_month_data')

n2o_data = pd.read_csv('./data/N2o/n2o_mm_gl.csv',header=0)
n2o_obj = DateMod(n2o_data, 'average')

n2o_obj.monthDataFrame.to_csv('N20_month_data')
listOfCh4 = []
i = 0
for file in glob.glob('./data/Ch4/*'):
    ch4_data = pd.read_csv(file, header=0)
    listOfCh4.append(DateMod(ch4_data, 'value'))

    if i==10:
        break
    i+=1
joinedCH4 = pd.DataFrame()
# concat all dataframes we made, and create sum
for ch4DataFrame in listOfCh4:
    joinedCH4 = pd.concat([joinedCH4, ch4DataFrame.monthDataFrame], axis=1)

# aggregate each column to get sum of all of the files we scraped.
joinedCH4 = joinedCH4.agg('sum',axis=1)
joinedCH4 = joinedCH4.to_frame().reset_index().rename(columns={'index':'month',0:'sum'})
CH4_year = []
CH4_month = []
for date in joinedCH4.month:
    CH4_year.append(date.year)
    CH4_month.append(date.month)
joinedCH4.month = CH4_month
joinedCH4['year'] = CH4_year
CH4_obj = DateMod(joinedCH4, 'sum')
#print(CH4_obj.dayDataFrame)
joinedCH4.to_csv('CH4_month_data')

# Don't know how to do these conversion.  Need help.
#ignoring the per capita data, we will use the yearly carbon emmision data and divide it into days then weeks and months
co2_data = pd.read_csv('./data/CO2Emission/global.1751_2014.csv', header=0)
co2_data = co2_data.rename(columns={'Year':'year','Total carbon emissions from fossil fuel consumption and cement production (million metric tons of C)':'CarbonEmissions'})
co2_data = co2_data.loc[:,['year','CarbonEmissions']]
co2_data = co2_data.drop(co2_data.index[0]).reset_index(drop=True)
co2_data = co2_data.apply(pd.to_numeric)
co2_obj = DateMod(co2_data,'CarbonEmissions')
#print(joinedCH4)
greenhouse = [sf6_obj,n2o_obj,CH4_obj, co2_obj]
for obj in greenhouse:
    print(IPA(obj.monthDataFrame[obj.monthDataFrame.keys().tolist()[0]]))
# initialize weather data into objs.
#mainControl = WorldController()
#mainControl.train_long_lat_model(None,None,None,None)



