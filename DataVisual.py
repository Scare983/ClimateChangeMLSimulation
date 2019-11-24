import pandas as pd
import glob
from calendar import monthrange
import datetime as dt
import numpy as np
from DataModifier import DateMod, IPA
from matplotlib import pyplot as plt

sf6_data = pd.read_csv('./data/Sf6/sf6_mm_gl.csv', header=0)
sf6_obj = DateMod(sf6_data, 'average', 'sf6')
n2o_data = pd.read_csv('./data/N2o/n2o_mm_gl.csv',header=0)
n2o_obj = DateMod(n2o_data, 'average', 'n2o')
ch4_data = dict()
ch4_txt = open('./data/Ch4/ch4_mm_gl.txt',mode='r')
keys = ch4_txt.readline().split()
for key in keys:
    ch4_data[key] = []
for line in ch4_txt:
    for i, v in enumerate(line.split()):
        ch4_data[keys[i]].append(v)
ch4_data = pd.DataFrame(ch4_data)
ch4_data = ch4_data.apply(pd.to_numeric)
ch4_obj = DateMod(ch4_data, 'average', 'ch4')
co2_data = pd.read_csv('./data/CO2Emission/global.1751_2014.csv', header=0)
co2_data = co2_data.rename(columns={'Year':'year','Total carbon emissions from fossil fuel consumption and cement production (million metric tons of C)':'CarbonEmissions'})
co2_data = co2_data.loc[:,['year','CarbonEmissions']]
co2_data = co2_data.drop(co2_data.index[0]).reset_index(drop=True)
co2_data = co2_data.apply(pd.to_numeric)
co2_obj = DateMod(co2_data,'CarbonEmissions', "CO2")

greenhouse = [sf6_obj,n2o_obj,ch4_obj, co2_obj]
for obj in greenhouse:
    plt.plot(list(obj.dayDataFrame.index), obj.dayDataFrame.values.tolist())
    plt.title(obj.dataName + " " +  obj.colVal + " over time")
    plt.show()