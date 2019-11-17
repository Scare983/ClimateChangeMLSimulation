import pandas as pd
import glob
from calendar import monthrange
import datetime
import numpy as np




#graph single dataframesUse.  Use this to determine how to create a function for past values
def graph_weeklyData(dataFrame):
    pass

#graph all of the dataframes.  Use this to determine how to create a function for past values
def graph_all(combinedDataFrame):
    pass


# testing on ch4, go up to 2014
def month_to_daysCH4(df):
    monthRanges = []
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
        numDaysInMonth = (monthrange(row['year'], row['month'])[1])
        valueToAppendToDay = row['value']/numDaysInMonth
        for days in range(1, numDaysInMonth+1):
            dateObjs.append(datetime.datetime(row['year'], row['month'], days))
            dateVals.append(valueToAppendToDay)

    # TODO HERE:  add dates after the end date of the given df to equal 2019.... maybe..
    return pd.DataFrame(dateVals, index=dateObjs, columns=['value'] )




# if called from main, we want to test this file, so create dataframes and pass em in.
def test_code():
    sf6_data = pd.read_csv('./data/Sf6/sf6_mm_gl.csv')
    for file in glob.glob('./data/Ch4/*'):
        ch4_data = pd.read_csv(file, header=0)
        ch4_data = month_to_daysCH4(ch4_data)
        #dates = pd.to_datetime(ch4_data[['year', 'month']])
        #otherData = pd.DataFrame(ch4_data['value'],index=dates)
        ch4_data = ch4_data['value'].resample('W').sum()
        print(ch4_data)
        break


if __name__ == '__main__':
    test_code()
    pass