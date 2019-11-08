import getopt
import sys
import numpy as np
import pandas as pd
import bs4
argumentHash = {'ch4':False, 'weather': False, 'sf6':False, 'debug':False}
def prossargs():
    try:
        opt, args = getopt.getopt(sys.argv[1:], "cwnshd")
    except getopt.GetoptError:
        usage()
    for opts, arg in opt:
        if opts == '-h':
            help()
        elif opts == '-c':
            argumentHash['ch4'] = True
        elif opts == '-w':
            argumentHash['weather'] = True
        elif opts == '-s':
            argumentHash['sf6'] = True
        elif opts == 'd':
            argumentHash['debug'] = True
        else:
            help()
    flag = False
    for a in argumentHash.keys():
        if argumentHash[a] == True:
            flag = False
            break
        else:

            flag = True
    if flag:
        print('No arguments turned on.')
        help()


def help():
    print('This file is used to update or retrieve infromation from websites ')
    print('the data found is stored inside a ./data folder and goes to corresponding ')
    print('folders for the desired atmospheric condition we are grabbing.')
    usage()

def usage():
    print('please input correct flags to update data files ')
    print('c = CH4, w = weather, n=n02 s=sf6 h=help d=debugMode')
    print(
        "USAGE:  python retrieveData.py [-cwnshd]")
    exit(2)

def debug(statement):
    if argumentHash['debug']:
        print(statement)









### main ###
prossargs()
