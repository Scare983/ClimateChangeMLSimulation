### Simulation from 1960 to 2012 about different variable greenhouse gases.
from sklearn.externals import joblib
import os
import numpy as np
from GreenHouseAgents.ghgControl import ghgControl
import GreenHouseAgents.defaultAgent as GHContainer
import getopt
import sys
import ast
# initial Gh values were calculated at 1960.  New ones can be placed within.
argumentHash = {'Long': None, 'Lat' : None, 'simTime':None, 'beginYear': 1960, 'initialN2o': 276.889729, 'initialSf6': 0.000005, 'initialCo2':217.592896, 'initialCh4':1529.14}
def usage():
    print('please print correct input values')
    print('python main.py -a (latitude) -o (longitude) -s (simTime)')
    print('Simtime cannot exceed 660 months because we are basing rates of GH on real data ')
    print('Our limitation is that CO2 readings I currently have end at Dec. 2014, but can be extended in the future. ')
    print("")
    print("")
    print("Optional parameters include:  startings values for greenhouse gases.  ")
    exit(2)


debug = False
try:

    opt, args = getopt.getopt(sys.argv[1:], "y:a:o:s:2:4:6:0:")
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
    for a in argumentHash.keys():
        if argumentHash[a] is None:
            usage()
except getopt.GetoptError:
    usage()

#model takes in sf6, ch4, co2, no2, and long lat(that has been clustered through kmeans)

monthModels = {'Jan': None, 'Feb': None, 'Mar': None, 'Apr': None, 'May': None, 'Jun': None, 'Jul': None, 'Aug': None, 'Sep': None,  'Oct': None, 'Nov': None, 'Dec':None }

monthFName = os.listdir('../learnedLinModels/')
i = 0
for key in monthModels.keys():
    monthModels[monthFName[i][0:3]] = joblib.load('../learnedLinModels/{}'.format(monthFName[i]))
    i+=1
kMeansModel = joblib.load('../KMeansModel/KMeansModel.pkl')


# 2 dots because this is being passed in.
ghDirName = '../greenhouseRates'
sf6RatesFname ='{}/sf6Rates.csv'.format(ghDirName)
ch4RatesFname = '{}/ch4Rates.csv'.format(ghDirName)
co2RatesFname = '{}/co2Rates.csv'.format(ghDirName)
n2oRatesFname = '{}/n2oRates.csv'.format(ghDirName)


longLatHash = kMeansModel.predict( np.array([argumentHash['Long'], argumentHash['Lat']]).reshape(1,-1))
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
            print('np.array([{},{},{},{}]).reshape(1,-1) '.format(cumSf6, cumN2o, cumCo2, cumCh4))
            dtString = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
            janTemp[dtString] = monthModels['Jan'].predict(np.array([cumSf6, cumN2o, cumCo2, cumCh4, longLatHash]).reshape(1,-1))
            yield env.timeout(1)

        elif timeOfMonth == 1:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            yield env.timeout(1)
        elif timeOfMonth == 2:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            yield env.timeout(1)
        elif timeOfMonth == 3:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            yield env.timeout(1)
        elif timeOfMonth == 4:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            yield env.timeout(1)
        elif timeOfMonth == 5:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            yield env.timeout(1)
        elif timeOfMonth == 6:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            yield env.timeout(1)
        elif timeOfMonth == 7:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            yield env.timeout(1)
        elif timeOfMonth == 8:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            yield env.timeout(1)
        elif timeOfMonth == 9:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            yield env.timeout(1)
        elif timeOfMonth == 10:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            yield env.timeout(1)
        elif timeOfMonth == 11:
            ghgControl.setSimTime(argumentHash['beginYear'], timeOfMonth+1)
            cumSf6 = sf6Obj.calculateNextGh()
            cumCo2 = co2Obj.calculateNextGh()
            cumN2o = n2oObj.calculateNextGh()
            cumCh4 = ch4Obj.calculateNextGh()
            yield env.timeout(1)
            #increment year at end.




import simpy
env = simpy.Environment()
env.process(greenHouseGas(env))
env.run(until=simTime)
print(janTemp)
print(longLatHash)
