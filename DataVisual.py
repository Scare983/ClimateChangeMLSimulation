import pandas as pd
import glob
from calendar import monthrange
import datetime as dt
import numpy as np
from DataModifier import DateMod, IPA
from matplotlib import pyplot as plt

sf6_data = pd.read_csv('./data/Sf6/sf6_mm_gl.csv', header=0)
sf6_obj = DateMod(sf6_data, 'average', 'sf6')
n2o_data = pd.read_csv('./data/N2o/n2o_mm_gl.csv',header=0)
n2o_obj = DateMod(n2o_data, 'average', 'n2o')
listOfCh4 = []
i = 0
for file in glob.glob('./data/Ch4/*'):
    ch4_data = pd.read_csv(file, header=0)
    listOfCh4.append(DateMod(ch4_data, 'value', 'CH4'))

    if i==10:
        break
    i+=1
joinedCH4 = pd.DataFrame()
for ch4DataFrame in listOfCh4:
    joinedCH4 = pd.concat([joinedCH4, ch4DataFrame.monthDataFrame], axis=1)
    joinedCH4 = joinedCH4.agg('sum',axis=1)
joinedCH4 = joinedCH4.to_frame().reset_index().rename(columns={'index':'month',0:'sum'})
CH4_year = []
CH4_month = []
for date in joinedCH4.month:
    CH4_year.append(date.year)
    CH4_month.append(date.month)
joinedCH4.month = CH4_month
joinedCH4['year'] = CH4_year
CH4_obj = DateMod(joinedCH4, 'sum', 'CH4')
co2_data = pd.read_csv('./data/CO2Emission/global.1751_2014.csv', header=0)
co2_data = co2_data.rename(columns={'Year':'year','Total carbon emissions from fossil fuel consumption and cement production (million metric tons of C)':'CarbonEmissions'})
co2_data = co2_data.loc[:,['year','CarbonEmissions']]
co2_data = co2_data.drop(co2_data.index[0]).reset_index(drop=True)
co2_data = co2_data.apply(pd.to_numeric)
co2_obj = DateMod(co2_data,'CarbonEmissions', "CO2")

greenhouse = [sf6_obj,n2o_obj,CH4_obj, co2_obj]
for obj in greenhouse:
    plt.plot(list(obj.dayDataFrame.index), obj.dayDataFrame.values.tolist())
    plt.title(obj.dataName + " " +  obj.colVal + " over time")
    plt.show()