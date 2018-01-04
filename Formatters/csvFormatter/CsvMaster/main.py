__author__ = 'TheBestPythonPerfectTeam'

import csv
import json

#modify to fit current csv
csvCategoryPosition = 2
csvCountPosition = 14
fileName = 'Data/worldPopulation.csv'
storeName = 'World Population.txt'


arrayOfEntries = []
with open(fileName, 'r') as csvfile:
    reader = csv.reader(csvfile)
    stop = 1
    for row in reader:
        if stop == 1:
            stop = 0
        elif not int(row[csvCountPosition]) == 0:
            arrayOfEntries.append((row[csvCategoryPosition],int(row[csvCountPosition]) ))
setOfEntries = set()
for entry in arrayOfEntries:
    setOfEntries.add(entry)

filteredArray = []
for entry in setOfEntries:
    filteredArray.append(entry)

PerfectArray = sorted(filteredArray, key=lambda tup: tup[1],reverse=True)


results = open("Results - " + storeName,"w")
for perfectStuff in json.dumps(PerfectArray, sort_keys=True, indent=4, separators=(',', ': ')):
    results.write(perfectStuff)
results.close()

print("FINISHED!!")







