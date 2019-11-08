import getopt
import sys
import numpy as np
import pandas as pd

def prossargs():
    try:
        opt, args = getopt.getopt(sys.argv[1:], "")
    except getopt.GetoptError:
        usage()def prossargs():
    try:
        opt, args = getopt.getopt(sys.argv[1:], "s:fk:")
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opts, arg in opt:
        if opts == '-s':
            if not arg.isdigit():
                usage()
            elif int(arg) <=0:
                print('Cannot have simtime <= 0, exiting...')
            else:
                argumentHash['SIM_TIME'] = int(arg)
        elif opts == '-f':
            argumentHash['isFixedLatency'] = True
        elif opts == '-k':
            if not arg.isdigit():
                usage()
            elif int(arg) <=0:
                print('Cannot have K <= 0, exiting...')
            else:
                argumentHash['maxLatency'] = int(arg)
    for a in argumentHash.keys():
        if argumentHash[a] is None:
            usage()



def help():
    print('This file is used to update or retrieve infromation from websites ')
    print('the data found is stored inside a ./data folder and goes to corresponding ')
    print('folders for the desired atmospheric condition we are grabbing.')
def usage():
    print('please input correct flags to update data files ')
    print('C = CH4, w = weather, n=n02 s=sf6 h=help')
    print(
        "python retrieveData [-cwnsh] ")
    exit(2)


    sys.exit(2)
    for opts, arg in opt:
        if opts == '-s':
            if not arg.isdigit():
                usage()
            elif int(arg) <=0:
                print('Cannot have simtime <= 0, exiting...')
            else:
                argumentHash['SIM_TIME'] = int(arg)
        elif opts == '-f':
            argumentHash['isFixedLatency'] = True
        elif opts == '-k':
            if not arg.isdigit():
                usage()
            elif int(arg) <=0:
                print('Cannot have K <= 0, exiting...')
            else:
                argumentHash['maxLatency'] = int(arg)
    for a in argumentHash.keys():
        if argumentHash[a] is None:
            usage()


def usage():
    print('please input only int values for args')
    print(
        "python ping.py -s 'INT-TIME' [-f optional ] -k 'INT -upper Latency'")
    exit(2)

