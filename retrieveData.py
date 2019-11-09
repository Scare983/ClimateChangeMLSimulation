import getopt
import sys
import urllib.request
from os.path import exists
from os import remove
import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
argumentHash = {'ch4':False, 'n02':True, 'weather': False, 'sf6':False, 'debug':False}
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
        elif opts == 'n':
            arg['n02'] = True
        elif opts == '-w':
            argumentHash['weather'] = True
        elif opts == '-s':
            argumentHash['sf6'] = True
        elif opts == '-d':
            argumentHash['debug'] = True
        else:
            help()
    flag = False
    for a in argumentHash.keys():
        if argumentHash[a]:
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




def getCh4():
    # this website has several pages of .txt files that we have to parse and
    # grab the data through ftp,
    # different webpages can be associted with pageID=###
    website = 'https://www.esrl.noaa.gov/gmd/dv/data/index.php?pageID=1&category=Greenhouse%2BGases&parameter_name=Methane'
    page = requests.get(website)
    debug(page.status_code)
    i = 1

    while page.status_code == 200:
        base = './data/Ch4/'
        soup = BeautifulSoup(page.content, 'html.parser')
        tbody = soup.find('tbody')
        #debug(tbody.find_all('tr'))
        # get first span in first td. which should be ID.
        currIndex = tbody.find('tr').td.span.get_text()
        #debug(currIndex)

        for tr in tbody.find_all('tr'):
            debug(tr.find_all('td')[1].span.get_text())
            allTD = tr.find_all('td')
            cityCountry = allTD[1].span.get_text()
            debug(allTD[5].get_text())
            isMonth = allTD[5].get_text()
            # debug(allTD[7].a['href'])
            #we want to store the data if this is true
            data = urllib.request.Request(allTD[7].a['href'])


            # actual
            if isMonth == 'Monthly Averages':
                data = urllib.request.Request(allTD[7].a['href'])
                with urllib.request.urlopen(data) as response:
                    downloadPage = response.read()
                nameList = cityCountry.split(',')
                fileNameTxt = base + "_".join(nameList)
                fileNameCsv = base + "_".join(nameList) + '.csv'
                if exists(fileNameCsv):

                    # might want to change this to break out of all loops
                    break
                else:

                    downloadPage = downloadPage.decode()

                    fileHandle = open(fileNameTxt, 'w')
                    fileHandle.write(downloadPage)
                    fileHandle.close()
                    fileHandle = open(fileNameTxt, 'r')
                    line = fileHandle.readline()
                    # remove comments. But we need last comment
                    dataHeader = ""
                    fileHandle2 = open(fileNameCsv, 'w')
                    while line:
                        if 'data_fields:' in line:
                            dataHeader = line.replace('# data_fields: ', "")
                            # debug(dataHeader)
                            dataHeader = dataHeader.replace(' ', ',')
                            fileHandle2.write(dataHeader)
                        else:
                            newLine = re.sub(r'#.*', '', line)
                            newLine = re.sub(r' +', ' ', newLine)
                            if newLine != "\n":
                                # print(newLine)
                                newLine = newLine.split(' ')
                                newLine = ','.join(newLine)
                                fileHandle2.write(newLine)
                        line = fileHandle.readline()
                    fileHandle.close()
                    fileHandle2.close()
                    remove(fileNameTxt)
        i+=1
        website ='https://www.esrl.noaa.gov/gmd/dv/data/index.php?pageID={}&category=Greenhouse%2BGases&parameter_name=Methane'.format(i)
        page = requests.get(website)
        if page.status_code == 200:
        # check index with previous
            soup = BeautifulSoup(page.content, 'html.parser')
            tbody = soup.find('tbody')
            nextIndex = tbody.find('tr').td.span.get_text()
            if nextIndex == currIndex:
            #            # there are no more pages and we go into a loop if we do not do this.
                break
            else:
                continue
        else:
            break

def updateCh4():
    pass


def getWeather():
    pass

def updateWeather():
    pass

def getN02():
    pass

def updateN02():
    pass

def getSf6():
    pass

def updateSf6():
    pass

### main ###
prossargs()
if argumentHash['ch4']:
    getCh4()
if argumentHash['weather']:
    getWeather()
if argumentHash['sf6']:
    getSf6()
if argumentHash['n02']:
    getN02()
