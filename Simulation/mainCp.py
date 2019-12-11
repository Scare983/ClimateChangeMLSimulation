from GreenHouseAgents import test
### Simulation from 1960 to 2012 about different variable greenhouse gases.
from sklearn.externals import joblib
import os
import numpy as np
argumentHash = {'Long': None, 'Lat' : None, 'rate': None, 'timeIsMonth': True}
def usage():
    print('please print correct input values')
    exit(2)

import getopt
import sys
debug = False
try:
    opt, args = getopt.getopt(sys.argv[1:], "l:o:r:y")

    for opts, arg in opt:
        if opts == '-l':#long
            argumentHash['Long'] = float(arg)
        elif opts == '-y':
            argumentHash['timeIsMonth'] = False
        elif opts == '-o':#lat
            argumentHash['Lat'] = float(arg)
        elif opts == '-r':#rate
            argumentHash['rate'] = arg
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
print(kMeansModel.predict( np.array([argumentHash['Long'], argumentHash['Lat']]).reshape(1,-1)  ))


# this is starting greenhouse gas from 1960.  Can make this
initialSf6 = 3.876
initialCo2 = 7066.814
initialN2o = 305.806
initialCh4 = 1572.580
longLatHash = kMeansModel.predict( np.array([argumentHash['Long'], argumentHash['Lat']]).reshape(1,-1))
simTime = 600
# we are calculating yearly change.
if argumentHash['timeIsMonth'] == False:
    simTime = 50

#600 months pass is the time of simulation.
# if time argument is months, we calculaute each month, if year we sum and average all predictions of a year.
def greenHouseGas(env):
    cumSumGH = {'sf6': initialSf6, 'n2o': initialN2o, 'co2': initialCo2, 'ch4':initialCh4, 'longLat': longLatHash}
    janTemp, febTemp, marTemp, aprTemp, mayTemp, junTemp, julTemp, augTemp, sepTemp, octTemp, novTemp, novTemp, decTemp = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}

    beginYear = 1960
    while True:

        if argumentHash['timeIsMonth'] == False:
            pass
        else:
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
                pass

import simpy
env = simpy.Environment()
env.process(greenHouseGas(env))
env.run(until=simTime)

