import pandas as pd
class ghgControl():
    simTime = 0
    def __init__(self, ghRateFName):
        rates = pd.read_csv(ghRateFName)
        self.cumValue = pd.DataFrame(columns=['date', 'cumSum'])
        self.baseRate = rates['rate'].to_list()
        #rate at which we may redact a policy.
        self.chaosRate = .0001
        # rate at which we may create a policy eachy month.
        self.richteousRate = .0001
    def addToCumSum(self, date, ghg):
        df = pd.DataFrame([date, ghg], columns=['date', 'cumSum'])
        self.cumValue.append(df, ignore_index=True)
    def getCumValue(self):
        return self.cumValue['cumSum'][-1]
    def popNextRate(self):
        return self.baseRate.pop(0)
    @staticmethod
    def setSimTime(yearTime):
        ghgControl.simTime = yearTime
    @staticmethod
    def getSimTime():
        return ghgControl.simTime