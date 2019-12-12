import pandas as pd
import datetime
class ghgControl():
    simYear = 0
    simMonth=0
    def __init__(self, ghRateFName, initialValue):
        rates = pd.read_csv(ghRateFName)
        self.cumValue = pd.DataFrame(columns=['dt', 'cumSum'])
        self.initialValue= initialValue
        self.addToCumSum(initialValue)
        self.baseRate = rates['rate'].to_list()
        #rate at which we may redact a policy.
    def addToCumSum(self,  ghg):
        myDate = '{}-{}'.format(ghgControl.getSimDatetimeString().year, ghgControl.getSimDatetimeString().month)
        df = pd.DataFrame({'dt':[myDate], 'cumSum': [ghg]})
        self.cumValue = self.cumValue.append(df, ignore_index=True)
        ###increase chaos and policy rate here.

    def getCumValue(self):
        return self.cumValue['cumSum'].values[-1]
    def getCumDf(self):
        return self.cumValue
    def popNextRate(self):
        return self.baseRate.pop(0)
    def start(self):
        self.popNextRate()
        return self.initialValue



    @staticmethod
    def setSimTime(yearTime, monthTime):
        ghgControl.simYear = yearTime
        ghgControl.simMonth = monthTime
    @staticmethod
    def getSimTime():
        return ghgControl.simYear, ghgControl.simMonth
    @staticmethod
    def getSimDatetimeString():
        year, month = ghgControl.getSimTime()
        return datetime.datetime(year, month, 1)


