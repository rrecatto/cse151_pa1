import numpy
import urllib
import scipy.optimize
import random
import csv
import math
from operator import xor
from collections import defaultdict

with open('abalone.csv', 'rb') as f:
    reader = csv.reader(f);
    data = list(reader);

def getSampleSet(perElems, dataSet, seed):
    dataSelected = [];
    remainElems = len(dataSet);
    neededElems = math.ceil(remainElems/perElems);
    #random.seed(seed);
    for i in range(0,len(dataSet)):
        r = random.random();
        if r < neededElems/remainElems:
            # for ease of testing, we will append the index selected, not the actual element
            # dataSelected.append(dataSet[i]);
            dataSelected.append(i);
            neededElems = neededElems - 1;
        remainElems = remainElems - 1;
    return dataSelected;

# tests the getSampleSet method: hard-coded to 10,100,1000,10000,100000.
def testFunction(perElems, dataSet, seed):
    random.seed(seed);
    meanArray = [];
    sdArray = [];
    array10 = runVarTimes(perElems, dataSet, seed, 10, meanArray, sdArray);
    array100 = runVarTimes(perElems, dataSet, seed, 100, meanArray, sdArray);
    array1000 = runVarTimes(perElems, dataSet, seed, 1000, meanArray, sdArray);
    array10000 = runVarTimes(perElems, dataSet, seed, 10000, meanArray, sdArray);
    array100000 = runVarTimes(perElems, dataSet, seed, 100000, meanArray, sdArray);

    i = 10;
    for each in meanArray:
        print "Normalized mean for " + str(i) + " tests:" + str(each/i);
        i = i*10;
    i = 10;
    for each in sdArray:
        print "Normalized SD for " + str(i) + " tests: " + str(each/i);
        i = i*10;
    print meanArray;

def runVarTimes(perElems, dataSet, seed, numTimes, meanArray, sdArray):
    retArray = [0]*len(dataSet);
    for i in range(0, numTimes):
        tempArray=getSampleSet(perElems, dataSet, seed);

        for j in range(0,len(tempArray)):
            retArray[tempArray[j]] = retArray[tempArray[j]]+1;
    tempMean = numpy.mean(retArray);
    stdArray = numpy.std(retArray);
    #print tempMean/numTimes;
    #print stdArray/numTimes;
    meanArray.append(tempMean);
    sdArray.append(stdArray);



testFunction(10, data, 10);
