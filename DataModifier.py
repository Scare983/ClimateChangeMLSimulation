import pandas as pd
import glob
from calendar import monthrange
import datetime as dt
import numpy as np

class DateMod():
    monthDataFrame = None
    weekDataFrame = None
    dayDataFrame = None
    def __init__(self, df, colValName):
        if "month" in df.keys():
            self.month_to_days(df,colValName)
        elif 'year' in df.keys():
            self.year_to_days(df,colValName)
        #TODO: fill in nan values created from months_to_day (They will = 0) to predicted ones.
    # testing on ch4, go up to 2014
    #returns dataframe with datetime as index, and values for each day given
    def year_to_days(self,df, colValName):
        dateObjs = []
        dateVals = []
        for i,y in enumerate(df.year):
            start = dt.date(int(y), 1, 1)
            end = dt.date(int(y)+1,1, 1)
            date = start
            days = (end - start).days
            value = int(df[colValName][i])
            while date != end:
                dateObjs.append(date)
                dateVals.append(value/days)
                date += dt.timedelta(days=1)
                df = pd.DataFrame(dateVals, index=dateObjs, columns=[colValName])
        self.dayDataFrame = df
       # self.monthDataFrame = pd.DataFrame(df[colValName].resample('M').sum(), columns=[colValName])
       # self.weekDataFrame = pd.DataFrame(df[colValName].resample('W').sum(), columns=[colValName])
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
                        dateObjs.append(dt.datetime(1960+year, month, days))
                        dateVals.append(np.nan)
        # add known dates to monthrange
        for index, row in df.iterrows():
            # check if row and month exist in delta time, if it doesn't add it.

            numDaysInMonth = (monthrange(int(row['year']), int(row['month']))[1])
            valueToAppendToDay = int(row[colValName])/numDaysInMonth
            for days in range(1, numDaysInMonth+1):
                dateObjs.append(dt.datetime(int(row['year']), int(row['month']), days))
                dateVals.append(valueToAppendToDay)

        # TODO HERE:  add dates after the end date of the given df to equal 2019.... maybe..
        df = pd.DataFrame(dateVals, index=dateObjs, columns=[colValName])
        self.dayDataFrame = df
        self.monthDataFrame = pd.DataFrame(df[colValName].resample('M').sum(), columns=[colValName])
        self.weekDataFrame = pd.DataFrame(df[colValName].resample('W').sum(), columns=[colValName])


#graph single dataframesUse.  Use this to determine how to create a function for past values
def graph_weeklyData(self, dataFrame):
    pass

#graph all of the dataframes.  Use this to determine how to create a function for past values
#give it several
def graph_all(self, combinedDataFrame):
    pass


# if called from main, we want to test this file, so create dataframes and pass em in.
# TODO: might want to put graph_all, and graph_weekly into new class, along with our training models.
def test_code(debug):
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


def usage():
    print('python DataModifier [-d]')

##MAIN METHOD##
if __name__ == '__main__':
    import getopt
    import sys
    debug = False
    try:
        opt, args = getopt.getopt(sys.argv[1:], "d")
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opts, arg in opt:
        if opts == '-d':
            debug = True


    test_code(debug)
