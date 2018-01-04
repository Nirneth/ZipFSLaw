__author__ = 'miguelabreu'

import json
import math
import matplotlib.pyplot as plt
import numpy as np

def calculateZipfTableWithJsonObject(jsonObject):
    rank = 1
    zipfTable = []
    maxValue = jsonObject[0][1]
    for entry in jsonObject:
        category = entry[0]
        frequency = entry[1]
        zipfTable.append((category,rank,frequency,math.log(rank,10),math.log(frequency,10),math.log(maxValue/rank,10)))
        rank += 1

    return zipfTable

fileName = "Data/Results - World Population.txt"
reportName = "World Population"

file = open(fileName)
jsonObject = json.load(file)

xValues = []
yValues = []
expectedYValues = []
realValues = []
realCategories = []

for tuple in calculateZipfTableWithJsonObject(jsonObject):
    print(tuple)
    ##if tuple[1] > 70:
    ##    break
    realCategories.append(tuple[0])
    realValues.append(tuple[2])
    xValues.append(tuple[3])
    yValues.append(tuple[4])
    expectedYValues.append(tuple[5])

## deviation
deviation = 0
for i in range(len(expectedYValues)):
    deviation += abs(expectedYValues[i] - yValues[i])
deviation = deviation / len(yValues)

##REPORT
reportFile = open("Report - "+reportName + ".txt","w")

reportFile.write("Total Categories : " + str(len(yValues)))
reportFile.write("\nMax Value        : " + str(realValues[0]))
reportFile.write("\nTop Category     : " + realCategories[0])
reportFile.write("\nDeviation        : " + str( round(deviation * 100,2)) + "%")
reportFile.close()

##Plot

slope,intercept=np.polyfit(xValues,yValues,1)
ablineValues = []
for i in xValues:
  ablineValues.append(slope*i+intercept)
plt.plot(xValues, ablineValues, 'g--')
plt.plot(xValues, yValues, 'ro',xValues,expectedYValues,'b-')
plt.title(fileName)
plt.show()