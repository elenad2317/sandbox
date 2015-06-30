#!/usr/bin/python
import pandas as pd # to generate json you need version newer than 0.12
# to generate excel you need openpyxl 1.8.6
import numpy as np
import random
import sys
import getopt 

########## The following are random number generators #############

def randString(l):
    # generates a string of random ints of len l  
    less = 10**(l-1)
    more = 10**l 
    n = random.randint(less, more)
    return str(n)

def randDate():
    # generates a random date, returns string of form "MM-DD-YYYY"
    m = random.randint(0,12)
    if len(str(m)) < 2:
        sm = '0' + str(m)
    else: 
        sm = str(m)
    d = random.randint(0,12)
    if len(str(d)) < 2: 
        sd = '0' + str(d)
    else: 
        sd = str(d)
    y= random.randint(1950, 2015)
    return sm + '-' + sd + '-' + str(y)

def randCost(): 
    # generates random cost between 100 and 100000
    # returns string of form "343"
    x = random.randint(3,6)
    return "$"+ randString(x)

def randLowCost():
    # generate random cost between 0 and 1000
    # returns string of form "$223"
    x = random.randint(10,99)
    return x

def randRate(): 
    # returns string of form "0.12"
    rate = random.randint(0,100)
    return str(float(rate)/100)

campaign = 'CAMPAIGN_TEST'
org= 'ORG_TEST'
strategy = 'STRATEGY_TEST'
seg = 'SEG_TEST'
provider = 'DATA_PROVIDER'

def genRow():
    # generates numpy array of the form hardcoded in accordance with columns 
    return np.array([org, campaign, strategy, randDate(), seg, provider, randString(5), randString(6), randRate(), randString(4), randString(4), randString(4), randString(4), randLowCost(), randLowCost(), randRate(), randString(3), randString(4), randString(4), randString(3), randLowCost(), randLowCost(), randLowCost(), randLowCost(), randString(4), randString(4), randString(4)])


matrix = []
for i in range(21): 
    matrix.append(genRow())
Matrix = np.matrix(matrix)

df = pd.DataFrame(Matrix,  columns = ('Organization', 'Campaign', 'Strategy', 'Report Date', 'Segment Name', 'Data Provider', 'UUIDs', 'Impressions', '% of Campaign Impressions', 'Clicks', 'PV Conversions', 'PC Conversions', 'Total Conversions', 'CTR', 'CTC', 'Response Rate', 'Media Cost', 'Total Spend', 'Total Ad Cost', 'Segment Cost', 'CPM', 'CPC', 'Total Spend/Clicks', 'CPA', 'PC Revenue', 'PV Revenue', 'Revenue'))

#############################################################################

import json
def makejson(df, filename): 
    end_dict = {'status': {"code":"success"}, 'data': []}
    for index, row in df.iterrows(): 
        user_row = {str(col) : row[col] for col in df.columns}
        #user_row should be js object 
        end_dict['data'].append( user_row)
    
    f = open(filename, 'w')
    json.dump(end_dict,f)

def main(df):
    opts, args = getopt.getopt(sys.argv[1:], 'h', ['sort-by', 'format'])
    for i in range(len(opts)): 
        if opts[i][0] == '-h':
            print "mock-backtest.py --sort-by <'CPC', 'CPA',or 'CPM'> -format <'csv', 'excel', or 'json'>"
            sys.exit(1)

        elif opts[i][0] == '--sort-by':
            sortby = args[i] 
        elif opts[i][0] == '--format':
            form = args[i]
    result = df.sort('CPC', ascending = False)
    if form == "csv": 
        result.to_csv('output.csv')
    elif form == "excel":
        result.to_excel('output.xlsx')
    elif form == "json":
        makejson(df, 'output.txt')
      
    return None 


if __name__ == "__main__":
    main(df)


