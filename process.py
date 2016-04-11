import numpy
import urllib
import scipy.optimize
import random
import csv
import math
import graphics
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
    runVarTimes(perElems, dataSet, seed, 10, meanArray, sdArray);
    runVarTimes(perElems, dataSet, seed, 100, meanArray, sdArray);
    runVarTimes(perElems, dataSet, seed, 1000, meanArray, sdArray);
    runVarTimes(perElems, dataSet, seed, 10000, meanArray, sdArray);
    runVarTimes(perElems, dataSet, seed, 100000, meanArray, sdArray);

    i = 10;
    for each in meanArray:
        print "Normalized mean for " + str(i) + " tests:" + str(each/i);
        i = i*10;
    i = 10;
    for each in sdArray:
        print "Normalized SD for " + str(i) + " tests: " + str(each/i);
        i = i*10;

    plot(meanArray);
    print meanArray;

def runVarTimes(perElems, dataSet, seed, numTimes, meanArray, sdArray):
    retArray = [0]*len(dataSet);
    for i in range(0, numTimes):
        tempArray=getSampleSet(perElems, dataSet, seed);

        for j in range(0,len(tempArray)):
            retArray[tempArray[j]] = retArray[tempArray[j]]+1;
    tempMean = numpy.mean(retArray);
    stdArray = numpy.std(retArray);
    meanArray.append(tempMean);
    sdArray.append(stdArray);


def plot(meanArray):
    win = graphics.GraphWin("Plot",800, 600);
    t = graphics.Line(graphics.Point(50,550), graphics.Point(750,550));
    t.setArrow("last");
    t.draw(win);
    t = graphics.Line(graphics.Point(50,550), graphics.Point(50,20));
    t.setArrow("last");
    t.draw(win);
    t = graphics.Text(graphics.Point(750,560), "Number of runs");
    t.draw(win);
    t = graphics.Text(graphics.Point(50,10), "Mean");
    t.draw(win);

    t = graphics.Text(graphics.Point(50,560), "0");
    t.draw(win);

    t = graphics.Line(graphics.Point(150,552), graphics.Point(150,548));
    t.draw(win);
    t = graphics.Text(graphics.Point(150,560), "10");
    t.draw(win);

    t = graphics.Line(graphics.Point(250,552), graphics.Point(250,548));
    t.draw(win);
    t = graphics.Text(graphics.Point(250,560), "100");
    t.draw(win);

    t = graphics.Line(graphics.Point(350,552), graphics.Point(350,548));
    t.draw(win);
    t = graphics.Text(graphics.Point(350,560), "1000");
    t.draw(win);

    t = graphics.Line(graphics.Point(450,552), graphics.Point(450,548));
    t.draw(win);
    t = graphics.Text(graphics.Point(450,560), "10000");
    t.draw(win);

    t = graphics.Line(graphics.Point(550,552), graphics.Point(550,548));
    t.draw(win);
    t = graphics.Text(graphics.Point(550,560), "100000");
    t.draw(win);

    t = graphics.Line(graphics.Point(650,552), graphics.Point(650,548));
    t.draw(win);
    t = graphics.Text(graphics.Point(650,560), "1000000");
    t.draw(win);

    t = graphics.Line(graphics.Point(48,450), graphics.Point(52,450));
    t.draw(win);
    t = graphics.Text(graphics.Point(25,450), "1");
    t.draw(win);

    t = graphics.Line(graphics.Point(48,350), graphics.Point(52,350));
    t.draw(win);
    t = graphics.Text(graphics.Point(25,350), "10");
    t.draw(win);

    t = graphics.Line(graphics.Point(48,250), graphics.Point(52,250));
    t.draw(win);
    t = graphics.Text(graphics.Point(25,250), "100");
    t.draw(win);

    t = graphics.Line(graphics.Point(48,150), graphics.Point(52,150));
    t.draw(win);
    t = graphics.Text(graphics.Point(25,150), "1000");
    t.draw(win);

    t = graphics.Line(graphics.Point(48,50), graphics.Point(52,50));
    t.draw(win);
    t = graphics.Text(graphics.Point(25,50), "10000");
    t.draw(win);

    i = 150;
    count = 10;
    last_point = [50, 550];
    for each in meanArray:
        raw_y = math.log10(each);
        y = 450 - raw_y*100;
        c = graphics.Circle(graphics.Point(i, y), 5);
        c.setOutline("red");
        c.draw(win);
        t = graphics.Text(graphics.Point(i,y+13), "(" + str(count) + "; " + str(each) + ")");
        t.draw(win);
        t = graphics.Line(graphics.Point(last_point[0], last_point[1]), graphics.Point(i,y));
        t.draw(win);
        last_point = [i, y];
        i += 100; 
        count *= 10;
    win.getMouse();
    win.close();



testFunction(10, data, 10);
