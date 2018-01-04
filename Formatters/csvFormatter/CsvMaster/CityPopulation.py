def getDictionary (filename):
    dataFile = open (filename, 'r')
    cityPopDictionary = dict()
    dataFile.readline()
    for line in dataFile: 
        linelist = line.strip('\n').split(',')
        if(linelist[0] != '40' and linelist[0] != '50' and linelist[2] == '0') : #and ("balance" not in linelist[5])) :
            cityPopDictionary[linelist[5]] = int(linelist[18])
    dataFile.close()
    return cityPopDictionary

cityPopDictionary = getDictionary('cityPopulation.csv')
for city in sorted(cityPopDictionary,key = cityPopDictionary.get , reverse = True) :
    print("{:25s} {:3d}".format(city,cityPopDictionary[city]))
