import pandas as pd
import glob
from calendar import monthrange
import datetime
import numpy as np

class DateMod():
    monthDataFrame = None
    weekDataFrame = None
    dayDataFrame = None
    def __init__(self, df, colValName):
        self.month_to_days(df,colValName)

    # testing on ch4, go up to 2014
    #returns dataframe with datetime as index, and values for each day given
    def month_to_days(self, df, colValName):
        dateObjs = []
        dateVals = []
        if int(df.year[0]) > 1960:
            diff = int(df.year[0]) - 1960
            # find delta, and append to month range list

            for year in range(diff+1):
                for month in range(1, 13):
                    # check if current year needs months added
                    if 1960+year == int(df.year[0]) and int(df.month[0]) == month:
                        break
                    for days in range(1, (monthrange(int(df.year[0]) + year, month)[1])):
                        dateObjs.append(datetime.datetime(1960+year, month, days))
                        dateVals.append(np.nan)

        # add known dates to monthrange
        for index, row in df.iterrows():
            # check if row and month exist in delta time, if it doesn't add it.

            numDaysInMonth = (monthrange(int(row['year']), int(row['month']))[1])
            valueToAppendToDay = int(row[colValName])/numDaysInMonth
            for days in range(1, numDaysInMonth+1):
                dateObjs.append(datetime.datetime(int(row['year']), int(row['month']), days))
                dateVals.append(valueToAppendToDay)

        # TODO HERE:  add dates after the end date of the given df to equal 2019.... maybe..
        df = pd.DataFrame(dateVals, index=dateObjs, columns=[colValName])
        self.dayDataFrame = df
        self.monthDataFrame = df[colValName].resample('M').sum()
        self.weekDataFrame = df[colValName].resample('W').sum()


#graph single dataframesUse.  Use this to determine how to create a function for past values
def graph_weeklyData(self, dataFrame):
    pass

#graph all of the dataframes.  Use this to determine how to create a function for past values
#give it several
def graph_all(self, combinedDataFrame):
    pass


    # if called from main, we want to test this file, so create dataframes and pass em in.
def test_code():
    sf6_data = pd.read_csv('./data/Sf6/sf6_mm_gl.csv', header=0)
    sf6_obj = DateMod(sf6_data, 'average')
    n2o_data = pd.read_csv('./data/N2o/n2o_mm_gl.csv',header=0)
    n2o_obj = DateMod(n2o_data, 'average')
    for file in glob.glob('./data/Ch4/*'):
        ch4_data = pd.read_csv(file, header=0)
        ch4_obj = DateMod(ch4_data, 'value')
        #print(ch4_obj.monthDataFrame)
        break


if __name__ == '__main__':
    test_code()
    pass