from WorldController import WorldController
from matplotlib import pyplot as plt
from DataModifier import DateMod, IPA
import pandas as pd
import glob
from matplotlib import pyplot as plt
# worldController takes care of temperature/longitude
#datamodifer is used to modify other data

def convertDFIntoMonthDict(dataFrame):
    monthDict = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None, 11: None, 12:None}
    for name, group in dataFrame.groupby(by=[dataFrame.index.month]):
        monthDict[group.index[0].month] = group
    return monthDict


sf6_data = pd.read_csv('./data/Sf6/sf6_mm_gl.csv', header=0)
sf6_obj = DateMod(sf6_data, 'average', 'sf6')
sf6_dict = convertDFIntoMonthDict(sf6_obj.monthDataFrame[sf6_obj.monthDataFrame.index.year <2012])

sf6_obj.monthDataFrame.to_csv('sf6_month_data')

n2o_data = pd.read_csv('./data/N2o/n2o_mm_gl.csv',header=0)
n2o_obj = DateMod(n2o_data, 'average', 'n2o')
n2o_obj.monthDataFrame.to_csv('N20_month_data')
n2o_dict = convertDFIntoMonthDict(n2o_obj.monthDataFrame[n2o_obj.monthDataFrame.index.year <2012])

ch4_txt = open('./data/Ch4/ch4_mm_gl.txt',mode='r')
keys = ch4_txt.readline().split()
for key in keys:
    ch4_data[key] = []
for line in ch4_txt:
    for i, v in enumerate(line.split()):
        ch4_data[keys[i]].append(v)
ch4_data = pd.DataFrame(ch4_data)
ch4_data = ch4_data.apply(pd.to_numeric)
ch4_obj = DateMod(ch4_data, 'average', 'ch4')
ch4_dict = convertDFIntoMonthDict(CH4_obj.monthDataFrame[CH4_obj.monthDataFrame.index.year <2012])

# Don't know how to do these conversion.  Need help.
#ignoring the per capita data, we will use the yearly carbon emmision data and divide it into days then weeks and months
co2_data = pd.read_csv('./data/CO2Emission/global.1751_2014.csv', header=0)
co2_data = co2_data.rename(columns={'Year':'year','Total carbon emissions from fossil fuel consumption and cement production (million metric tons of C)':'CarbonEmissions'})
co2_data = co2_data.loc[:,['year','CarbonEmissions']]
co2_data = co2_data.drop(co2_data.index[0]).reset_index(drop=True)
co2_data = co2_data.apply(pd.to_numeric)
co2_obj = DateMod(co2_data,'CarbonEmissions', 'co2')
#print(joinedCH4)
co2_dict = convertDFIntoMonthDict(co2_obj.monthDataFrame[co2_obj.monthDataFrame.index.year <2012])


greenhouse = [sf6_obj,n2o_obj,CH4_obj, co2_obj]
for obj in greenhouse:
    interval = []
    for i, month in enumerate(obj.yearDataFrame.index):
        if i != 0:
            interval.append(old + '-' + month.strftime('%m/%Y') )
            #interval.append(i)
        old = month.strftime('%m/%Y')
    plt.plot(interval, IPA(obj.yearDataFrame[obj.yearDataFrame.keys().tolist()[0]]))
    plt.show()
    #print(IPA(obj.monthDataFrame[obj.monthDataFrame.keys().tolist()[0]]))
# initialize weather data into objs.
mainControl = WorldController()


    #nitDf = pd.DataFrame()
    #allWeatherLongLat =  pd.concat(allWeatherLongLat, initDf)
    #print(allWeatherLongLat)
#self,sf6, n2o, co2, ch4
myTrainedArray  = mainControl.getDfToTrain(sf6_obj.monthDataFrame[sf6_obj.monthDataFrame.index.year <=2012], n2o_obj.monthDataFrame[n2o_obj.monthDataFrame.index.year <=2012], co2_obj.monthDataFrame[co2_obj.monthDataFrame.index.year <=2012], CH4_obj.monthDataFrame[CH4_obj.monthDataFrame.index.year <=2012])

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
linearModel = []
i = 1
for df in myTrainedArray:
    x =  df[df.columns[1:]]
    y = df[df.columns[0]]
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.8, random_state=42)
    linMod = LinearRegression().fit(X_train, y_train)
    linearModel.append(linMod)
    plt.title(f'month: {i}')
    plt.plot(y_test, label='real')
    plt.plot(linMod.predict(X_test), label='predicted')
    plt.show()
    i+=1
#mainControl.train_long_lat_model(None,None,None,None)


