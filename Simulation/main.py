### Simulation from 1960 to 2012 about different variable greenhouse gases.
from sklearn.externals import joblib
import os
import numpy as np
from GreenHouseAgents.ghgControl import ghgControl
import GreenHouseAgents.defaultAgent as GHContainer
import getopt
import sys
argumentHash = {'Long': None, 'Lat' : None, 'simTime':None}
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

    opt, args = getopt.getopt(sys.argv[1:], "a:o:s:")
    for opts, arg in opt:
        if opts == '-o':#long
            argumentHash['Long'] = float(arg)
        elif opts == '-a':#lat
            argumentHash['Lat'] = float(arg)
        elif opts == '-s':#simTime
            if(int(arg) > 660):
                usage()
            argumentHash['simTime'] = int(arg)
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

# this is starting greenhouse gas from 1960 in January. Instantiate default values.
initialSf6 = 0.000005
initialCo2 = 217.592896
initialN2o = 276.889729
initialCh4 = 1529.14
# 2 dots because this is being passed in.
ghDirName = '../greenhouseRates'
sf6RatesFname ='{}/sf6Rates.csv'.format(ghDirName)
ch4RatesFname = '{}/ch4Rates.csv'.format(ghDirName)
co2RatesFname = '{}/co2Rates.csv'.format(ghDirName)
n2oRatesFname = '{}/n2oRates.csv'.format(ghDirName)


longLatHash = kMeansModel.predict( np.array([argumentHash['Long'], argumentHash['Lat']]).reshape(1,-1))
simTime = 600
# we are calculating yearly change.


#600 months pass is the time of simulation.
# if time argument is months, we calculaute each month, if year we sum and average all predictions of a year.

### initialization complete.  Run simulation.


def greenHouseGas(env):
    cumSumGH = {'sf6': initialSf6, 'n2o': initialN2o, 'co2': initialCo2, 'ch4':initialCh4, 'longLat': longLatHash}
    janTemp, febTemp, marTemp, aprTemp, mayTemp, junTemp, julTemp, augTemp, sepTemp, octTemp, novTemp, novTemp, decTemp = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
    beginYear = 1960

    ghgControl.setSimTime(beginYear)
    ch4Obj = GHContainer.ch4Control(ch4RatesFname, initialCh4)
    co2Obj = GHContainer.co2Control(co2RatesFname, initialCo2)
    sf6Obj = GHContainer.sf6Control(sf6RatesFname, initialSf6)
    n2oObj = GHContainer.n2oControl(n2oRatesFname, initialN2o)

    while True:
        timeOfMonth = env.now % 12
        if timeOfMonth == 0:
            yield env.timeout(1)

        elif timeOfMonth == 1:
            yield env.timeout(1)
        elif timeOfMonth == 2:
            yield env.timeout(1)
        elif timeOfMonth == 3:
            yield env.timeout(1)
        elif timeOfMonth == 4:
            yield env.timeout(1)
        elif timeOfMonth == 5:
            yield env.timeout(1)
        elif timeOfMonth == 6:
            yield env.timeout(1)
        elif timeOfMonth == 7:
            yield env.timeout(1)
        elif timeOfMonth == 8:
            yield env.timeout(1)
        elif timeOfMonth == 9:
            yield env.timeout(1)
        elif timeOfMonth == 10:
            yield env.timeout(1)
        elif timeOfMonth == 11:
            yield env.timeout(1)
            #increment year at end.
            beginYear +=1
            ghgControl.setSimTime(beginYear)

            pass

import simpy
env = simpy.Environment()
env.process(greenHouseGas(env))
env.run(until=simTime)

