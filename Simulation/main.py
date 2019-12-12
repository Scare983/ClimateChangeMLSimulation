### Simulation from 1960 to 2012 about different variable greenhouse gases.
from sklearn.externals import joblib
import os
import numpy as np
import pandas as pd
from GreenHouseAgents.ghgControl import ghgControl
import GreenHouseAgents.defaultAgent as GHContainer
import getopt
import sys
import calendar as cal
import warnings



# initial Gh values were calculated at 1960.  New ones can be placed within.
argumentHash = {'Long': None, 'Lat' : None, 'simTime':None, 'beginYear': 1960, 'initialN2o': 276.889729, 'initialSf6': 0.000005, 'initialCo2':217.592896, 'initialCh4':1529.14, 'mlModel':'b', 'output': None}
def usage():
    print('please print correct input values')
    print('python main.py -a (latitude) -o (longitude) -s (simTime)')
    print('Simtime cannot exceed 660 months because we are basing rates of GH on real data ')
    print('Our limitation is that CO2 readings I currently have end at Dec. 2014, but can be extended in the future. ')
    print("")
    print("")
    print("Optional parameters include:  startings values for greenhouse gases.")
    print("2 Models work.  Default = Bayes Lin Model.")
    print("Other Model is regular Lin Regression")
    print('-m  l|b')
    exit(2)


debug = False
try:

    opt, args = getopt.getopt(sys.argv[1:], "y:a:o:s:2:4:6:0:m:t:")
    for opts, arg in opt:
        if opts == '-o':#long
            argumentHash['Long'] = float(arg)
        elif opts == '-a':#lat
            argumentHash['Lat'] = float(arg)
        elif opts == '-s':#simTime
            if(int(arg) > 660):
                usage()
            argumentHash['simTime'] = int(arg)
        elif opts == '-2':#simTime
            argumentHash['initialCo2'] = float(arg)
        elif opts == '-4':#simTime
            argumentHash['initialCh4'] = float(arg)
        elif opts == '-6':#simTime
            argumentHash['initialSf6'] = float(arg)
        elif opts == '-0':#simTime
            argumentHash['initialN2o'] = float(arg)
        elif opts == '-y':#simTime
            argumentHash['beginYear'] = int(arg)
        elif opts == '-m':#simTime
            argumentHash['mlModel'] = arg[0]
        elif opts == '-t':#simTime
            argumentHash['output'] = arg
    for a in argumentHash.keys():
        if argumentHash[a] is None:
            usage()
except getopt.GetoptError:
    usage()

#model takes in sf6, ch4, co2, no2, and long lat(that has been clustered through kmeans)


kMeansModel = joblib.load('../KMeansModel/KMeansModel.pkl')
longLatHash = kMeansModel.predict( np.array([argumentHash['Lat'], argumentHash['Long']]).reshape(1,-1))
monthModels = {'Jan': None, 'Feb': None, 'Mar': None, 'Apr': None, 'May': None, 'Jun': None, 'Jul': None, 'Aug': None, 'Sep': None,  'Oct': None, 'Nov': None, 'Dec':None }
monthFName = ""
if argumentHash['mlModel'] == 'l':
    monthFName = '../learnedLinModelByClusters/'
else:
    monthFName = '../learnedBayLinModelByClusters/'
monthDirList=os.listdir(monthFName)
i = 0
for key in monthModels.keys():
    monthModels[monthDirList[i][0:3]] = joblib.load('{}/{}/{}linModel.pkl'.format(monthFName,monthDirList[i], *longLatHash))
    i+=1
# 2 dots because this is being passed in.
ghDirName = '../greenhouseRates'
sf6RatesFname ='{}/sf6Rates.csv'.format(ghDirName)
ch4RatesFname = '{}/ch4Rates.csv'.format(ghDirName)
co2RatesFname = '{}/co2Rates.csv'.format(ghDirName)
n2oRatesFname = '{}/n2oRates.csv'.format(ghDirName)



simTime =  argumentHash['simTime']
# we are calculating yearly change.


#600 months pass is the time of simulation.
# if time argument is months, we calculaute each month, if year we sum and average all predictions of a year.

### initialization complete.  Run simulation.
########
#these values are instaniented here and modified in simulation.
janTemp, febTemp, marTemp, aprTemp, mayTemp, junTemp, julTemp, augTemp, sepTemp, octTemp, novTemp, decTemp = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
ghgControl.setSimTime(argumentHash['beginYear'], 1)
ch4Obj = GHContainer.ch4Control(ch4RatesFname, argumentHash['initialCh4'])
co2Obj = GHContainer.co2Control(co2RatesFname, argumentHash['initialCo2'])
sf6Obj = GHContainer.sf6Control(sf6RatesFname, argumentHash['initialSf6'])
n2oObj = GHContainer.n2oControl(n2oRatesFname, argumentHash['initialN2o'])
########
def greenHouseGas(env):
    i=0
    while env.now <= argumentHash['simTime']:
        timeOfMonth = env.now % 12
        if timeOfMonth == 0:
            if i != 0:
                argumentHash['beginYear']=argumentHash['beginYear']+1
            else:
                i+=1
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            dtString = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
            janTemp[dtString] = monthModels['Jan'].predict(np.array([cumSf6, cumN2o, cumCo2, cumCh4]).reshape(1,-1))
            yield env.timeout(1)

        elif timeOfMonth == 1:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            #print('np.array([{},{},{},{}]).reshape(1,-1) '.format(cumSf6, cumN2o, cumCo2, cumCh4))
            dtString = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
            febTemp[dtString] = monthModels['Feb'].predict(np.array([cumSf6, cumN2o, cumCo2, cumCh4]).reshape(1,-1))
            yield env.timeout(1)
        elif timeOfMonth == 2:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            dtString = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
            marTemp[dtString] = monthModels['Mar'].predict(np.array([cumSf6, cumN2o, cumCo2, cumCh4]).reshape(1,-1))
            yield env.timeout(1)
        elif timeOfMonth == 3:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            dtString = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
            aprTemp[dtString] = monthModels['Apr'].predict(np.array([cumSf6, cumN2o, cumCo2, cumCh4]).reshape(1,-1))
            yield env.timeout(1)
        elif timeOfMonth == 4:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            dtString = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
            mayTemp[dtString] = monthModels['May'].predict(np.array([cumSf6, cumN2o, cumCo2, cumCh4]).reshape(1,-1))
            yield env.timeout(1)
        elif timeOfMonth == 5:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            dtString = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
            junTemp[dtString] = monthModels['Jun'].predict(np.array([cumSf6, cumN2o, cumCo2, cumCh4]).reshape(1,-1))
            yield env.timeout(1)
        elif timeOfMonth == 6:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            dtString = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
            julTemp[dtString] = monthModels['Jul'].predict(np.array([cumSf6, cumN2o, cumCo2, cumCh4]).reshape(1,-1))
            yield env.timeout(1)
        elif timeOfMonth == 7:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            dtString = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
            augTemp[dtString] = monthModels['Aug'].predict(np.array([cumSf6, cumN2o, cumCo2, cumCh4]).reshape(1,-1))
            yield env.timeout(1)
        elif timeOfMonth == 8:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            dtString = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
            sepTemp[dtString] = monthModels['Sep'].predict(np.array([cumSf6, cumN2o, cumCo2, cumCh4]).reshape(1,-1))
            yield env.timeout(1)
        elif timeOfMonth == 9:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            dtString = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
            octTemp[dtString] = monthModels['Oct'].predict(np.array([cumSf6, cumN2o, cumCo2, cumCh4]).reshape(1,-1))
            yield env.timeout(1)
        elif timeOfMonth == 10:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            dtString = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
            novTemp[dtString] = monthModels['Nov'].predict(np.array([cumSf6, cumN2o, cumCo2, cumCh4]).reshape(1,-1))
            yield env.timeout(1)
        elif timeOfMonth == 11:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            dtString = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
            decTemp[dtString] = monthModels['Dec'].predict(np.array([cumSf6, cumN2o, cumCo2, cumCh4]).reshape(1,-1))
            yield env.timeout(1)
            #increment year at end.

def graphActVsPredicted(joinedDf, monthName, showAll=False):
    import matplotlib.pyplot as plt


    if argumentHash['output'] is None:
        plt.plot(joinedDf['average'], label='Actual Temp')
        plt.plot(joinedDf['predTemp'], label='Predicted Temp')
        plt.title("{} Average Temperature".format(monthName))
        plt.show(block=True)
        plt.legend()
    else:
        if showAll:
            plt.plot(joinedDf['average'])
            plt.plot(joinedDf['predTemp'], marker='o', markersize=8, linewidth=2, linestyle='dashed', label='Predicted {}'.format(monthName))
            plt.legend()
            plt.savefig('{}/{}.png'.format(argumentHash['output'], 'ActVsPredictedAll'))
        else:
            plt.plot(joinedDf['average'], label='Actual Temp')
            plt.plot(joinedDf['predTemp'],  markersize=8, linewidth=2, linestyle='dashed', label='Predicted Temp')
            plt.title("{} Average Temperature".format(monthName))
            plt.legend()
            plt.savefig('{}/{}/{}.png'.format(argumentHash['output'], monthName, 'ActVsPredicted'))
            plt.clf()


def formatWeatherDictToDf(weatherDict):
    data = []

    for keys in weatherDict.keys():
        data.append(['{}-1'.format(keys), *weatherDict[keys]])
    df = pd.DataFrame(data, columns=['dt', 'predTemp'])
    df.set_index('dt', inplace=True)
    df.index=pd.to_datetime(df.index)
    return df
def generateMonthData():
    i=0
    for myMonth in [janTemp, febTemp, marTemp, aprTemp, mayTemp, junTemp, julTemp, augTemp, sepTemp, octTemp, novTemp, decTemp]:
        monthDf = formatWeatherDictToDf(myMonth)
        fName = '../ActualClusterTemperatures/{}/Cluster{}Temp.csv'.format(cal.month_abbr[i+1], *longLatHash)
        df = pd.read_csv(fName, index_col='dt')
        df.index=pd.to_datetime(df.index)

        joined = monthDf.join(df)
        joined.dropna(inplace=True)
        graphActVsPredicted(joined, cal.month_abbr[i+1])

        calculateMSE(joined, cal.month_abbr[i+1])
        i+=1
    #this loop just to show Cumultive weather
    i=0
    for myMonth in [janTemp, febTemp, marTemp, aprTemp, mayTemp, junTemp, julTemp, augTemp, sepTemp, octTemp, novTemp, decTemp]:
        monthDf = formatWeatherDictToDf(myMonth)
        fName = '../ActualClusterTemperatures/{}/Cluster{}Temp.csv'.format(cal.month_abbr[i+1], *longLatHash)
        df = pd.read_csv(fName, index_col='dt')
        df.index=pd.to_datetime(df.index)
        joined = monthDf.join(df)
        joined.dropna(inplace=True)
        graphActVsPredicted(joined, cal.month_abbr[i+1], True)
        i+=1
        #print(joined)
def calculateMSE(joinedDf, monthName):
    mse = np.square(np.subtract(joinedDf['average'].to_list(), joinedDf['predTemp'].to_list())).mean()
    file1=open(r"{}/{}/MSE.txt".format(argumentHash['output'], monthName), "w+")
    file1.write("MSE of {}: {}".format(monthName, mse))
    file1.close()

import simpy
env = simpy.Environment()
env.process(greenHouseGas(env))
env.run(until=simTime)
generateMonthData()


