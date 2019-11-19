from WorldController import WorldController
from DataModifier import DateMod
import pandas as pd
import glob
# worldController takes care of temperature/longitude
#datamodifer is used to modify other data




sf6_data = pd.read_csv('./data/Sf6/sf6_mm_gl.csv', header=0)
sf6_obj = DateMod(sf6_data, 'average')
n2o_data = pd.read_csv('./data/N2o/n2o_mm_gl.csv',header=0)
n2o_obj = DateMod(n2o_data, 'average')


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


# Don't know how to do these conversion.  Need help.
co2_data = pd.read_csv('./data/CO2Emission/global.1751_2014.csv', header=0)


print(joinedCH4)

#mainControl = WorldController()




